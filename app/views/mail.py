#!/usr/bin/env python3

"""mail views"""


from app.views import app_views
from app.email import send_password_reset_email
from app import mail, db
from flask import redirect, url_for, flash, render_template
from app.forms import ResetPasswordForm, ResetPasswordRequestForm
from flask_login import current_user
from app.models.user import User
from app.constants import (
    ADMIN_NAV_LINKS,
    USER_NAV_LINKS
)

@app_views.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('app_views.home'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('app_views.home'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('app_views.login'))
    return render_template('forms/reset_password.html', form=form,
                            user_nav_links=USER_NAV_LINKS)


@app_views.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('app_views.home'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user:
            send_password_reset_email(user)

        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('app_views.login'))
    return render_template('forms/reset_password_request.html',form=form,
                           user_nav_links=USER_NAV_LINKS)

