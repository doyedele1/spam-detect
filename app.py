# Web Packages 
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap

# ML Packages
import os
import pickle
from sklearn import *
from collections import Counter

# Initialize the app
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
            f = open(email, errors="ignore")
            blob = f.read()
            words += blob.split(" ")
            pickle = pickle - 1

        for i in range(len(words)):
            if not words[i].isalpha():
                words[i] = ""

        dictionary = Counter(words)
        del dictionary[""]
        return dictionary.most_common(3000)

# d = make_dict()
# features, labels = make_dataset(d)

# x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

# clf = MultinomialNB()
# clf.fit(x_train, y_train)

# preds = clf.predict(x_test)
    # Saved machine learning model
    clf = pickle.load(open('text-classifier.mdl', 'rb'), protocol=4)
    d = make_dict()

    # Receives input query from form
    if request.method == 'POST':
        comment = request.form['comment']
        features = []
        # inp = input(">").split()
        # if inp[0] == "exit":
        #     break
        for word in d:
            features.append(comment.count(word[0]))
        res = clf.predict([features])
        # print(["Not Spam", "Spam"][res[0]])
        # print(res)
    return render_template('result.html', prediction = res)
        
if __name__== '__main__':
    app.run(debug=True)