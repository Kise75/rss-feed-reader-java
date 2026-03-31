# Project Improvements

Repository: `https://github.com/Kise75/rss-feed-reader-java`

This document summarizes the main improvements added after importing the original RSS Reader source code.

## 1. Modern JDK Build Compatibility

- Added JAXB and `javax.annotation` dependencies in the root Maven configuration.
- Upgraded the WAR packaging plugin to a newer version compatible with modern JDKs.
- Verified the project build with:

```bash
mvnw.cmd -DskipTests package
```

## 2. Homepage Search Feature

- Added a keyword search form on the homepage.
- Users can now search RSS articles by title or description.
- Search results are displayed using the same latest-news layout.

Files updated:

- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/HomeController.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/IRssFeedItemService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/impl/RssFeedItemService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/repository/ItemRepository.java`
- `rss-web/src/main/webapp/WEB-INF/views/index.jsp`

## 3. Homepage Statistics Dashboard

- Added three dashboard cards on the homepage:
  - total RSS articles
  - total channels
  - total users
- This gives the project a more complete portal/dashboard feel.

Files updated:

- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/HomeController.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/IRssFeedService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/impl/RssFeedService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/IUserService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/impl/UserService.java`
- `rss-web/src/main/webapp/WEB-INF/views/index.jsp`

## 4. Manual Refresh for RSS Channels

- Added a dedicated refresh action in the account page for each subscribed feed.
- Users can refresh a single channel immediately without waiting for the scheduled background task.

Files updated:

- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/UserController.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/IRssFeedService.java`
- `rss-core/src/main/java/com/danielmichalski/rss/core/service/impl/RssFeedService.java`
- `rss-web/src/main/webapp/WEB-INF/views/my-account.jsp`

## 5. Safer Delete Operation

- Changed channel removal from a direct GET request to a POST request.
- Added a confirmation dialog before channel removal.
- This is a security and usability improvement because destructive operations should not be done through plain GET links.

Files updated:

- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/UserController.java`
- `rss-web/src/main/webapp/WEB-INF/views/my-account.jsp`

## 6. Duplicate Feed Validation

- Added validation to prevent a user from adding the same RSS URL multiple times.
- If the submitted feed URL already exists in the account, the system now shows a validation error instead of storing duplicated data.

Files updated:

- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/UserController.java`
- `rss-web/src/main/resources/properties/messages_en.properties`
- `rss-web/src/main/resources/properties/messages_pl.properties`

## 7. Feed Reachability Validation

- Improved the channel creation flow so that the system checks whether the provided RSS URL can actually be loaded.
- If the URL is unreachable or not a valid RSS feed, the user receives an error message and the invalid channel is not stored.

Files updated:

- `rss-core/src/main/java/com/danielmichalski/rss/core/service/impl/RssFeedService.java`
- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/UserController.java`

## 8. Improved Account Dashboard

- Added account summary boxes that show:
  - number of subscribed channels
  - number of latest loaded items
  - account owner
- Added success feedback messages after add, refresh, and remove actions.

Files updated:

- `rss-web/src/main/java/com/danielmichalski/rss/web/controller/UserController.java`
- `rss-web/src/main/webapp/WEB-INF/views/my-account.jsp`

## 9. Localization Updates

- Added new UI text for the new features in both English and Polish message files.
- This keeps the project consistent with its original multilingual design.

Files updated:

- `rss-web/src/main/resources/properties/messages_en.properties`
- `rss-web/src/main/resources/properties/messages_pl.properties`

## Summary

The project is no longer just an imported source code sample. It now contains:

- visible UI improvements
- safer request handling
- stronger validation
- manual refresh support
- searchable content
- clearer dashboard statistics
- successful build support on a modern Java environment

These improvements make the project easier to demonstrate, easier to explain in the report, and more suitable for final project evaluation.
