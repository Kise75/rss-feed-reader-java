# NotebookLM Source Pack

## Project Title

RSS Feed Reader Project Using Git and GitHub

## Course Context

- Course: CMP186 - Tools and Environments for Software Development
- Final project type: source code management, report writing, and presentation
- Submission items required by the lecturer:
  - source code on Git or GitHub
  - report
  - slide deck
- Required report structure:
  - Chapter 1: Introduction about the project
  - Chapter 2: Introduction to Git and GitHub
  - Chapter 3: Applying Git and GitHub to manage the source code of the project
  - Chapter 4: Conclusion and discussion
- Required report length: at least 30 pages
- Presentation date shown by the lecturer: Saturday, April 4, 2026

## Project Overview

This project is a Java-based web application that acts as an RSS Feed Reader. The purpose of the application is to collect RSS feeds from multiple websites, retrieve the latest news entries, store them in the system, and display them to users in a simple web interface. Instead of visiting many websites manually, a user can subscribe to RSS channels and read the newest articles from one place.

The project was imported into a GitHub repository because the original project link from an online project list was no longer downloadable. To keep the final project valid and presentable, the imported source code was organized inside a Git repository, improved, documented, built successfully, and published through GitHub.

The public repository used for source code management is:

`https://github.com/Kise75/rss-feed-reader-java`

## Original Source and Adaptation

The original downloadable link in the PDF project list pointed to a page about "RSS Feed Reader Java Project", but the download source was unavailable. A replacement source with a clear MIT license was selected:

- Upstream source: `https://github.com/DanielMichalski/spring-web-rss-channels`

This replacement was appropriate because it is still an RSS Reader project built with Java web technologies and includes the core concepts required for the assignment:

- RSS aggregation
- user accounts
- feed subscription management
- recent article display
- web-based interaction
- source code version management through Git/GitHub

## Core Objective of the Project

The core objective is to minimize the delay between the publication of content on source websites and the appearance of that content in the RSS reader. In practical terms, the system helps users:

- register an account
- log in securely
- add RSS channels
- refresh subscribed channels
- read the latest articles
- manage their own subscribed feeds

## Main Technologies

The application uses the following technologies:

- Java
- Spring MVC
- Spring Security
- Spring Data JPA
- Hibernate
- JSP
- Apache Tiles
- Bootstrap
- jQuery
- HSQLDB
- Maven

The application also uses scheduled refresh logic and XML/JAXB processing to parse RSS feeds.

## Architecture Summary

The application follows a layered architecture:

1. Presentation layer
   - JSP pages
   - Bootstrap styling
   - jQuery validation and interaction

2. Controller layer
   - Handles HTTP requests
   - Prepares data for views
   - Coordinates user actions such as add, remove, refresh, register, login

3. Service layer
   - Contains business logic
   - Retrieves and stores feeds and feed entries
   - Applies security rules and validation

4. Repository layer
   - Uses Spring Data JPA repositories
   - Communicates with the database

5. Data layer
   - Stores users, feed definitions, and feed entries

## Main Features of the Base Project

The imported project already had these core features:

- homepage that shows latest RSS articles
- user registration and login
- personal account page for managing feeds
- administrator user management pages
- scheduled feed reloading
- multilingual text resources

## Improvements Added in This Final Project

The imported project was not submitted unchanged. Several improvements were added so the lecturer can evaluate actual project work and not only the upload of an existing codebase.

### 1. Homepage Search Feature

A search bar was added to the homepage so users can search RSS articles by title or description. This improvement makes the application more useful because users can now locate related news items quickly instead of only browsing the newest entries.

### 2. Homepage Statistics Dashboard

Three statistics cards were added to the homepage:

- total articles
- total channels
- total users

These statistics make the homepage feel more like a real dashboard and help demonstrate database-driven dynamic content.

### 3. Manual Channel Refresh

The account page now allows users to refresh an RSS channel manually. This is useful because the original project depended mainly on scheduled updates. Manual refresh improves the user experience and allows better classroom demonstration.

### 4. Safer Delete Operation

Channel deletion was changed from a GET request to a POST request. This is a meaningful software engineering improvement because delete operations should not be exposed as plain links. A confirmation prompt was also added.

### 5. Duplicate URL Prevention

The system now prevents users from adding the same RSS feed URL multiple times in the same account. This improves data quality and avoids unnecessary duplication.

### 6. Feed Reachability Validation

When a user adds a new RSS channel, the system now attempts to load the feed first. If the URL does not provide a readable RSS feed, the channel is rejected and an error message is shown. This improves usability and makes the application behavior more reliable.

### 7. Account Summary Dashboard

The account page now shows quick summary information:

- number of subscribed channels
- number of loaded news items
- account owner

This supports a better demonstration of personalized data management.

### 8. Modern JDK/Maven Compatibility

The imported project was originally designed for an older Java environment. Compatibility updates were added so the project could build successfully on a modern JDK:

- JAXB and `javax.annotation` dependencies were added
- the Maven WAR plugin was upgraded
- Maven package build was verified successfully

## Git and GitHub Workflow Used

Git and GitHub were not only used as storage. They were used as the official project management environment for the final assignment.

The workflow included:

1. importing the selected source code into a local Git repository
2. creating a new GitHub repository
3. connecting the local repository to the GitHub remote
4. committing changes incrementally
5. pushing changes to the public repository
6. keeping the report and supporting documents inside the repository

This process demonstrates the practical use of version control in a real project context.

## Typical Git Steps in This Project

Typical Git commands used in the project workflow include:

```bash
git init
git add .
git commit -m "Import RSS Feed Reader source"
git commit -m "Add Java 9+ compatibility for Maven build"
git remote add origin https://github.com/Kise75/rss-feed-reader-java.git
git branch -M main
git push -u origin main
```

These commands are important because they show how Git was used to track imported code, implementation improvements, documentation changes, and final project delivery.

## Educational Value of the Project

This project is suitable for a final course in tools and environments because it demonstrates both software development and development workflow management.

Technical learning outcomes include:

- understanding RSS and XML-based content aggregation
- using Spring MVC for web application structure
- using repositories and services to separate application concerns
- handling authentication and authorization
- improving an existing codebase
- maintaining build compatibility

Workflow learning outcomes include:

- initializing and managing a Git repository
- using GitHub as a public source management platform
- documenting software improvements
- preparing report and slide artifacts from the same repository

## Suggested Slide Themes

If NotebookLM generates slides from this file, it should emphasize:

- the project problem and motivation
- architecture and technologies
- before-and-after improvements
- Git/GitHub workflow
- public repository as submission evidence
- conclusion and future work

## Suggested Screens or Visuals for Slides

Useful visuals to propose in the slide deck:

- architecture diagram with layers: view, controller, service, repository, database
- screenshot of the homepage dashboard
- screenshot of the account page with refresh/remove actions
- diagram of the Git workflow from local repo to GitHub
- summary slide listing all implemented improvements

## Key Talking Points for Presentation

When presenting the project in class, the student should explain:

1. why RSS readers are useful
2. what the project does at a functional level
3. which technologies are used and why
4. what changes were added beyond the imported source
5. how Git and GitHub were applied to manage the code professionally
6. what was learned from integrating source code, improving it, documenting it, and publishing it

## Concise Conclusion

This final project demonstrates more than just downloading source code. It shows the complete process of selecting a suitable project, adapting it for a current environment, improving it with additional features, managing it using Git and GitHub, and preparing academic artifacts such as a report and presentation. The final result is a public GitHub repository, a documented improvement history, and a project that is much easier to explain and evaluate in class.
