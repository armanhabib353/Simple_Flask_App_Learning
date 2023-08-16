from flask import render_template

def index():
    return "Welcome to Home Page in View File"

def index_tem(name, marks):
    # marks = 80
    return render_template('index.html', name=name, marks=marks)

def index_for():
    data = {'python':46, 'flask':35,'Machine learning':88,'deep learnng':30}
    return render_template('index_for.html', data=data)