from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route("/")
def func():
    return "Hello!"

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            c1 = (data["c1"])
            
            with open('test.pkl','rb') as file_handle:
                clf = pickle.load(file_handle)
            result = clf.predict(c1)
            
        except ValueError:
            return jsonify("Please enter a number.")
        return jsonify("The number is {}".format(result.tolist()))

if __name__ == '__main__':
    app.run(debug=True)
