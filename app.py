"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, redirect, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


def serialize(cupcake):
    """return a serialized version of cupcake info"""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image,
    }


@app.route("/api/cupcakes/")
def all_cupcakes():
    """return list of all cupcakes"""
    cupcakes = Cupcake.query.all()
    serialized = [serialize(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)
