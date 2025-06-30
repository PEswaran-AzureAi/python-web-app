from flask import Flask, render_template
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

uri = "mongodb+srv://parv08:g5RcqDbZugmLlN23@azurecluster01.u6onopw.mongodb.net/?retryWrites=true&w=majority&appName=AzureCluster01"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
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
