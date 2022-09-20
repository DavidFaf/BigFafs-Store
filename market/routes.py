from crypt import methods
from market import app
from flask import render_template, redirect, url_for , flash
from market.models import Item
from market.forms import RegisterForm, LoginForm
from market.models import User
from market import db
from flask_login import login_user, logout_user, login_required

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

        login_user(create_user)
        flash(f"Account created successfully, you are now logged in as {create_user.username}")

        return redirect(url_for('market_page'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login_page():

    form = LoginForm()

    attempted_user = User.query.filter_by(username=form.username.data).first()
    if form.validate_on_submit():
        if attempted_user and attempted_user.password_checker(
                            password_to_check= form.password.data):
            login_user(attempted_user)
            flash(f"Success!, you are logged in as {attempted_user.username}", category='success')
            return redirect(url_for('market_page'))
        else:
            flash(f"Username and passwords don't match, please try again", category='danger')
            pass


    return render_template('login.html', form=form)


@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart_page():
    return render_template('cart.html')

@app.route('/info')
def more_info():
    return render_template('info.html')



@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out", category='info')
    return redirect(url_for('home_page'))