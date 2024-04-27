#!/usr/bin/python3

"""Define Routes for serving html files to client"""

from flask import jsonify, abort, request, render_template
from app.views import app_views


@app_views.route("/sidebar")
def get_sidebar():
    return render_template("/modals/sidebar.jinja2")
