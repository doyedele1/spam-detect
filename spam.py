import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle

# Make a dictionary of the 3000 most common words
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

# Prepare the dataset using feature vectorization
def make_dataset(dictionary):
    direc = "emails/"
    files = os.listdir(direc)
    
    emails = [direc + email for email in files]
    feature_set = []
    labels = []
    pickle = len(emails)

    for email in emails:
        data = []
        f = open(email, errors="ignore")
        words = f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)
        
        if "ham" in email:
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        pickle = pickle - 1
    return feature_set, labels


d = make_dict()
features, labels = make_dataset(d)

# Percentages of training and test data
x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

# Train the model using a built-in classifier
clf = MultinomialNB()
clf.fit(x_train, y_train)

preds = clf.predict(x_test)
print(accuracy_score(y_test, preds))

# Save the model to disk
filename = 'text-classifier.mdl'
pickle.dump(clf, open(filename, 'wb'))

# Load the model from disk
clf = pickle.load(open(filename, 'rb'))