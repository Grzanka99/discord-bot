from flask import Flask


def load_settings(app: Flask, settings_obj: object):
    app.config.from_object(settings_obj)


def create_app(settings_obj: object) -> Flask:
    app = Flask('DiscordBOT-API')

    load_settings(app, settings_obj)

    return app
