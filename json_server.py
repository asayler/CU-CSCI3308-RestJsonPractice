#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Animal Farm Server

import flask
import farm

app = flask.Flask(__name__)

@app.route("/", methods=['GET'])
def get_animal_types():
    res = farm.list_animal_types()
    return flask.jsonify(res)

# Add more routes/functions here

if __name__ == "__main__":
    farm.setup()
    app.run(debug=True)
