import numpy as np
from flask import Flask, request, jsonify
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
import time
import joblib
import requests

from flask import Flask, jsonify

app = Flask(__name__)

model = joblib.load("mlp_20_10.joblib")

def data_acquisition():

    data_url = "http://192.168.1.103:30000/stats"

    try:
        response = requests.get(data_url)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

@app.route('/predict', methods=['GET'])
def predict():
    data = data_acquisition()



    throughput = data.get('throughput', None)
    percentage = data.get('percentage', None)
    print(percentage)

   
    try:
        throughput = float(throughput)
        percentage = float(percentage)
    except ValueError:
        return jsonify({"error": "Invalid data format"}), 400


    input_data = np.array([throughput, percentage]).reshape(1, -1)
    prediction = model.predict(input_data)
    prediction = prediction.tolist()
    if prediction[0] >= 2:
    	return [1]
    else:
    	return [0]



def main():
	predict();

	
if __name__ == '__main__':
    while True:
        app.run(host="0.0.0.0", port=8080, debug=False)
        #time.sleep(15)
