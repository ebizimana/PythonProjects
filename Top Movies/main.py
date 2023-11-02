# Created By: Elie Bzimana
# Created On: August 4, 2023

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import requests

# Create APP
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

# Create a Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
db = SQLAlchemy()
db.init_app(app)


# Create DB Table
class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    image_url = db.Column(db.String(250), nullable=False)


# Create Form
class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    # year = IntegerField('Movie Released Year', validators=[DataRequired()])
    # description = StringField('Movie Description', validators=[DataRequired()])
    # rating = FloatField('Rate Movie', validators=[DataRequired()])
    # ranking = IntegerField('Rank the Movie', validators=[DataRequired()])
    # review = StringField('Movie Review', validators=[DataRequired()])
    # image_url = StringField('Movie Image URL', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Table))
        all_movies = result.scalars()
        return render_template("index.html", all_movies=all_movies)


# Add a Movie
@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
