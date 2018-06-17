from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "reindert",
        date = datetime.utcnow()
    ))
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title="This is the user", user=User("Daniel", "Jezierski"))

@app.route("/add" , methods=["GET", "POST"])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('store url: ' + url)
        return redirect(url_for('index'))
    return render_template('add.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

class User:
    def __init__(self, firstname, secondname):
        self.firstname = firstname
        self.secondname = secondname

    def initials(self):
        return f"{self.firstname[0]}{self.secondname[0]}"

    def __str__(self):
        return self.__name__

if __name__ == "__main__":
    app.run(debug=True)
