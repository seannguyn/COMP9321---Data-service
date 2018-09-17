from flask import Flask, request, Flask, Blueprint, redirect, url_for, render_template

from flask_restplus import Resource, Api, fields ,reqparse, inputs, apidoc
from pymongo import MongoClient
from flask_cors import CORS
import datetime
import json
import requests
from random import randint

# registering the api route, SETTING UP FLASK
app = Flask(__name__)
api = Api(app)
CORS(app)


# SETTING UP MLAB
# username: comp9321
# password: comp9321
MONGODB_URI = "mongodb://comp9321:comp9321@ds139124.mlab.com:39124/9321_asg2"

client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database("9321_asg2")

# SET UP MODEL for importing Indicators
indicator_import = api.model(
'Indicator',{
    'indicator_id':           fields.String,
})

@api.route('/indicators')
class IndicatorsList(Resource):
    def get(self):
        indicatorCollection = db['indicatorCollection']
        cursor = indicatorCollection.find({})

        indicatorList = []

        for document in cursor:
            obj = {}
            obj["location"]     = document['location']
            obj["collection_id"]= document['id']
            obj["creation_time"]= document['creation_time']
            obj["indicator"]    = document['indicator']

            indicatorList.append(obj)

        return indicatorList,200

    @api.expect(indicator_import)
    def post(self):
        data = request.json

        url = ('http://api.worldbank.org/v2/countries/all/indicators/'+data['indicator_id']+'?date=2012:2017&format=json&per_page=100')
        r = requests.get(url)
        data = json.loads(r.content.decode('ascii'))

        if (len(data)==1):
            return data[0], 400
        else:
            entries = []
            collection = {}

            for entry in data[1]:
                obj = {}
                obj['country']  = entry['country']['value']
                obj['date']     = entry['date']
                obj['value']    = 0 if entry['value'] == None else float(entry['value'])
                entries.append(obj)

            collection['id'] = data[1][0]['indicator']['id']
            collection['location'] = "/indicators/"+data[1][0]['indicator']['id']
            collection['indicator'] = data[1][0]['indicator']['id']
            collection['indicator_value'] = data[1][0]['indicator']['value']
            collection['creation_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            collection['entries'] = entries

            indicatorCollection = db['indicatorCollection']

            if ( indicatorCollection.find_one({"indicator": data[1][0]['indicator']['id']}) == None):
                indicatorCollection.insert_one(collection)

                return {
                    "location" : "/indicators/"+collection['id'],
                    "collection_id" : collection['id'],
                    "creation_time": collection['creation_time'],
                    "indicator" : collection['indicator']
                }, 201

            else:
                return {
                    "location" : "/indicators/"+collection['id'],
                    "collection_id" : collection['id'],
                    "creation_time": collection['creation_time'],
                    "indicator" : collection['indicator']
                }, 200

@api.route('/indicators/<string:id>')
class Indicators(Resource):
    def get(self,id):
        print("GET_ 1",id)

        indicatorCollection = db['indicatorCollection']
        document = indicatorCollection.find_one({"id": id})

        if ( document == None):

            return {
                "message" : "collection_id: "+ id +" does not exist",
                }, 400
        else:
            retDocument = {}
            retDocument['collection_id']    = document['id']
            retDocument['indicator']        = document['indicator']
            retDocument['indicator_value']  = document['indicator_value']
            retDocument['creation_time']    = document['creation_time']
            retDocument['entries']          = document['entries']

            return retDocument, 200

    def delete(self,id):
        print("DELETE_ 1",id)
        indicatorCollection = db['indicatorCollection']
        document = indicatorCollection.find_one({"id": id})

        if ( document == None):

            return {
                "message" : "collection_id: "+ id +" does not exist",
                }, 400
        else:
            myQuery = { "id": id }

            indicatorCollection.delete_one(myQuery)
            return {
                "message" :"Collection = "+ id +" is removed from the database!"
                }, 200

@api.route('/indicators/<string:id>/<int:year>/<string:country>')
class IndicatorYearCountry(Resource):
    def get(self,id,year,country):
        print("GET_ 1",id,year,country)

        # check if id is valid
        indicatorCollection = db['indicatorCollection']
        document = indicatorCollection.find_one({"id": id})

        if ( document == None):

            return {
                "message" : "collection_id: "+ id +" does not exist",
                }, 400

        # check if year is valid
        if (year < 2012 or year > 2017):
            return {
                "message" : "year need to br from 2012 to 2017",
                }, 400

        for x in document['entries']:
            if x['country'] == country:
                return {
                    "collection_id":    document['id'],
                    "indicator" :       document['id'],
                    "country" :         country,
                    "year" :            year,
                    "value":            x['value'],
                }, 200

        return {
            "message" : "country: "+country+" is invalid",
            }, 400


queryParser = api.parser()
queryParser.add_argument('query')

@api.route('/indicators/<string:id>/<int:year>')
@api.expect(queryParser)
class IndicatorYearCountrySort(Resource):
    def get(self,id,year):

        args = queryParser.parse_args()
        query = args.get('query')


        print("GET_ 1",id,year,query)

        # check if id is valid
        indicatorCollection = db['indicatorCollection']
        document = indicatorCollection.find_one({"id": id})

        if ( document == None):

            return {
                "message" : "collection_id: "+ id +" does not exist",
                }, 400

        # check if year is valid
        if (year < 2012 or year > 2017):
            return {
                "message" : "year need to br from 2012 to 2017",
                }, 400

        entries = []
        for x in document['entries']:
            if x['date'] == str(year):
                y = {}
                y['country'] = x['country']
                y['date'] = year
                y['value'] =  0 if x['value'] == None else float(x['value'])

                entries.append(y)

        sortedEntries = sorted(entries, key=lambda k: k['value'],  reverse=True)

        if query != None:
            if query.startswith('top') == True:
                query = int(query.replace("top", ""))

                return sortedEntries[0:query],200

            elif query.startswith('bottom') == True:
                query = int(query.replace("bottom", ""))

                return sortedEntries[-query:],200
        else:
            return sortedEntries,200



if __name__ == '__main__':

    app.run(debug=True)
