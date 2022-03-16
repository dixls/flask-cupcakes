"""Flask app for Cupcakes"""

from flask import Flask, jsonify, render_template, request
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


@app.route("/api/cupcakes")
def all_cupcakes():
    """return list of all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def cupcake_details(cupcake_id):
    """return information about one specific cupcake by id"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def add_cupcake():
    """adds a new cupcake to cupcakes table"""

    flavor = request.json.get("flavor")
    size = request.json.get("size")
    rating = request.json.get("rating")
    image = request.json.get("image")

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def edit_cupcake(cupcake_id):
    """edit an existing cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """delete a cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message=f"deleted {cupcake.flavor} cupcake")


@app.route("/")
def home_page():
    """display home page"""

    form = AddCupcakeForm()

    return render_template("index.html", form=form)