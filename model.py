import numpy as np
from flask import Flask, request, jsonify
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification

app = Flask(__name__)

X, y = make_classification(n_samples=100, n_features=5, random_state=42)
model = MLPClassifier(hidden_layer_sizes=(10, 5), max_iter=1000, random_state=42)
model.fit(X, y)

@app.route('/predict', methods=['GET'])
def predict():

    #data = request.json
    data = [0.3, 0.5, 0.2, 0.1, 0.4]

    if len(data) != 5:
        return jsonify({"error": "O vetor deve conter 5 elementos"}), 400


    input_data = np.array(data).reshape(1, -1)

 
    prediction = model.predict(input_data)

    return jsonify({"prediction": int(prediction[0])})

if __name__ == '__main__':

    app.run(port=8080)
