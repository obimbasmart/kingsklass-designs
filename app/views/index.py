#!/usr/bin/python3
"""index default view"""

from flask import jsonify, render_template
from app.views import app_views
from ..constants import (
    FOOTER_SUPPORT_LINKS,
    FOOTER_QUICK_LINKS,
    USER_NAV_LINKS,
    ADMIN_NAV_LINKS
)


@app_views.route("/")
def home():
    return render_template('pages/home.html',
                           support_links=FOOTER_SUPPORT_LINKS,
                           quick_links=FOOTER_QUICK_LINKS,
                           user_nav_links=USER_NAV_LINKS,
                           admin_nav_links=ADMIN_NAV_LINKS,
                           )


@app_views.route("/status")
def get_status():
    """get api status"""
    return jsonify({"status": "OK"})