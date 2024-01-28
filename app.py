# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:04:48 2024

@author: CB SUMANTH
"""

from flask import Flask, jsonify
from models import db, NewsArticle
from fetch_news import fetch_rss_feeds

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Fetch news and store in the database
rss_feeds = ["http://rss.cnn.com/rss/cnn_topstories.rss",
"http://qz.com/feed",
"http://feeds.foxnews.com/foxnews/politics",
"http://feeds.reuters.com/reuters/businessNews",
"http://feeds.feedburner.com/NewshourWorld",
"https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

news_articles = fetch_rss_feeds(rss_feeds)

with app.app_context():
    for article in news_articles:
        db.session.add(NewsArticle(title=article['title'], summary=article['summary'], category=article['category']))
    db.session.commit()

# Routes
@app.route('/news', methods=['GET'])
def get_news():
    articles = NewsArticle.query.all()
    news_data = [{'title': article.title, 'summary': article.summary, 'category': article.category} for article in articles]
    return jsonify(news_data)

if __name__ == '__main__':
    app.run(debug=True)
