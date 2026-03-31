package com.danielmichalski.rss.web.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import com.danielmichalski.rss.core.entity.RssFeedEntity;
import com.danielmichalski.rss.core.service.IRssFeedService;
import com.danielmichalski.rss.core.service.IUserService;

import javax.validation.Valid;
import java.security.Principal;
import java.util.stream.Collectors;
import com.danielmichalski.rss.core.entity.UserEntity;

/**
 * Author: Daniel
 */
@Controller
public class UserController {

    private IUserService userService;

    private IRssFeedService blogService;

    @Autowired
    public UserController(IUserService userService, IRssFeedService blogService) {
        this.userService = userService;
        this.blogService = blogService;
    }

    @RequestMapping("account")
    public String account(Model model, Principal principal) {
        String userName = principal.getName();
        UserEntity user = userService.findOneWithAllBlogs(userName);
        long totalAccountItems = user.getBlogEntities().stream()
                .map(blog -> blog.getItemEntities() == null ? 0 : blog.getItemEntities().size())
                .collect(Collectors.summingInt(Integer::intValue));
        model.addAttribute("blog", new RssFeedEntity());
        model.addAttribute("user", user);
        model.addAttribute("totalAccountItems", totalAccountItems);
        return "account";
    }

    @RequestMapping(value = "account", method = RequestMethod.POST)
    public String doAddBlog(@Valid @ModelAttribute("blog") RssFeedEntity rssFeedEntity, Model model,
                            Principal principal, BindingResult result, RedirectAttributes redirectAttributes) {
        String submittedUrl = rssFeedEntity.getUrl() == null ? "" : rssFeedEntity.getUrl().trim();
        boolean duplicateUrl = userService.findOneWithAllBlogs(principal.getName()).getBlogEntities().stream()
                .anyMatch(blog -> blog.getUrl() != null
                        && blog.getUrl().trim().equalsIgnoreCase(submittedUrl));
        if (duplicateUrl) {
            result.rejectValue("url", "page.myAccount.error.duplicateUrl");
        }
        if (result.hasErrors()) {
            return account(model, principal);
        }
        try {
            String name = principal.getName();
            blogService.save(rssFeedEntity, name);
            redirectAttributes.addFlashAttribute("successMessage", "New RSS channel added successfully.");
        } catch (IllegalArgumentException e) {
            result.rejectValue("url", "page.myAccount.error.unreachableUrl");
            return account(model, principal);
        }
        return "redirect:/account";
    }

    @RequestMapping(value = "blog/remove/{id}", method = RequestMethod.POST)
    public String removeBlog(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        RssFeedEntity rssFeedEntity = blogService.findOne(id);
        blogService.delete(rssFeedEntity);
        redirectAttributes.addFlashAttribute("successMessage", "RSS channel removed successfully.");
        return "redirect:/account";
    }

    @RequestMapping(value = "blog/refresh/{id}", method = RequestMethod.POST)
    public String refreshBlog(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        RssFeedEntity rssFeedEntity = blogService.findOne(id);
        blogService.refresh(rssFeedEntity);
        redirectAttributes.addFlashAttribute("successMessage", "RSS channel refreshed successfully.");
        return "redirect:/account";
    }

}
