from flask import Flask
from flask import request

from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_restplus import reqparse
from flask_restplus import inputs

import sqlite3
import pandas as pd
from pandas.io import sql
import simplejson as json
import numpy as np
from flask import Flask, Blueprint
from flask_restplus import Api, apidoc


from flask import Flask, Blueprint

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)
app.register_blueprint(blueprint)


student_model = api.model(
'Student',{
    'name':           fields.String,
    'age':            fields.String,
    'preTestScore':   fields.String,
    'postTestScore':  fields.String,
})

parser = reqparse.RequestParser()
parser.add_argument('order', choices=list(column for column in student_model.keys()))
parser.add_argument('ascending', type=inputs.boolean)

@api.route('/students')
class StudentsList(Resource):

    @api.expect(parser, validate=True)
    def get(self):
        # get books as JSON string
        args = parser.parse_args()

        # retrieve the query parameters
        order_by = args.get('order')
        ascending = args.get('ascending', True)

        if order_by:
            df.sort_values(by=order_by, inplace=True, ascending=ascending)

        json_str = df.to_json(orient='index')

        # convert the string JSON to a real JSON
        ds = json.loads(json_str)
        ret = []

        for idx in ds:
            student = ds[idx]
            student['zid'] = int(idx)
            ret.append(student)

        return ret

    @api.expect(student_model)
    def post(self):
        student = request.json


        row_num = df.shape[0]
        zid = row_num + 1

        # check if the given identifier does not exist
        if zid in df.index:
            return {"message": "A Student with Identifier={} is already in the dataset".format(zid)}, 400

        # Put the values into the dataframe
        for key in student:
            if key not in student_model.keys():
                # unexpected column
                return {"message": "Property {} is invalid".format(key)}, 400
            df.loc[zid, key] = student[key]

        df.append(student, ignore_index=True)
        df.to_csv("student.csv")
        return {"message": "Book {} is created".format(zid)}, 201

@api.route('/students/<string:id>')
class Students(Resource):
    def get(self,id):
        if (id in df.index):
            student = dict(df.loc[id])
            print("hahahahhahahahahahhahaha",student)
            student['zid'] = id
            return student
        else:
            api.abort(404, "Student {} doesn't exist".format(id))

    def delete(self,id):
        if (id in df.index):
            df.drop(id, inplace=True)
            df.to_csv("students.csv");
        else:
            api.abort(404,"Student {} doesn't exist".format(id))

    @api.expect(student_model)
    def put(self,id):
        if (id not in df.index):
            api.abort(404,"Student {} doesnt exist".format(id))

        student = request.json

        if 'zid' in student and id != student['zid']:
            return {"message": "zid cannot be changed".format(id)}, 400

        # Update the values
        for key in student:
            if key not in student_model.keys():
                # unexpected column
                return {"message": "Property {} is invalid".format(key)}, 400
            df.loc[id, key] = student[key]

        df.append(student, ignore_index=True)
        df.to_csv("student.csv")
        return {"message": "Student {} has been successfully updated".format(id)}, 200




if __name__ == '__main__':
    raw_data = {
        'zid': ['1','2','3','4','5'],
        'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'age': ['42', '52', '36', '24', '73'],
        'preTestScore': ['4', '24', '31', '50', '70'],
        'postTestScore': ['75', '46', '57', '62', '70']}

    df = pd.DataFrame(raw_data, columns = ['zid', 'name', 'age', 'preTestScore', 'postTestScore'])
    df = df.set_index('zid')
    app.run(debug=True)
