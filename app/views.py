from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
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
        print("Password {}".format(user.password))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)