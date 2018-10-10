# coding: utf-8

"""Flask Web Application for Jitenshea (Bicycle-sharing data)
"""

import daiquiri
import logging
import random

from flask import Flask, render_template, abort


daiquiri.setup(level=logging.INFO)
logger = daiquiri.getLogger("jitenshea-webapp")


app = Flask(__name__)
app.config['ERROR_404_HELP'] = False
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

CITIES = ['bordeaux', 'lyon']


def check_city(city):
    if city not in CITIES:
        abort(404, "City {} not found".format(city))

@app.route('/')
def index():
    cities = ['bordeaux', 'lyon']
    body_class = "body-index body-bg-{}".format(random.randint(1,3))
    return render_template("index.html", body_class=body_class, cities=cities)

@app.route('/doc/')
def swagger_ui():
    return render_template("swagger-ui.html")

@app.route("/<string:city>")
def city_view(city):
    check_city(city)
    return render_template('city.html', city=city)


@app.route("/<string:city>/<int:station_id>")
def station_view(city, station_id):
    check_city(city)
    return render_template('station.html', city=city, station_id=station_id)


@app.route("/<string:city>/cluster")
def clustering_view(city):
    check_city(city)
    return render_template("cluster.html", city=city)
