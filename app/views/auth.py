#!/usr/bin/env python3

"""Authentication views"""


from flask import (
    jsonify, request, abort,
    make_response, render_template,
    flash, redirect, url_for
)
from flask_login import current_user, login_user, logout_user
from app.views import app_views
from urllib.parse import urlsplit
from ..models.user import User
from app.forms import RegisterationForm, LoginForm
from app.constants import (
    ADMIN_NAV_LINKS,
    USER_NAV_LINKS
)
from app import db
from app.email import send_mail


@app_views.route("/login", methods=["POST", "GET"])
def login():
    """handle user login authentication"""
    if current_user.is_authenticated:
        return redirect(url_for('app_views.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user is None:
            user = User.query.filter_by(username=form.email.data).one_or_none()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', "error")
            return redirect(url_for('app_views.login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("app_views.home")
        flash('Logged in successfully')
        return redirect(next_page)

    return render_template("forms/login.html",
                           form=form,
                           user_nav_links=USER_NAV_LINKS)


@app_views.route("/register", methods=["GET", "POST"])
def register():
    """create a new user
    """
    if current_user.is_authenticated:
        return redirect(url_for('app_views.home'))

    form = RegisterationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successfull")
        return redirect(url_for('app_views.login'))
    return render_template("/forms/register.html",
                           form=form,
                           user_nav_links=USER_NAV_LINKS)


@app_views.route("/logout")
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('app_views.home'))


