from flask import Flask


def load_settings(app: Flask, settings_obj: object):
    app.config.from_object(settings_obj)


def load_extensions(app: Flask):
    from extensions import db, ma, cors

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)


def create_app(settings_obj: object) -> Flask:
    app = Flask('DiscordBOT-API')

    load_settings(app, settings_obj)
    load_extensions(app)

    return app
