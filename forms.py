from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField
from wtforms.validators import InputRequired

class AddCupcakeForm(FlaskForm):
    """Form for adding new cupcakes"""

    flavor = StringField("Flavor", validators=[InputRequired()], render_kw={"placeholder": "Flavor"})
    size = StringField("Size", validators=[InputRequired()], render_kw={"placeholder": "Size"})
    rating = FloatField("Rating", validators=[InputRequired()], render_kw={"placeholder": "Rating"})
    image = URLField("Image URL", render_kw={"placeholder": "Image URL"})