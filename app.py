# Import necessary libraries

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():

    date = request.form["date"]
    return render_template('index.html', date)


@app.route('/results', methods=['POST'])
def results():

    """
    data = request.get_json(force=True)
    predict =model.predict([np.array(list(data.values()))])
    output = predict[0]
    return jsonify(output)
    """



if __name__ == "__main__":
    app.run(debug=True)
