# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:03:36 2024

@author: CB SUMANTH
"""

import feedparser

def fetch_rss_feeds(feed_urls):
    articles = []

    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            article = {
                'title': entry.title,
                
                'category': 'Others'  # Default category
            }
            articles.append(article)

    return articles

# Example feed URLs
rss_feeds = ["http://rss.cnn.com/rss/cnn_topstories.rss",
"http://qz.com/feed",
"http://feeds.foxnews.com/foxnews/politics",
"http://feeds.reuters.com/reuters/businessNews",
"http://feeds.feedburner.com/NewshourWorld",
"https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

news_articles = fetch_rss_feeds(rss_feeds)
