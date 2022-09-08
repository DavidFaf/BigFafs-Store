import imp
from market import app
from flask import render_template
from market.models import Item


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_place():
    all_items = Item.query.all()
    return render_template('market_place.html', items=all_items)
