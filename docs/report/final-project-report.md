# FINAL PROJECT REPORT

## RSS Feed Reader Project Using Git and GitHub

Course:

CMP186 - Tools and Environments for Software Development

University:

HUTECH International Institute of Technology

Student / GitHub Account:

Tan Phat - `Kise75`

Submission Items:

Source code, report, slide

Submission Deadline:

Saturday, April 4, 2026

\newpage

## Abstract

This report presents the final project for the course "Tools and Environments for Software Development". The selected topic is an RSS Feed Reader web application developed with Java and Spring technologies. The project demonstrates both software functionality and practical source code management using Git and GitHub. The assignment required students to download or obtain a project source code, create a Git or GitHub account, upload and manage the source code on the repository platform, write a report of at least thirty pages, and prepare presentation slides based on the report contents.

The chosen project is an RSS Feed Reader that aggregates content from multiple websites through RSS feeds. The system allows users to create an account, log in, subscribe to RSS channels, retrieve the latest articles, and manage personal feed subscriptions. The original downloadable source code referenced in a project list was no longer available, so a replacement source with a clear MIT license was selected from GitHub. That source was then imported into a new repository, improved, documented, built successfully, and published through a public GitHub repository.

This report does not only describe the imported project. It also explains the improvements that were added during the final project process. These improvements include homepage statistics, article search capability, manual feed refresh, duplicate feed validation, safer deletion operations, account summary enhancements, and compatibility updates for building the project on a modern Java environment. As a result, the final repository contains a project that is more functional, more demonstrable, and more suitable for academic evaluation than the original imported version.

In addition, the report explains the role of Git and GitHub as core tools in modern software development. Git provides local version control through staging, commits, branches, and history, while GitHub provides remote repository hosting, synchronization, collaboration support, and transparent submission evidence. Applying these tools in the final project helps demonstrate an important learning outcome of the course: software development is not only about writing code, but also about organizing, documenting, improving, and managing that code professionally.

The report is divided into four main chapters exactly as required by the lecturer. Chapter 1 introduces the project topic, objectives, architecture, technologies, features, and improvements. Chapter 2 introduces Git and GitHub, including their concepts, workflows, and significance in team-based development. Chapter 3 explains how Git and GitHub were applied to this specific RSS Feed Reader project from source acquisition to repository publication and enhancement tracking. Chapter 4 concludes the project and discusses achievements, limitations, future work, and lessons learned.

\newpage

## Table of Contents

1. Chapter 1: Introduction About the Project  
1.1 Background of RSS technology  
1.2 Problem statement  
1.3 Project objectives  
1.4 Scope of the project  
1.5 Functional requirements  
1.6 Non-functional requirements  
1.7 System architecture  
1.8 Technology stack  
1.9 Main modules and pages  
1.10 Database and entities  
1.11 Improvements added in this project  
1.12 Build and execution summary  

2. Chapter 2: Introduction to Git and GitHub  
2.1 Version control in software engineering  
2.2 What is Git  
2.3 Core Git concepts  
2.4 Common Git commands  
2.5 What is GitHub  
2.6 GitHub features for project management  
2.7 Git workflow and collaboration  
2.8 Best practices for academic projects  

3. Chapter 3: Applying Git and GitHub to manage the source code of the project  
3.1 Requirement analysis from the lecturer  
3.2 Selecting and importing the source code  
3.3 Creating the repository  
3.4 Initial commits and repository organization  
3.5 Implemented improvements and tracked changes  
3.6 Public repository publication  
3.7 Build verification and submission readiness  
3.8 Why Git and GitHub are valuable in this project  

4. Chapter 4: Conclusion and discussion  
4.1 Achievements  
4.2 Strengths of the project  
4.3 Limitations  
4.4 Future development directions  
4.5 Lessons learned  

References  
Appendix A: Repository structure  
Appendix B: Main Git commands used  
Appendix C: Important files changed  
Appendix D: Build and run instructions  
Appendix E: Git and GitHub glossary for the project  
Appendix F: Improvement rationale and presentation notes  

\newpage

# CHAPTER 1: INTRODUCTION ABOUT THE PROJECT

## 1.1 Background of RSS Technology

RSS stands for Really Simple Syndication or Rich Site Summary, depending on the historical naming convention used in different contexts. In practice, RSS is an XML-based format that allows websites to publish updates in a structured way so that users or other systems can subscribe to content automatically. A website may publish headlines, summaries, publication dates, and article links in an RSS feed. A feed reader or aggregator can periodically retrieve that information and present the newest updates to readers in one place.

Before the widespread adoption of social media recommendation systems, RSS was one of the most important technologies for following website updates efficiently. Even today, RSS remains relevant because it is an open, standardized, and platform-independent way to consume information. RSS gives users control over what they subscribe to. It also avoids algorithmic filtering because the content is directly collected from the source sites selected by the user.

From a software engineering perspective, an RSS Reader project is useful for educational purposes because it combines multiple practical topics. It requires working with external data sources, network retrieval, structured XML parsing, database persistence, user management, and presentation of retrieved content in a friendly interface. It can also be extended easily with additional features such as searching, filtering, validation, statistics, scheduling, and security improvements.

This makes the RSS Reader topic very suitable for a final project in a course related to tools, environments, and software development workflow. It is not only a content-driven website, but also a system that demonstrates how a software project can be managed through version control and repository hosting tools.

## 1.2 Problem Statement

Many websites publish information continuously throughout the day. Users who want to follow updates from many sites often face the same difficulty: they must repeatedly visit different pages, check whether new content has been published, and manually compare old and new information. This process is inefficient and time-consuming. It also becomes increasingly difficult as the number of followed websites grows.

An RSS Reader addresses this problem by collecting updates from many sources and presenting them in a centralized interface. Instead of checking every website manually, the user subscribes to RSS channels and reads all newly aggregated content in one system. Therefore, the essential problem addressed by this project is the delay and inconvenience between content publication on source websites and content discovery by end users.

From a system perspective, the problem has two dimensions. The first dimension is data retrieval: the application must collect RSS feeds correctly and consistently. The second dimension is user usability: the application must present the retrieved content in a way that is manageable, searchable, and easy to refresh.

The imported source code already solved the basic form of this problem, but it also had limitations from the perspective of final project demonstration. It did not clearly show modern build compatibility, it did not support article search on the homepage, and some user actions could be improved in terms of safety and convenience. Therefore, the project described in this report focuses not only on using an RSS Reader source code, but also on adapting and improving it to become a more complete and presentable final project.

## 1.3 Project Objectives

The main objective of this project is to manage and improve an RSS Feed Reader application while using Git and GitHub as the official tools for source code management. This general objective can be divided into specific objectives as follows:

First, the project aims to provide a working web application that can aggregate RSS content from multiple channels. Users must be able to see recent news, create an account, log in, subscribe to feeds, and manage their subscriptions.

Second, the project aims to demonstrate the use of Git as a version control system. This includes repository initialization, staging changes, creating commits, tracking improvements, and preserving source code history.

Third, the project aims to demonstrate the use of GitHub as a public repository platform. The final source code must be uploaded, synchronized, and made accessible for evaluation by the lecturer.

Fourth, the project aims to improve the selected source code so that it is not only a raw imported project. The final result must show meaningful work done by the student. For that reason, several improvements were designed and implemented in the user interface, validation logic, and build configuration.

Fifth, the project aims to produce academic deliverables beyond the software itself. These deliverables include a detailed report, a NotebookLM source file for slide generation, and a presentation prompt aligned with the report contents.

## 1.4 Scope of the Project

The scope of the project includes source code acquisition, local setup, build verification, project improvement, repository publication, and documentation. The system operates as a web application in which registered users can manage personal RSS subscriptions and view retrieved feed entries. The project also includes administrator views for inspecting user accounts.

Within the software scope, the implemented features cover:

- homepage news display
- article search on the homepage
- account registration and login
- personal feed subscription management
- manual channel refresh
- channel deletion with safer request handling
- duplicate RSS URL prevention
- statistics display
- build compatibility updates for modern JDKs

The scope of this report also includes explanation of Git and GitHub concepts because the lecturer specifically required a chapter about those tools and another chapter about applying those tools to the project.

There are also some limitations to the project scope. The system does not implement advanced recommendation logic, category-based personalization, mobile app support, or external notification systems such as email or push alerts. The database used in the project is suitable for educational demonstration, but it is not designed as a large-scale production deployment. The user interface is functional and understandable, but it is still based on an older JSP and Bootstrap architecture rather than a modern frontend framework.

## 1.5 Functional Requirements

Functional requirements describe what the system should do. In this RSS Feed Reader project, the main functional requirements are:

1. The system shall allow new users to register an account.
2. The system shall allow registered users to log in securely.
3. The system shall display the latest RSS feed items on the homepage.
4. The system shall allow authenticated users to add new RSS channels to their account.
5. The system shall validate whether the newly submitted channel URL is a reachable RSS feed.
6. The system shall prevent the same user from adding the same RSS URL more than once.
7. The system shall allow users to refresh a subscribed channel manually.
8. The system shall allow users to remove a subscribed channel through a safer POST-based operation.
9. The system shall allow users to view the latest feed items for each subscribed channel in the account page.
10. The system shall allow users to search articles by title or description on the homepage.
11. The system shall display statistics such as total articles, total channels, and total users.
12. The system shall allow administrators to view and manage user records.

These functional requirements are consistent with the original project concept while also reflecting the new improvements added for the final submission.

## 1.6 Non-Functional Requirements

Non-functional requirements describe how the system should behave rather than which business functions it provides. In this project, the most important non-functional requirements are usability, reliability, maintainability, security, portability, and acceptable educational-level performance.

The application must be simple enough for classroom demonstration. Users should understand how to register, log in, add RSS channels, refresh channels, and search content without requiring long training. The project improves usability by adding clearer account summaries, success messages, and a straightforward homepage search form.

The application should avoid storing invalid feeds when possible. The added feed reachability validation improves reliability by checking whether a URL can be read as an RSS source before storing it permanently.

The project should remain easy to inspect and extend. The layered architecture with controllers, services, repositories, entities, and views supports maintainability. Git and GitHub further improve maintainability by keeping a history of changes and making documentation part of the same repository.

The application already uses Spring Security for authentication. This project further improves request safety by converting feed deletion from a GET request to a POST request and applying authorization-aware refresh handling.

The project should build on a modern environment. Because the imported source was originally built for an older Java setup, compatibility dependencies and plugin updates were added so the application can be packaged successfully on a newer JDK.

## 1.7 System Architecture

The system follows a multi-layered web architecture. This is a common pattern in Java enterprise and educational applications because it separates responsibilities and helps students understand the structure of a complete web system.

The presentation layer includes JSP files, Bootstrap styling, and client-side JavaScript. It is responsible for displaying content to users and collecting user input. In this project, the presentation layer contains the homepage, login page, registration page, contact page, account page, and administrative user pages.

Controllers receive HTTP requests, interact with services, and prepare model data for the views. For example, `HomeController` loads the latest or searched feed items and statistics for the homepage, while `UserController` manages the account page, adding channels, refreshing channels, and removing channels.

The service layer contains business logic such as retrieving RSS items, validating feeds, refreshing channels, saving users, and loading associated data. This layer is important because it keeps controllers small and focused on web concerns rather than business rules.

The repository layer uses Spring Data JPA. Repositories are responsible for database access. They provide methods for retrieving users, blogs, and feed entries, as well as custom queries such as finding recent items for a feed or searching entries by keyword.

The system also includes scheduled reloading of channels. This means feed refresh is not based only on manual user action. Instead, the application can periodically reload all channels in the background. Manual refresh was added in this project as a complementary improvement for usability and demonstration.

## 1.8 Technology Stack

The selected technology stack reflects a classic Java web application model. Even though some technologies are older, they remain educationally valuable because they clearly demonstrate key software engineering layers.

Java is the main programming language used for application logic, model classes, controllers, services, repositories, and RSS parsing support. Spring MVC handles request mapping, controller dispatching, model binding, and interaction between the web layer and business logic. Spring Security is used for authentication and authorization. Spring Data JPA simplifies repository development while Hibernate handles persistence under the JPA model.

JSP is used as the view technology. Apache Tiles helps structure page layouts so the application can reuse headers, footers, and templates consistently. Bootstrap supports layout and styling, while jQuery helps with form validation and simple interactions. Maven is used for dependency management and project packaging. The included database setup is suitable for a local educational environment and makes the project easier to run without complex infrastructure.

## 1.9 Main Modules and Pages

The homepage module displays the newest RSS items. In the improved version, it also displays a statistics dashboard and a search form. This page is useful for both guests and authenticated users because it provides an immediate view of the latest aggregated content.

The authentication module allows users to register and log in. This module provides identity management for the rest of the application because personal RSS channel subscriptions are tied to user accounts.

The account module is the core personal workspace of the system. It allows users to view subscribed channels, add a new channel, inspect recent items per channel, refresh a channel manually, and remove a channel safely. The improved version also displays personal statistics such as total subscribed channels and the count of recently loaded items.

The administration module allows an administrator to inspect user lists and user detail pages. This demonstrates role-based access patterns in the project.

## 1.10 Database and Entities

The main entities of the project are `UserEntity`, `UserRoleEntity`, `RssFeedEntity`, `RssFeedEntryEntity`, and `CountryEntity`. These entities model registered users, permissions, subscribed channels, retrieved feed items, and related profile data.

`RssFeedEntity` and `RssFeedEntryEntity` are especially important because together they represent the relationship between a subscribed source and the articles aggregated from that source. `UserEntity` is equally important because ownership of subscribed channels is tied to user accounts.

The entity design is sufficient for a final project because it models both user-level ownership and content-level storage. The relationships also support meaningful demonstrations of database mapping and layered service handling.

## 1.11 Improvements Added in This Project

The project now includes modern build compatibility, homepage search, homepage statistics, manual channel refresh, safer deletion, duplicate feed prevention, feed reachability validation, and better account summaries. These are not only cosmetic changes. They improve usability, safety, maintainability, and demonstration quality.

The most significant improvement from an environment perspective is the build compatibility update. The most visible UI improvements are the dashboard statistics and search interface. The most meaningful account-management improvements are manual refresh, duplicate URL prevention, and safer deletion.

## 1.12 Build and Execution Summary

The final project was built successfully with Maven after the compatibility fixes. This is an essential requirement because a final project should not only look correct in the repository but also be technically reproducible.

The verified build command used in the project environment is:

```bash
mvnw.cmd -DskipTests package
```

The successful build confirms that dependencies are resolved correctly, the source code is consistent, the packaging configuration is functional, and the project is in a demonstrable submission state.

\newpage

# CHAPTER 2: INTRODUCTION TO GIT AND GITHUB

## 2.1 Version Control in Software Engineering

Version control is one of the most important practices in modern software development. In simple terms, version control is the process of recording changes in source code over time so that developers can understand what changed, when it changed, why it changed, and how to revert or compare versions if needed.

Without version control, software development quickly becomes risky and disorganized. Files may be overwritten, changes may be lost, and multiple team members may create conflicting versions of the same file. Version control provides structure and traceability, which are especially important in academic projects where the submission should clearly show evidence of progress and contribution.

Version control is not only useful for large companies. It is also essential for students because it teaches disciplined software engineering habits. By using version control, students learn how to save meaningful milestones instead of random file copies, write descriptive commit messages, track bug fixes and improvements, collaborate more safely, and present evidence of work to lecturers.

Git is the version control system used in this project, and GitHub is the repository hosting platform used to publish and manage the remote copy of the project.

## 2.2 What Is Git

Git is a distributed version control system. "Distributed" means every local repository contains the full project history, not only the latest version. This makes Git fast, flexible, and reliable even when working offline.

Git was designed to support source code management efficiently. It tracks snapshots of files and directories over time. Each commit records a specific project state. Developers can compare states, restore previous versions, create branches, and merge changes.

Git is especially strong because it separates several stages of work:

- working directory
- staging area
- local repository

This staged workflow helps developers decide exactly which modifications belong in each commit.

For students, Git is valuable because it creates a visible development history. A lecturer can inspect the repository and see that the project was not submitted as a single final upload only. Instead, the repository can show gradual progress such as import, build fixes, feature improvements, documentation, and report additions.

## 2.3 Core Git Concepts

To understand Git properly, it is helpful to review its core concepts.

### Repository

A repository is the main Git project container. It includes both the source code files and the metadata describing the project history.

### Working Tree

The working tree is the current local set of files visible in the project folder. Developers edit files here before staging them.

### Staging Area

The staging area is an intermediate area where selected changes are prepared for the next commit. This allows better control over commit quality.

### Commit

A commit is a saved snapshot of the project. Good commits should group related changes together and use clear messages.

### Branch

A branch is an independent line of development. Branches are useful for parallel work, experiments, and feature development without disturbing the main version.

### Merge

Merging combines changes from one branch into another. This is common in team workflows.

### Remote

A remote is a reference to a repository stored elsewhere, often on GitHub. Developers use remotes to push local commits and pull remote updates.

### Clone

Cloning creates a local copy of a remote repository.

### Push and Pull

Push uploads local commits to the remote repository. Pull retrieves and integrates remote updates into the local repository.

These concepts are all relevant to the final project because the assignment explicitly requires students to upload project source code to Git or GitHub and manage the project through a repository workflow.

## 2.4 Common Git Commands

The following commands are among the most important commands in Git:

### `git init`

Creates a new Git repository in the current folder.

### `git status`

Shows the current status of the working tree and staging area.

### `git add`

Stages changes for the next commit.

### `git commit -m "message"`

Creates a commit with a message describing the change.

### `git log`

Shows commit history.

### `git diff`

Shows differences between versions or between working tree and staged files.

### `git branch`

Lists or creates branches.

### `git checkout` or `git switch`

Moves between branches or restores certain states, depending on usage.

### `git remote add origin <url>`

Adds a remote repository reference named `origin`.

### `git push -u origin main`

Pushes commits to the `main` branch on the remote repository and sets upstream tracking.

### `git pull`

Downloads and integrates changes from the remote repository.

In this final project, Git commands were used not just as academic examples but as real actions to prepare the project for publication and evaluation.

## 2.5 What Is GitHub

GitHub is a cloud-based platform for hosting Git repositories. It provides remote storage, a web interface, collaboration tools, issue tracking, pull requests, branch visibility, commit browsing, and repository sharing.

A Git repository can exist only locally, but GitHub makes it possible to publish that repository online. This is important in academic contexts because lecturers need a way to inspect student work outside the student’s local machine.

GitHub also functions as a documentation platform. A repository can include README files, reports, source code, images, PDFs, release notes, and documentation folders. This makes GitHub a convenient final project environment because all submission-related assets can be placed in a structured and transparent location.

## 2.6 GitHub Features for Project Management

Several GitHub features are especially useful in software development and in this final project.

### Repository Hosting

The most basic function of GitHub is hosting repositories so that code is available online and synchronized with the local Git history.

### Visibility Control

Repositories can be private or public. In this project, the repository was initially created as private for safety and later changed to public so the lecturer can access it directly. This is an example of a real project management decision.

### Commit History Browsing

GitHub allows anyone with access to inspect commits, compare changes, and understand the evolution of the project.

### README Presentation

The README acts as the front page of the repository. It explains the project, the source origin, and how the final version differs from the original imported source.

### Collaboration Possibility

Even if a repository is created by one student account, GitHub can support collaborators, branches, and shared work. This is aligned with the lecturer’s note about members uploading or working through Git/GitHub.

### Evidence of Work

From an academic perspective, GitHub creates visible evidence that the project has been organized, updated, and published correctly. This is much stronger than submitting a single compressed file without history.

## 2.7 Git Workflow and Collaboration

Git workflows can vary depending on team size and project complexity. In a simple student project, a practical workflow is:

1. create or obtain a project source
2. initialize or clone a Git repository
3. review the existing code
4. make improvements
5. stage relevant files
6. commit with meaningful messages
7. push to GitHub
8. continue documentation and final cleanup

In more advanced teams, developers also create feature branches, pull requests, and code review processes. Even if this final project was completed primarily through one account, the same workflow principles apply. GitHub remains the central place where the final, traceable, shareable version of the project is stored.

The presence of commit history is especially useful when discussing improvement work. For example, a sequence of commits can show initial source import, environment compatibility fixes, feature enhancements, documentation additions, and final repository preparation. This sequence tells a story of development and is one of the strongest arguments for using Git and GitHub in an academic final project.

## 2.8 Best Practices for Academic Projects

When students use Git and GitHub for coursework, some best practices should be followed.

Commit messages should describe what changed and why. Messages such as "fix", "update", or "final" are much less useful than messages like "Add Java 9+ compatibility for Maven build" or "Add homepage search and dashboard statistics".

The report source, slide prompt, improvement notes, and supporting files should all be placed in the repository so that the repository itself becomes the central project record.

The README should explain the project, the upstream source if imported, and how the final version differs from the original.

A project on GitHub should not only exist; it should also build successfully when possible. Build verification gives confidence that the repository is in a usable state.

If an external source is used, it is important to choose a source with a clear license and to document its origin. This was done in the current project by selecting an MIT-licensed upstream repository and documenting the source in the README.

In conclusion, Git and GitHub are not side topics for this project. They are central to how the final project is organized, improved, explained, and delivered.

\newpage

# CHAPTER 3: APPLYING GIT AND GITHUB TO MANAGE THE SOURCE CODE OF THE PROJECT

## 3.1 Requirement Analysis from the Lecturer

The lecturer’s instructions for the final project can be summarized into several required steps:

1. Download source code for the group topic.
2. Create a Git or GitHub account.
3. Upload the source code to a Git or GitHub account.
4. Write a report based on the project.
5. Prepare slides based on the report to present in class.

The lecturer also required a report with at least thirty pages and specified four chapters:

- Chapter 1: Introduction about the topic
- Chapter 2: Introduction to Git and GitHub
- Chapter 3: Applying Git and GitHub to manage the source code
- Chapter 4: Conclusion and discussion

Therefore, this final project was organized not only as software development but also as repository management and documentation work. Every step performed in the project can be mapped back to one of the lecturer’s instructions.

## 3.2 Selecting and Importing the Source Code

The project topic selected from the provided list was "RSS Feed Reader". The related project description explained a system that minimizes the delay between content publication and content appearance in an aggregator. However, when the referenced source location was checked, the original downloadable source was no longer available.

This created an important real-world software engineering scenario: sometimes the originally referenced dependency or source is unavailable, and the developer must find a reliable replacement source. Instead of stopping at that point, a replacement source was identified on GitHub:

`https://github.com/DanielMichalski/spring-web-rss-channels`

This replacement was suitable because:

- it matched the topic of an RSS Feed Reader
- it was a web application in Java
- it supported user accounts and feed subscriptions
- it had a clear MIT license
- it was structured well enough for improvement and documentation

The source code was cloned locally, imported into the working folder, and committed as the initial project state. This step corresponds directly to the lecturer’s first requirement: obtaining the source code for the selected project topic.

## 3.3 Creating the Repository

After importing the selected source code into the local workspace, a new Git repository was initialized in the project folder. This established the project under version control. Initial import files, source folders, Maven configuration, views, and resources were then staged and committed.

Later, a new GitHub repository was created under the account `Kise75`. The repository created for the project is:

`https://github.com/Kise75/rss-feed-reader-java`

At first, the repository was created as private to safely verify setup and push access. After confirming that the code had been uploaded successfully and after the user requested lecturer accessibility, the repository was prepared to be published as public for evaluation. This workflow reflects a normal real-world practice: establish the repository safely first, then expose it publicly when ready.

Creating a dedicated repository is an important step because it separates this final project from unrelated repositories and gives the project a clear submission identity.

## 3.4 Initial Commits and Repository Organization

A good repository should not contain only one giant final commit. Instead, it should show recognizable stages of development. The repository in this project was organized around a sequence of meaningful milestones.

The first major milestone was the import of the selected RSS Feed Reader source code. This commit preserved the original state of the imported code as a baseline.

The second major milestone was build compatibility adjustment. Because the project initially failed on a modern JDK, compatibility-related dependencies and plugin changes were introduced. This commit documented the technical adaptation needed to make the project usable in the current environment.

The third milestone was documentation of source origin and build updates in the README. This made the repository more transparent and academically credible.

Subsequent milestones included the actual application improvements:

- search functionality
- homepage statistics
- manual feed refresh
- safer deletion
- duplicate validation
- account summary improvement
- report and presentation support files

This commit-based organization is important because it demonstrates process. A lecturer inspecting the repository can understand that the project evolved through manageable steps instead of being uploaded as a single opaque result.

## 3.5 Connecting Local Git to GitHub

After the local repository was prepared, the remote origin was configured to point to the GitHub repository. The main branch was then pushed to GitHub. This step fulfilled the lecturer’s requirement of uploading the source code to Git/GitHub.

The core workflow can be summarized as:

```bash
git init
git add .
git commit -m "Import RSS Feed Reader source"
git branch -M main
git remote add origin https://github.com/Kise75/rss-feed-reader-java.git
git push -u origin main
```

After that initial publication, additional changes were committed locally and pushed again so the GitHub repository always represented the latest project state.

The value of this step is not only technical. It also provides submission evidence. The public GitHub repository becomes a traceable artifact that the lecturer can inspect directly on the web.

## 3.6 Implemented Improvements and Tracked Changes

One of the strongest parts of applying Git and GitHub is the ability to show exactly what changed in the project. In this final project, several substantial improvements were made, and each of them can be associated with specific code files and commit history.

### 3.6.1 Homepage Search

The homepage was improved so users can search RSS entries using a keyword. This required changes to the repository layer, the service layer, the controller layer, and the view layer. This improvement demonstrates how a relatively simple user feature can involve multiple layers of the application architecture. That makes it a good example to discuss in both the report and the presentation.

### 3.6.2 Homepage Statistics

Three dashboard cards were added to the homepage: total articles, total channels, and total users. This required the controller to collect counts from the service layer and pass them to the JSP. Although this is a small feature from a coding perspective, it significantly improves the demonstration quality of the project.

### 3.6.3 Manual Refresh

Originally, feed updates were primarily tied to scheduled reloading. The account page was improved to allow a manual refresh action on each channel. This is useful because it shows immediate cause-and-effect during a classroom demo. The user can click refresh and explain that the system is reloading a specific RSS feed without waiting for the scheduler.

This feature also provided a good opportunity to apply better authorization handling so users refresh only the feeds they are permitted to manage.

### 3.6.4 Safer Deletion

One notable improvement is the conversion of feed deletion from a GET request into a POST request. In web application design, destructive actions should not usually be triggered through ordinary links because links can be followed unintentionally, cached, or prefetched. Switching to POST and adding a confirmation message improves correctness and demonstrates awareness of software engineering best practices.

### 3.6.5 Duplicate URL Validation

If users add the same RSS URL repeatedly, the project becomes cluttered and less reliable. This issue was solved by adding duplicate checking on the account management flow. This is a practical data validation improvement that shows the student did more than superficial UI changes.

### 3.6.6 Feed Reachability Validation

In the original flow, an RSS channel could potentially be stored even if the feed was not actually readable. The improved version validates the URL by attempting to load the RSS feed before saving it. This makes the application more dependable and more polished from a user perspective.

### 3.6.7 Build Compatibility

A very important tracked change is the environment compatibility fix. This change is not just academic; it was necessary for the project to build successfully at all. Adding legacy compatibility dependencies and updating the packaging plugin transformed the imported source into a working submission artifact for a modern machine.

This improvement is especially relevant to the course because tools and environments are part of the project context. A project that builds only in an outdated environment is weaker than a project that has been adapted thoughtfully.

## 3.7 Public Repository Publication

The lecturer needs direct access to the source repository, so repository visibility matters. Once the repository content was ready and the user requested public access, the repository could be made public so the lecturer can enter the repository directly without authentication barriers.

Public visibility supports the following academic goals:

- easy inspection by the lecturer
- visible commit history
- accessible README and documentation
- direct access to source code and report files
- easy sharing in Google Classroom or presentation materials

At the same time, because the project origin was documented clearly and the upstream license was respected, publishing it publicly remains professionally responsible.

## 3.8 Documentation as Part of Source Management

Git and GitHub were applied not only to the application code. They were also applied to project documents. This is important because software engineering includes project communication and traceability, not only source files.

The repository now includes:

- README with source origin and build notes
- project improvement summary
- NotebookLM source file
- slide generation prompt
- detailed report source

By storing these materials in the same repository, the project becomes self-contained. Anyone inspecting the repository can understand not only the code, but also the reasoning, deliverables, and educational context around the code.

This approach also reflects good project management. If documentation is separated from the code in random folders or personal devices, it becomes harder to maintain. GitHub solves this by making the repository the single source of truth for the final project.

## 3.9 Build Verification and Submission Readiness

A final project repository should be checked before submission. In this project, build verification was performed using Maven after the compatibility updates were applied.

The result of the build verification demonstrates that:

- the project packages successfully
- the dependency configuration is valid
- the code changes did not break compilation
- the final repository state is stable enough for submission and presentation preparation

Submission readiness also includes the preparation of academic materials:

- report source in Markdown
- PDF report generation attempt
- NotebookLM source file
- NotebookLM slide prompt

Thus, the repository is not merely source storage. It is an organized submission package.

## 3.10 Why Git and GitHub Are Valuable in This Project

Applying Git and GitHub in this project is valuable for several reasons.

First, they make the development history visible. This is important in a final project because the lecturer can see real work, not just the end result.

Second, they protect the project from accidental loss. If the local machine has issues, the remote repository preserves the project.

Third, they enable structured improvement. Because each modification can be committed separately, the student can reason about the project in stages: import, fix, improve, document, publish.

Fourth, they improve communication. A public GitHub link is far easier to share than a compressed folder buried in a local machine.

Fifth, they connect directly to the course theme. Tools and environments are not abstract ideas in this project. They are embodied in the actual use of Git, GitHub, Maven, Java, and the local development environment.

In conclusion, Chapter 3 demonstrates that Git and GitHub were applied in a practical, traceable, and academically relevant way throughout the lifecycle of the RSS Feed Reader final project.

\newpage

# CHAPTER 4: CONCLUSION AND DISCUSSION

## 4.1 Achievements

This final project achieved the main requirements set by the lecturer. A suitable source code for the assigned topic was obtained, organized in a Git repository, published through GitHub, improved with additional features, and supported by written report materials and slide preparation resources.

From a technical point of view, the project now functions as a complete RSS Feed Reader web application with:

- account registration and login
- feed subscription management
- homepage article display
- search capability
- statistics dashboard
- manual refresh support
- safer deletion logic
- duplicate feed prevention
- build compatibility with a modern JDK

From a process point of view, the project also achieved important workflow goals:

- version control setup
- remote repository publication
- staged commits
- documentation integration
- public repository availability for evaluation

These combined achievements make the final result more meaningful than a simple upload of borrowed code.

## 4.2 Strengths of the Project

One major strength of the project is its clear educational relevance. It combines software development, version control, build tooling, and web application structure in one practical assignment.

Another strength is the layered design. Because controllers, services, repositories, entities, and views are separated, the project is relatively easy to study and explain. This makes it suitable for a class presentation because the architecture can be described clearly.

The project also has strong demonstrability. The lecturer can observe visible homepage features, account-based feed management, refresh and removal actions, search results, statistics, and public repository history. The added improvements strengthen this demonstrability even further.

Finally, the use of GitHub as a public repository increases transparency. The final work is not hidden in a private local folder. It is accessible, reviewable, and traceable.

## 4.3 Limitations

Although the project is suitable and improved, it still has limitations.

First, the frontend stack is based on older technologies such as JSP and older Bootstrap conventions. While this is fine for learning, modern production projects often use newer frontend approaches.

Second, the RSS parsing logic assumes specific feed formats and date parsing patterns. More advanced parsing support could make the system more robust for diverse sources.

Third, the project currently focuses on essential features rather than advanced product-level capabilities. It does not include recommendation engines, category tagging, full-text search indexing, analytics dashboards, notification systems, or modern deployment automation.

Fourth, the current project report relies on a replacement source because the original download link was unavailable. Although the replacement was chosen responsibly and documented clearly, it remains an adaptation rather than the exact original downloadable package from the project list.

Fifth, the project uses a repository-centered workflow but does not fully demonstrate collaborative branching or pull request review across multiple contributors. That would be a good direction if this were expanded into a larger team project.

## 4.4 Future Development Directions

If more time were available, several enhancements could be implemented.

The first direction is advanced search and filtering. The system could support filtering by date, channel, keyword combinations, and categories.

The second direction is bookmarking and favorites. Users could save important articles for later reading.

The third direction is category management. Feeds could be grouped by topic such as technology, business, sports, or education.

The fourth direction is notification features. The system could notify users when new items appear in selected channels.

The fifth direction is better feed parsing robustness. Support for more RSS and Atom variations would improve interoperability.

The sixth direction is a modern frontend. The project could be modernized with a newer frontend framework while preserving the backend logic.

The seventh direction is automated CI workflow. GitHub Actions or another CI platform could be added so that every push automatically runs a build or tests. This would be an excellent extension for a course about tools and environments.

## 4.5 Lessons Learned

Several important lessons were learned during this final project.

The first lesson is that software development often starts with imperfect conditions. In this case, the originally referenced source download was not available. A practical developer must know how to respond by finding an appropriate replacement, validating licensing, and documenting the adaptation clearly.

The second lesson is that build environments matter. A project that worked in the past may fail in a current environment. Understanding dependencies, plugins, and compatibility updates is a key part of real software work.

The third lesson is that small features can have meaningful impact. Improvements like search, statistics, and manual refresh may seem modest, but they significantly increase the quality of the demonstration and the clarity of the project.

The fourth lesson is that Git and GitHub are not optional extras. They are central tools for organizing software professionally. They make progress visible, protect work, and support academic evaluation.

The fifth lesson is that documentation should be treated as part of the project itself. Reports, README files, improvement notes, and slide preparation materials all contribute to the completeness of the final submission.

## 4.6 Final Conclusion

The RSS Feed Reader final project successfully demonstrates the intersection of application development and source code management. The project started from an imported Java RSS Reader source and evolved into a better organized, better validated, and better documented submission through the use of Git, GitHub, Maven, and structured improvement work.

The final public repository provides a central location for the application source code and the supporting project artifacts. The report explains the application topic, the role of Git and GitHub, the concrete improvement steps, and the final results. For these reasons, the project meets the lecturer’s requirements and also represents a practical example of how software engineering tools and environments support the full lifecycle of a development task.

\newpage

# REFERENCES

1. Git Documentation. Available at: https://git-scm.com/doc  
2. GitHub Documentation. Available at: https://docs.github.com/  
3. Spring Framework Documentation. Available at: https://spring.io/projects/spring-framework  
4. Hibernate ORM Documentation. Available at: https://hibernate.org/orm/documentation/  
5. Maven Documentation. Available at: https://maven.apache.org/guides/  
6. Upstream source used for the imported project: https://github.com/DanielMichalski/spring-web-rss-channels  
7. Final public repository for this project: https://github.com/Kise75/rss-feed-reader-java  

\newpage

# APPENDIX A: REPOSITORY STRUCTURE

The project repository is organized as follows:

```text
rss-feed-reader-java/
  .github/
  .mvn/
  docs/
    notebooklm-source.md
    notebooklm-slide-prompt.txt
    project-improvements.md
    report/
      final-project-report.md
  rss-core/
    src/main/java/...
  rss-web/
    src/main/java/...
    src/main/resources/...
    src/main/webapp/...
  LICENSE
  README.md
  pom.xml
  mvnw
  mvnw.cmd
```

This structure separates application logic, web interface, and documentation clearly. Such organization makes the project easier to review and easier to present.

\newpage

# APPENDIX B: MAIN GIT COMMANDS USED

The following commands summarize the main Git workflow used in the project:

```bash
git init
git status
git add .
git commit -m "Import RSS Feed Reader source"
git commit -m "Add Java 9+ compatibility for Maven build"
git commit -m "Document imported source origin and build updates"
git remote add origin https://github.com/Kise75/rss-feed-reader-java.git
git branch -M main
git push -u origin main
git log --oneline
```

These commands are central to Chapter 3 because they show exactly how Git and GitHub were applied in practice.

\newpage

# APPENDIX C: IMPORTANT FILES CHANGED

The following files are especially important in the final improved version:

### Build and compatibility

- `pom.xml`
- `rss-web/pom.xml`

### Homepage improvements

- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/HomeController.java`
- `rss-web/src/main/webapp/WEB-INF/views/index.jsp`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/IRssFeedItemService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/impl/RssFeedItemService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/repository/ItemRepository.java`

### Account improvements

- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/UserController.java`
- `rss-web/src/main/webapp/WEB-INF/views/my-account.jsp`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/IRssFeedService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/impl/RssFeedService.java`

### Localization

- `rss-web/src/main/resources/properties/messages_en.properties`
- `rss-web/src/main/resources/properties/messages_pl.properties`

### Project documentation

- `README.md`
- `docs/project-improvements.md`
- `docs/notebooklm-source.md`
- `docs/notebooklm-slide-prompt.txt`
- `docs/report/final-project-report.md`

\newpage

# APPENDIX D: BUILD AND RUN INSTRUCTIONS

## Build

Use the following command from the repository root:

```bash
mvnw.cmd -DskipTests package
```

## Run using Tomcat Maven Plugin

```bash
mvnw.cmd tomcat7:run-war -pl rss-web
```

Then open:

`http://localhost:8081/rss-web/`

## Default Demo Account

According to the project README, the default demo account is:

```text
login: admin
password: secret
```

## Demo Flow for Presentation

1. Open the homepage and show statistics cards.
2. Use the search box to search for a keyword in RSS articles.
3. Log in to the system.
4. Open the account page.
5. Show current subscribed channels.
6. Add a new RSS channel or explain validation rules.
7. Demonstrate manual refresh.
8. Demonstrate remove with confirmation.
9. Show the public GitHub repository and explain commit history.

This presentation flow aligns well with both the lecturer’s instructions and the slide preparation task.

\newpage

# APPENDIX E: GIT AND GITHUB GLOSSARY FOR THE PROJECT

This appendix provides a short glossary of terms that are useful during presentation and report discussion.

## Repository

A repository is the complete project container that stores files and Git history. In this final project, the repository contains application code, documentation, and report-related materials.

## Commit

A commit is a recorded snapshot of the project at a specific point in time. Commits allow the student to show progress and explain project milestones such as source import, compatibility fixes, and feature improvements.

## Branch

A branch is a line of development. Although the current project mainly uses the `main` branch, branches are important in larger workflows because they allow isolated feature work.

## Remote

A remote is a linked repository stored elsewhere, usually on a platform such as GitHub. The `origin` remote in this project points to the public GitHub repository.

## Push

A push uploads local commits to the remote repository. This is how local work becomes visible on GitHub.

## Pull

A pull retrieves and integrates remote changes. This is essential in collaborative projects where multiple members may update the same repository.

## Clone

Cloning copies a remote repository to the local machine. The imported upstream RSS Reader source was first obtained through a clone operation before being adapted into the final project repository.

## Working Tree

The working tree is the current visible version of the files in the local project directory. Any edits made before staging exist here.

## Staging Area

The staging area contains selected modifications that will become part of the next commit. This is useful for preparing clean, focused commits.

## README

The README is the primary front-page documentation file of a GitHub repository. In this project, the README documents the upstream origin and the build compatibility updates.

## Public Repository

A public repository can be viewed by anyone with the link. The lecturer requested easy access for evaluation, so a public repository is helpful for final review.

## License

A license states how source code can be used, modified, and redistributed. Choosing an upstream source with a clear license is important when adapting an external project.

## Issue Tracking

Although not deeply used in this project, issue tracking is one of GitHub’s important features for organizing tasks, bugs, and discussions in collaborative development.

## Pull Request

A pull request is a GitHub-based method for proposing and reviewing changes before merging them into another branch. It is especially useful in team projects.

## Fork

A fork is a copy of a repository under a different user or organization account. Forking is common in open-source work and can also be useful in student collaboration.

## Upstream

In this project, "upstream" refers to the original public source repository from which the RSS Reader project was imported before being adapted and improved.

\newpage

# APPENDIX F: IMPROVEMENT RATIONALE AND PRESENTATION NOTES

This appendix explains why each improvement was chosen and how the student can talk about it during presentation.

## F.1 Why Add Homepage Search

Search is one of the easiest features for a lecturer to understand immediately. It creates an obvious difference between the original imported project and the improved final project. During presentation, the student can say that an RSS Reader becomes more useful when readers can locate relevant news quickly instead of only reading the latest ten entries.

From a technical point of view, this feature also demonstrates layered programming. The search is not only a textbox in the UI. It required changes in:

- repository query methods
- service interfaces and implementations
- controller request handling
- JSP view logic

This makes search a strong improvement both functionally and academically.

## F.2 Why Add Statistics on the Homepage

Statistics make the homepage look more like a real dashboard. Without them, the page only shows article entries and does not summarize the system as a whole.

The three selected metrics were intentionally simple:

- total articles
- total channels
- total users

These metrics are enough to show database-driven dynamic data, while remaining easy to implement and explain. During presentation, the student can describe this improvement as a usability and visibility enhancement.

## F.3 Why Add Manual Refresh

Manual refresh is very useful in a classroom demo. Scheduled tasks are technically interesting, but they are hard to demonstrate because the lecturer cannot always see the scheduler working in real time. A refresh button solves that problem.

This improvement also aligns with real user expectations. If a user adds or manages a feed, they often want immediate control over retrieving recent content.

During presentation, the student can explain that the system now supports both automated background refresh and user-driven refresh, making the application more interactive.

## F.4 Why Convert Delete from GET to POST

This improvement may seem small, but it demonstrates software engineering awareness. GET requests are intended for retrieving resources, not for destructive actions. Deleting data through GET can be risky.

By converting deletion into a POST request and adding confirmation, the project becomes:

- safer
- more standards-aligned
- easier to justify as an improved version instead of a raw import

This is a strong talking point if the lecturer asks whether the improvements are only visual or also technical.

## F.5 Why Add Duplicate RSS URL Validation

Duplicate feeds reduce usability and can clutter the account page. Preventing duplicates improves data quality and user experience.

This feature is also easy to demonstrate. The presenter can explain that the system now protects users from adding the same source repeatedly, which shows better validation logic.

## F.6 Why Add Feed Reachability Validation

Allowing users to save invalid or unreadable feeds leads to confusion and a poor experience. Reachability validation means the application checks the RSS source before storing it permanently.

This improvement is especially valuable because it connects user-facing quality with backend validation. It is not just a UI message; it reflects a design choice to reject bad input earlier in the workflow.

## F.7 Why Add Modern Build Compatibility

This improvement is highly relevant to the course theme. A software project is not useful if it cannot build in the current development environment. Modernizing the Maven and dependency setup shows that the student understood the practical importance of environment management.

This is also one of the strongest arguments for the "Tools and Environments" course context. The student can say that the project work included not only application features, but also environment adaptation and build reproducibility.

## F.8 How to Explain the Public GitHub Repository

If the lecturer asks why the project was made public, the best explanation is:

- the lecturer needs direct access for evaluation
- public visibility makes code and history easy to inspect
- the repository acts as proof of project progress
- GitHub is part of the course learning outcome

The student can also mention that the repository was initially kept private for setup safety and then made public when ready for review. That sounds realistic and professional.

## F.9 Suggested Speaking Flow for the Student

When presenting the project, the student can use the following speaking flow:

1. Introduce the topic and explain what an RSS Reader is.
2. Explain why Git and GitHub are important for managing project source code.
3. Describe how the original source download was unavailable and how a licensed replacement source was selected.
4. Explain the major improvements added to the project.
5. Show the public GitHub repository as the final code management result.
6. Conclude with lessons learned about software tools, environments, and documentation.

## F.10 Suggested Answers to Lecturer Questions

### Question: Why did you not use the original download link from the PDF?

Suggested answer: The original project page still existed, but the downloadable source link was no longer available. To continue the assignment responsibly, I selected a replacement RSS Reader source from GitHub with a clear MIT license and documented the source clearly in the repository.

### Question: What exactly did you improve in the project?

Suggested answer: I added homepage search, homepage statistics, manual channel refresh, duplicate feed prevention, safer POST-based deletion, better account summaries, and modern JDK/Maven compatibility updates. These changes are visible in both the code and the public GitHub history.

### Question: Why is GitHub important here?

Suggested answer: GitHub stores the source code publicly for evaluation, preserves the full change history, and shows that the project was managed professionally instead of being submitted as a single final folder.

### Question: What did you learn from this project?

Suggested answer: I learned how to adapt an existing source code project, how to improve it meaningfully, how to fix build environment issues, and how to manage the full development workflow using Git and GitHub.
