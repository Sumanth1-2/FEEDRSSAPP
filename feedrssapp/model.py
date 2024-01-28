# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:04:27 2024

@author: CB SUMANTH
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    summary = db.Column(db.Text)
    category = db.Column(db.String(50))
