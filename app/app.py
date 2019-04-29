from flask import Flask, render_template, redirect, url_for

application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
    return render_template('index.html')

@application.route('/goaway')
def goaway():
    return render('GO AWAY!')

def goaway2():
    return render_template('goaway.html')

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)
