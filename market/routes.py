from crypt import methods
from market import app
from flask import render_template, redirect, url_for 
from market.models import Item
from market.forms import RegisterForm, LoginForm
from market.models import User
from market import db

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    all_items = Item.query.all()
    return render_template('market_place.html', items=all_items)


@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        create_user = User(username=form.username.data,
        email_address=form.email_address.data,
        password = form.password1.data,)
        db.session.add(create_user)
        db.session.commit()
        return redirect(url_for('market_page'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)