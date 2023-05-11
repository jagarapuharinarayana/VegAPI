
from flask import Flask, jsonify
from vegData import get_veg_data
app = Flask(__name__)

@app.route("/")
def Data():
    return jsonify(get_veg_data())

if __name__ == "__main__":
   from waitress import serve
   serve(app, host="127.0.0.1", port=8080)
