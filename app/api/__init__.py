# app/api/__init__.py
def mapped_api(app):
    from api.user_api import init_user_routes
    init_user_routes(app)
