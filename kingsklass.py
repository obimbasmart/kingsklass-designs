from app import app
from app.views import app_views
app.register_blueprint(app_views)
