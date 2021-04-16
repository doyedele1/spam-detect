# Web Packages
from flask import Flask, render_template, jsonify, request

# ML Packages
import os
import pickle
from sklearn import *
from collections import Counter

from model import make_dict

app = Flask(__name__)

# Saved machine learning model
clf = pickle.load(open("text-classifier.mdl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/about")
def about():
  return render_template("about.html")

@app.route('/predict', methods=['POST'])
def predict():
    # For rendering predicted result on the GUI
    d = make_dict()

    # if request.method == 'POST':
    inp = request.form['inp']
    # data_in = [[email]]
    features = []
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    return render_template('index.html', prediction = res)

if __name__== '__main__':
    app.run(debug=True)
