from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo


load_dotenv()

Mongo_URI=os.getenv('Mongo_URI')

client = pymongo.MongoClient(Mongo_URI)

db = client.AsgDB
collection = db['Asg-app']

app = Flask(__name__)

@app.route('/')

def home():

    day_of_week = datetime.today().strftime('%A')
    current_Time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day = day_of_week, time = current_Time)

@app.route('/submittodoitem', methods=["post"])
def submit():
    try:
        form_data = dict(request.form)
        collection.insert_one(form_data)

        return "data submitted successfully."

    except Exception as e:
         return render_template('index.html', error="Something went wrong.")

if __name__ == '__main__':
    app.run(debug=True)