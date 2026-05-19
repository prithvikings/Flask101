from flask import Flask, request, session, redirect, url_for, Response

app=Flask(__name__)
app.secret_key='your_secret_key' # Set a secret key for session management if we dont set a secret key, flask will raise an error when we try to use sessions. The secret key is used to sign the session cookies, ensuring that they cannot be tampered with by clients. In a production environment, you should use a strong, random secret key and keep it secure.

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username=='admin' and password=='password':
            session['logged_in'], session['username'] = True, username
            return redirect(url_for('welcome'))
        else:
            return Response('Invalid credentials',status=401,mimetype='text/plain') #we are using mimetype to specify the content type of the response, in this case, plain text by default flask return text/html.
    return '''
    <h2>Login Page</h2>
    <form method="post">
        <input type="text" name="username" placeholder="Username"/>
        <input type="password" name="password" placeholder="Password"/>
        <input type="submit" value="Login"/>
    </form>
    '''    


@app.route('/welcome',methods=['GET'])
def welcome():
    if 'logged_in' in session and session['logged_in']:
        return '''
        <h2>Welcome Page</h2>
        <p>Welcome, {0}!</p>
        <a href="/logout">Logout</a>
        '''.format(session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/logout', methods=['GET'])
def logout():
    session.clear() # Clear the session to log the user out
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)