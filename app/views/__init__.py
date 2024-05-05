#!/usr/bin/python3
"""initialize view module"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__)

from . import index
from . import product
from . import order
from . import user
# from . import category
from . import review
from . import static_views
from . import auth
from . import notification
from . import mail