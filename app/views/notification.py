#!/usr/bin/python3

"""Product review routes
"""

from app.views import app_views
from flask import render_template
from flask_login import login_required

@app_views.route("/notifications")
@login_required
def get_notifications():
    return render_template("pages/notifications.html")
