#!/usr/bin/python3

"""
Product views
"""

from app.views import app_views
from flask import render_template
from app.constants import USER_NAV_LINKS

@app_views.route("/products")
def get_products():
    products = DB.get(Products).all()
    return render_template("pages/products.html",
                           user_nav_links=USER_NAV_LINKS)