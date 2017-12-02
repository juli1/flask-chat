from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, MessageForm
from .models import User, Message


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = MessageForm()

    # Handle the case when we send a message
    if form.validate_on_submit():
        flash("Posting message")
        # Adding the message to the database
        m = Message(content=form.message.data, author=g.user)
        db.session.add(m)
        db.session.commit()
        # We redirect, we do not render the template. Otherwise
        # the form will be filled again.
        return redirect("/index")

    # Take only the last 20 messages
    msgs = Message.query.limit(20)
    return render_template("index.html", messages=msgs,form=form)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user and g.user.is_authenticated:
        flash("You are already logged in")
        return redirect('/index')

    form = LoginForm()
    if form.validate_on_submit():

        users = User.query.filter(User.username == form.username.data)
        print ("query count {}".format(users.count()))
        if users.count() != 1:
            flash('User %s does not exist' %
                  (form.username.data))
            return render_template('login.html',
                                   title='Sign In',
                                   form=form)
        user = users.first()
        if user.password != form.password.data:
            flash('Invalid password for user %s' %
                  (form.username.data))
            return render_template('login.html',
                                   title='Sign In',
                                form=form)
        login_user(user)
        print("Password {}".format(user.password))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))