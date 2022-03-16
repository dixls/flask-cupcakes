from ctypes import sizeof
from logging.handlers import RotatingFileHandler
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField

class AddCupcakeForm(FlaskForm):
    """Form for adding new cupcakes"""

    flavor = StringField("Flavor")
    size = StringField("Size")
    rating = FloatField("Rating")
    image = URLField("Image URL")