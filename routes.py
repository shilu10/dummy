from Application.models import SpamDetection
from flask import Flask, render_template, request
from Application import app

@app.route('/')
def home() :
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit() :
    if request.method == 'POST' :
        message = request.form['message']
        spam_detection = SpamDetection()
        result = spam_detection.prediction(message)

        return render_template('result.html', result=result)
        
    else :
        return render_template('home.html')


    



