from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method=='POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return name


@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', name = username)

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result = result)



@app.route('/profile/<name>')
def profile(name):
    return 'This profile belongs to %s' %name

@app.route('/detail/<int:id>')
def detail(id):
    return 'This profile belongs to %d' %id

@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello guest %s' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
     return  redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/sucess/<name>')
def sucess(name):
    return 'Welcome %s' %name


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['nm']
        return redirect(url_for('sucess', name = username))
    else:
        username = request.args.get('nm')
        return redirect(url_for('sucess', name = username))


if __name__ == '__main__':
    app.run()




