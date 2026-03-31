package com.danielmichalski.rss.web.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import com.danielmichalski.rss.core.entity.RssFeedEntryEntity;
import com.danielmichalski.rss.core.service.IRssFeedItemService;
import com.danielmichalski.rss.core.service.IRssFeedService;
import com.danielmichalski.rss.core.service.IUserService;

import java.util.List;

/**
 * Author: Daniel
 */
@Controller
@RequestMapping("/")
public class HomeController {

    private IRssFeedItemService itemService;

    private IRssFeedService rssFeedService;

    private IUserService userService;

    @Autowired
    public HomeController(IRssFeedItemService itemService, IRssFeedService rssFeedService, IUserService userService) {
        this.itemService = itemService;
        this.rssFeedService = rssFeedService;
        this.userService = userService;
    }

    @RequestMapping(method = RequestMethod.GET)
    public String index(@RequestParam(value = "q", required = false) String query, Model model) {
        String normalizedQuery = query == null ? "" : query.trim();
        List<RssFeedEntryEntity> items = normalizedQuery.isEmpty()
                ? itemService.find10NewestEntries()
                : itemService.searchNewestEntries(normalizedQuery, 10);

        model.addAttribute("items", items);
        model.addAttribute("searchQuery", normalizedQuery);
        model.addAttribute("isSearchActive", !normalizedQuery.isEmpty());
        model.addAttribute("totalArticles", itemService.countAllEntries());
        model.addAttribute("totalChannels", rssFeedService.countAllFeeds());
        model.addAttribute("totalUsers", userService.countAllUsers());
        return "index";
    }

}
