from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import util
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('app.html')

@app.route("/get_location_names", methods=['GET'])
def get_location_names():
    response = jsonify({
        "locations":util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response

@app.route("/predict_home_price",  methods=['POST'])
def predict_home_price():
    region = int(request.form["region"])

    building_type = int(request.form["building_type"])
    level = int(request.form["level"])
    levels = int(request.form["levels"])
    rooms = int(request.form["rooms"])
    area = float(request.form["area"])
    kitchen_area = float(request.form["kitchen_area"])
    object_type = int(request.form["object_type"])
    
    response = jsonify({
        "estimated_price":util.get_estimated_price(region,
                                                   building_type,
                                                   level,
                                                   levels,
                                                   rooms,
                                                   area,
                                                   kitchen_area,
                                                   object_type)
    })
    
    return response
    

if __name__ == "__main__":
    print("Starting Python Flask server for Home Price Predictions...")
    util.load_saved_artifacts()
    app.run(host="127.0.0.1", port=5000)