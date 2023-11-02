# Created By: Elie Bizimana
# Created On: August 1, 2023

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create Flask app
app = Flask(__name__)

# Create New Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)


# Create a New Table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()
        return render_template("index.html", books=all_books)


# Create CREAD Functionality

# ADD a Book
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=request.form["title"],
                            author=request.form["author"],
                            rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for('home'))
    return render_template("add.html")


# Edit A Book
@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    if request.method == "GET":
        with app.app_context():
            book = db.get_or_404(Book, book_id)
            return render_template("edit.html", book=book)
    else:
        with app.app_context():
            book = db.get_or_404(Book, book_id)
            book.rating = request.form["rate"]
            db.session.commit()
            return redirect(url_for('home'))


# Delete A Book
@app.route("/delete/<book_id>")
def delete(book_id):
    with app.app_context():
        book = db.get_or_404(Book, book_id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

