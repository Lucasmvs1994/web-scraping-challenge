#Dependencies...

from flask import Flask, render_template
import scraper
from flask_pymongo import PyMongo

# Flask Setup

app = Flask(__name__)


# Setting up mongo connection

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)


@app.route("/")
def index():

    mars_db = mongo.db.mars.find_one()
    return render_template("index.html", mars_db=mars_db)

@app.route("/scrape")
def scraper():

    mars_db = scraper.scrapping_mars_db()
    mongo.db.mars.insert_one(mars_db)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run
