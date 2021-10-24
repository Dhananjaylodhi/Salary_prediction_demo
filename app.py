from flask import Flask, render_template, request
#import numpy as np
import model as mdl

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    output = 0
    if request.method == 'POST':
        experience = request.form['experience']
        test_score = request.form['test_score']
        interview_score = request.form['interview_score']
        list1 = []
        list1.append(int(experience))
        list1.append(int(test_score))
        list1.append(int(interview_score))
        output = mdl.predict_salary(list1)

    return render_template('index.html', salary = output)

'''
@app.route("/sub", methods = ['POST'])
def submit():
    if request.method == 'POST':
        experience = request.form['experience']
        test_score = request.form['test_score']
        interview_score = request.form['interview_score']
        list1 = []
        list1.append(int(experience))
        list1.append(int(test_score))
        list1.append(int(interview_score))

    return render_template('sub.html', name = list1)
    
'''

if __name__ == "__main__":
    app.run(debug=True)