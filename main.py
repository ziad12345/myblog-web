from flask import Flask, render_template, request
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/f4b1be8860bd21348c26").json()
print(posts)
author ="Me"
smth = "#2"
@app.route('/')
def home():
    return render_template("index.html", all_posts=posts, author=author, smth=smth)

@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/index.html')
def home_page():
    return render_template("index.html",all_posts=posts, author=author, smth=smth)


@app.route('/contact.html', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        choice = "yes"
        return render_template("contact.html", choice=choice)

    else:
        return render_template("contact.html")

@app.route('/1')
def here():
    num = 1
    return render_template("post.html",all_posts=posts, author=author, num=num)

@app.route('/2')
def id2():
    num = 2
    return render_template("post.html",all_posts=posts, num=num)
@app.route('/3')
def id3():
    num = 3
    return render_template("post.html",all_posts=posts, num=num)


if __name__ =="__main__":
    app.run(debug=True)