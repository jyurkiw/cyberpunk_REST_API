import os

from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from CP2020_Discord_Bot_API.api.equipment import WeaponsRoller


def createApp(test_config=None):
    load_dotenv()
    dbName = os.getenv("DB_NAME")

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # create rollers
    weaponsRoller = weaponsRoller(dbName)

    @app.route("/weapons/categories")
    def getWeaponCategories():
        return jsonify(weaponsRoller.getWeaponCategories())

    return app
