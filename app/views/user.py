#!/usr/bin/python3

"""
User routes
"""

from flask import request, render_template, flash, redirect
from flask_login import current_user, login_required
from app.views import app_views
from decimal import Decimal
from app import db
from app.constants import USER_NAV_LINKS, ADMIN_NAV_LINKS
from app.forms import EditProfileForm, InputMeasurementForm


@app_views.route("/user/me")
@login_required
def get_current_authenticated_user():
    user_info = current_user.get_public_info()
    return render_template("pages/profile.html",
                           user_info=user_info,
                           user_nav_links=USER_NAV_LINKS,
                           admin_nav_links=ADMIN_NAV_LINKS)


@app_views.route("/user/edit_profile", methods=["POST", "GET"])
def edit_user_profile():
    form = EditProfileForm()
    if request.method == "GET":
        return render_template("forms/edit_profile.html", form=form)

    if form.validate_on_submit():
        if form.username.data:
            current_user.username = form.username.data
        if form.first_name.data:
            current_user.first_name = form.first_name.data
        if form.last_name.data:
            current_user.last_name = form.last_name.data
        if form.phone.data:
            current_user.phone_no = form.phone.data
        db.session.commit()
        redirect("/user/me")
    return render_template("forms/edit_profile.html", form=form)


@app_views.route("/user/measurements", methods=["GET", "POST"])
def get_or_post_measurements():
    form = InputMeasurementForm()
    if form.validate_on_submit():
        new_measurements = {}
        for field_name, field in form.data.items():
            if isinstance(field, Decimal):
                new_measurements[field_name] = float(field)
        current_user.measurements = new_measurements
        db.session.commit()
        flash("Measurement updated")
    return render_template("forms/measurements.html", form=form)

