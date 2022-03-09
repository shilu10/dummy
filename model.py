from resources import SpamDetection
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home() :
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit() :
    if request.method == 'POST' :
        message = request.form['message']
        spam_detection = SpamDetection()
        print(message)
        result = spam_detection.prediction(message)
        return render_template('result.html', result=result)
    else :
        return render_template('home.html')

app.run(debug = True, port = 5001)
    



