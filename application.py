import os
from dotenv import load_dotenv
from flask import Flask, render_template
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

CONNECTION_STRING = os.environ.get("COSMOS_CONNECTION_STRING")

# Create a new client and connect to the server
client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    message = "Connected to MongoDB successfully!"
except Exception as e:
    print(e)
    message = f"Failed to connect to MongoDB: {e}"


@app.route("/")
def index():
    return render_template("base.html", message=message)
