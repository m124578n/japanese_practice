from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .dbs import db
from .practice import practice
from .timer import timer
from .app import app as ap


migrate = Migrate()


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    migrate.init_app(app, db)

    app.register_blueprint(practice.bp)
    app.register_blueprint(timer.bp)
    app.register_blueprint(ap.bp)

    with app.app_context():
        db.create_all()

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app
