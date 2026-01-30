# flask_app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = "replace-with-secret"

    # register routes
    
    # from interface.flask.routes import tugas_bp
    # from interface.flask.materi_routes import materi_bp
    from interface.flask.akademik_routes import akademik_bp

    # # app.register_blueprint(tugas_bp)
    # app.register_blueprint(materi_bp)
    app.register_blueprint(akademik_bp)

    return app
