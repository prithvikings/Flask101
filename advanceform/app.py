from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('thankyou.html', username=username, email=email, message=message)
    return render_template('feedback.html')