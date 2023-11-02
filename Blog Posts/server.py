# Created By: Elie B.
# Created Date: Feb 7, 2023
# Updated Date: Feb 15, 2023

from flask import Flask, render_template
import random
import datetime
import requests
from post import Post

app = Flask(__name__)

all_posts = requests.get(" https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route("/")
def home():
    return render_template("index.html", posts=post_objects)


@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    requested_post = None
    for one_post in post_objects:
        if one_post.id == blog_id:
            requested_post = one_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)


# Code for templates (practice)
# @app.route("/")
# def home():
#     year = datetime.date.today().year
#     print(year)
#     random_number = random.randint(1, 10)
#     return render_template("index.html", num=random_number, year=year)
#
#
# @app.route("/guess/<name>")
# def guess(name):
#     gender_response = requests.get(f"https://api.genderize.io?name={name}")
#     gender = gender_response.json()['gender']
#     age_response = requests.get(f"https://api.agify.io?name={name}")
#     age = age_response.json()['age']
#     return render_template("guess.html", name=name, gender=gender, age=age)
#
#
# @app.route("/blog")
# def blog():
#     blog_response = requests.get(" https://api.npoint.io/c790b4d5cab58020d391")
#     all_posts = blog_response.json()
#     return render_template("blog.html", posts=all_posts)


