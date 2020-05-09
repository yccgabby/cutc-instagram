from app import bot
from flask import render_template

@bot.route('/')
@bot.route('/index')
def index():
    user = {'username': 'CUTC'}
    notifs = [
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