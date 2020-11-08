'''
create own personal website
first build simple app
'''

from flask import Flask, render_template

# create variable to store instance of flask app
app = Flask(__name__)

@app.route('/') # / means home page
# a sinple function that does something
def home():
    return render_template("home.html")


@app.route('/about') # / means home page
# a sinple function that does something
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug = True)
