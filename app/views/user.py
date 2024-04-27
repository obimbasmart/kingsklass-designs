#!/usr/bin/python3

"""
User routes
"""

from flask import request, render_template, flash, redirect
from flask_login import current_user, login_required
from app.views import app_views
from app import db
from app.constants import USER_NAV_LINKS, ADMIN_NAV_LINKS
from app.forms import EditProfileForm, InputMeasurementForm


@app_views.route("/user/me")
@login_required
def get_current_authenticated_user():
    user_info = current_user.get_public_info()
    print(user_info)
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
            current_user.phone = form.phone.data
        db.session.commit()
        redirect("/user/me")
    return render_template("forms/edit_profile.html", form=form)


@app_views.route("/user/measurements", methods=["GET", "POST"])
def get_or_post_measurements():
    form = InputMeasurementForm()
    return render_template("forms/measurements.html", form=form)

# @app_views.route("/users")
# @app_views.route("/users/<user_id>")
# # @jwt_required()
# def get_users(user_id=None):
#     """get a list of all users in storage or
#        get a specific user by ID
#     """

#     if user_id is None:
#         return make_response(jsonify([
#             user.to_dict() for user in storage.all(User).values()
#         ]))

#     user = storage.get(User, user_id)
#     if user is None:
#         abort(404)
#     return make_response(jsonify(user.to_dict()), 200)


# @app_views.route("/users/<user_id>/orders")
# @app_views.route("/users/<user_id>/orders/<order_id>")
# # @jwt_required()
# def get_user_orders(user_id=None, order_id=None):
#     """get a list of all orders made by a user
#        or get a specific order from a user
#     """
#     user = storage.get(User, user_id)
#     if user is None:
#         abort(404)

#     orders = storage.all(Order).values()

#     if order_id is None:
#         return make_response(jsonify([
#             order.to_dict() for order in orders
#             if order.user_id == user_id
#         ]), 200)

#     order = storage.get(Order, order_id)
#     if order is None or order.user_id != user.id:
#         abort(404)

#     return make_response(jsonify(order.to_dict()), 200)


# @app_views.route("/users/<user_id>/orders", methods=["POST"])
# # @jwt_required()
# def create_user_orders(user_id=None, order_id=None):
#     """create a new order for this user
#     """
#     user = storage.get(User, user_id)
#     if user is None:
#         abort(404)

#     order_data = request.get_json(silent=True)
#     if order_data is None:
#         abort(400, "Not a JSON")

#     if "product_id" not in order_data:
#         abort(400, "Missing product_id")
#     if "measurements" not in order_data:
#         abort(400, "Missing measurements")

#     new_order = Order(product_id=order_data['product_id'],
#                       user_id=user_id)

#     new_order.save()
#     order_measurements = order_data["measurements"]
#     for m in order_measurements:
#         new_order.measurements[m] = order_measurements[m]

#     new_order.save()
#     return make_response(jsonify(new_order.to_dict()), 200)


# @app_views.route("/users/<user_id>/measurements", methods=["GET",  "PUT"])
# # @jwt_required()
# def get_user_measurements(user_id=None):
#     """get measurments for this user"""
#     user = storage.get(User, user_id)
#     if user is None:
#         abort(404)

#     if request.method == "GET":
#         return jsonify(user.measurements)

#     data = request.get_json(silent=True)
#     if data is None:
#         abort(400, "Not a JSON")

#     measurements = data.get("measurements")
#     if measurements is None:
#         abort(400, "Missing measurements")

#     if not isinstance(measurements, dict):
#         abort(400, "Measurements data must be a dictionary of measurements")

#     for m in measurements:
#         user.measurements[m] = measurements[m]

#     user.save()
#     return (jsonify(user.measurements), 200)
