from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/swagger'
API_URL = '../static/data/swagger.json'

swagger_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)