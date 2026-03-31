package com.danielmichalski.rss.core.service;

import java.util.List;

import com.danielmichalski.rss.core.entity.RssFeedEntryEntity;

/**
 * Author: Daniel
 */
public interface IRssFeedItemService {

    List<RssFeedEntryEntity> findAll();

    List<RssFeedEntryEntity> find10NewestEntries();

    List<RssFeedEntryEntity> searchNewestEntries(String keyword, int limit);

    long countAllEntries();

}
