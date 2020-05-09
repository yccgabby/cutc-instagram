from app import bot
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@bot.route('/')
@bot.route('/index')
def index():
    user = {'username': 'CUTC'}
    notifs = [ # hard-coded, need to integrate to InstaPy notification feed
        {
            'username': 'random_account',
            'message': 'liked your post'
        },
        {
            'username': 'random_account2',
            'message': 'followed you'
        }
    ]
    return render_template('index.html',title='Home Page',user=user,notifs=notifs)
@bot.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # gather data, run validators attached to fields, and if everything is all right it will return True
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)