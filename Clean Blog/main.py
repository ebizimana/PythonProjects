# Created by: Elie Bizimana
# Created on: July 28, 2023


from flask import Flask, render_template, request
from post import Post
import requests
import smtplib

OWN_EMAIL = "elieb7842@gmail.com"
OWN_PASSWORD = "pudnyw-9Vygzi-zywmys"
posts = requests.get("https://api.npoint.io/cb61ede0199eb6f13aab").json()
post_object = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_object.append(post_obj)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        return render_template("contact.html", msg=True)
    return render_template("contact.html", msg=False)


# @app.route("/form-entry", methods=["POST"])
# def receive_data():

@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    requested_post = None
    for one_post in post_object:
        if one_post.id == blog_id:
            requested_post = one_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject: New Message\n\n" \
                    f"Name: {name}\n Email: {email}\n Phone:{phone}" \
                    f"\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL,OWN_PASSWORD, email_message)


if __name__ == "__main__":
    app.run(debug=True)
