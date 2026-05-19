from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return redirect(url_for('welcome', username=username, password=password))
    return render_template('login.html')


@app.route('/welcome', methods=['GET'])
def welcome():
    username = request.args.get('username')
    password = request.args.get('password')
    return render_template('welcome.html', username=username, password=password)

@app.route('/logout', methods=['GET'])
def logout():
    return redirect(url_for('login'))