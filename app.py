# Web Packages
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pickle
from model import make_dict

app = Flask(__name__)

@app.route('/')
def home():

    return "Hello World!"


@app.route('/api', methods=['POST'])
def predict():

    if clf:
        try:

            data = request.get_json()

            email_input = data['email']

            d = make_dict()

            features = []
            
            # inp = raw_input(">").split()

            for word in d:
                features.append(email_input.count(word[0]))
            
            prediction = clf.predict([features])

            if prediction == [0]:
                return "Not Spam"
            return "Spam"

            # print(type(prediction))

            return jsonify({'prediction': str(prediction)})
            # print res # Not Spam - [0], Spam - [1]
            # print(["Not Spam", "Spam!"][res[0]])
            # print(model.accuracy_score)

        except:

            return jsonify({'trace': traceback.format_exc()})

    else:
        print ('Train the model first')
        return ('No model here to use')
    

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input

    except:
        port = 12345 # If you don't provide any port the port will be set to 12345


    # Load machine learning model
    clf = pickle.load(open("text-classifier.mdl", "rb"))
    print('Model loaded')

    app.run(port=port, debug=True)