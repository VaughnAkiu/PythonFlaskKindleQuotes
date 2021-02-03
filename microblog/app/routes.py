#routes are different URLs which the application implements
#handlers for these routes written as Python functions are called view functions
from flask import render_template
from app import app
from app.forms import LoginForm

#these two decorators translates to when a WEb browser requests, / or /index, the function will pass index(), which returns hello,... etc
@app.route('/')         #decorator (modifies the function that follows)
@app.route('/index')    #decorator
def index():
    user = {'username' : 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts) #takes template filename, variable list of template arguments, returns that template with placeholder now with actual values

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)



