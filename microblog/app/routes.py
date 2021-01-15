#routes are different URLs which the application implements
#handlers for these routes written as Python functions are called view functions

from app import app

#these two decorators translates to when a WEb browser requests, / or /index, the function will pass index(), which returns hello,... etc
@app.route('/')         #decorator (modifies the function that follows)
@app.route('/index')    #decorator
def index():
    user = {'username' : 'Miguel'}
    return ''' 
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''  



