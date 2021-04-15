from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap

# ML Packages
import os
import pickle
from sklearn import *
from collections import Counter

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    def make_dict():
        direc = "emails/"
        files = os.listdir(direc)
        emails = [direc + email for email in files]
        words = []
        pickle = len(emails)

        for email in emails:
            f = open(email)
            blob = f.read()
            words += blob.split(" ")
            pickle = pickle - 1

        for i in range(len(words)):
            if not words[i].isalpha():
                words[i] = ""

        dictionary = Counter(words)
        del dictionary[""]
        return dictionary.most_common(3000)

    # Saved machine learning model
    clf = pickle.load(open("text-classifier.mdl", "rb"))
    d = make_dict()

    if request.method == 'POST':
        inp = request.form['inp']
        # data_in = [[email]]
        features = []
        for word in d:
            features.append(inp.count(word[0]))
        res = clf.predict([features])
    return render_template('result.html', prediction = res)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__== '__main__':
    app.run(debug=True)
