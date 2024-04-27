#!/usr/bin/python3

"""
Order Model
"""

from flask import jsonify, abort, request, make_response
from app.views import app_views
from app import db
from ..models.order import Order
# # from flask_jwt_extended import jwt_required


@app_views.route("/orders")
@app_views.route("/orders/<order_id>")
# @jwt_required()
def get_post_order(order_id=None):
    """get a list of all orders in storage or"""

    if order_id is None:
        return make_response(jsonify([
            order.to_dict() for order in storage.all(Order).values()
        ]))

    order = storage.get(Order, order_id)
    if order is None:
        abort(404)
    return make_response(jsonify(order.to_dict()), 200)


@app_views.route("/orders/<order_id>/measurements")
def get_order_measurements(order_id=None):
    """get a list of all measurement for this order"""
    order = storage.get(Order, order_id)
    if order is None:
        abort(404)

    return jsonify(order.measurements)
