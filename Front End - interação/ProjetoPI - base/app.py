from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
from Model.Series import Series
import requests
import json
from bs4 import BeautifulSoup

def findAllSeries():
    auth = ("couchdb", "couchdb")
    j = {
       "selector": {
          "_id": {
             "$gt": None
          }
       }
    }
    r = requests.post("http://localhost:5984/series/_find", json=json.loads(str(j).replace("None", "null").replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    response = list()
    return j2["docs"]

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
cors = CORS(app)

@app.route('/')
def index():
    data = findAllSeries()
    return render_template('index.html', data=data)

@app.route('/search/title/<title>')
@cross_origin()
def searchTitle(title):
    auth = ("couchdb", "couchdb")
    j = {
        "selector": {
            "title_s": {
                "$regex": title.upper()
            }
        }
    }
    r = requests.post("http://localhost:5984/series/_find",
                      json=json.loads(str(j).replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    series = list()
    for j in j2['docs']:
        series.append(json.loads(json.dumps(Series(j['title'], j['genre'], j['year'], j['notes']).__dict__)))
    print(r.status_code)
    return jsonify(series)

@app.route('/search/genre/<genre>')
@cross_origin()
def searchGenre(genre):
    auth = ("couchdb", "couchdb")
    j = {
        "selector": {
            "genre_s": {
                "$regex": genre.upper()
            }
        }
    }
    r = requests.post("http://localhost:5984/series/_find",
                      json=json.loads(str(j).replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    series = list()
    for j in j2['docs']:
        series.append(json.loads(json.dumps(Series(j['title'], j['genre'], j['year'], j['notes']).__dict__)))
    print(r.status_code)
    return jsonify(series)

@app.route('/search/year/<year>')
@cross_origin()
def searchYear(year):
    auth = ("couchdb", "couchdb")
    j = {
        "selector": {
            "year": {
                "$eq": int(year)
            }
        }
    }
    r = requests.post("http://localhost:5984/series/_find",
                      json=json.loads(str(j).replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    series = list()
    for j in j2['docs']:
        series.append(json.loads(json.dumps(Series(j['title'], j['genre'], j['year'], j['notes']).__dict__)))
    print(r.status_code)
    return jsonify(series)
@app.route('/search/notes/<notes>')
@cross_origin()
def searchNotes(notes):
    auth = ("couchdb", "couchdb")
    j = {
        "selector": {
            "notes": {
                "$eq": float(notes)
            }
        }
    }
    r = requests.post("http://localhost:5984/series/_find",
                      json=json.loads(str(j).replace("'", "\"")), auth=auth)
    j2 = json.loads(r.text)
    series = list()
    for j in j2['docs']:
        series.append(json.loads(json.dumps(Series(j['title'], j['genre'], j['year'], j['notes']).__dict__)))
    print(r.status_code)
    return jsonify(series)

app.run(debug=True)
