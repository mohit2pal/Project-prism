# Libraries
import base64
# import json
from flask import Flask, request, jsonify
# import uvicorn
# from fastapi import FastAPI
import pickle

from scanner import sql_scanner

# Create the app
# app = FastAPI()
app = Flask(__name__)
# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)

# Index route, opens automatically on http://127.0.0.1:8000/
@app.route("/run", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.get_json()
        

if __name__ == '__main__':
    app.run(debug=True)