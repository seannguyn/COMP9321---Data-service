from flask import Flask
from flask_restplus import Resource, Api
import sqlite3
import pandas as pd
from pandas.io import sql

app = Flask(__name__)
api = Api(app)


@api.route('/books/<int:id>')
class Books(Resource):
    def get(self,id):
        if (id in df.index):
            print("found")
            book = dict(df.loc[id])
            return book
        else:
            api.abort(404, "Book {} doesn't exist".format(id))

    def delete(self,id):
        if (id in df.index):
            df.drop(id,inplace=True)
            df.to_csv("new.csv")
        else:
            api.abort(404, "Book {} doesn't exist".format(id))


if __name__ == '__main__':
    columns_to_drop = ['Edition Statement',
                       'Corporate Author',
                       'Corporate Contributors',
                       'Former owner',
                       'Engraver',
                       'Contributors',
                       'Issuance type',
                       'Shelfmarks'
                       ]
    csv_file = "Books.csv"
    df = pd.read_csv(csv_file)

    # drop unnecessary columns
    df.drop(columns_to_drop, inplace=True, axis=1)

    # clean the date of publication & convert it to numeric data
    new_date = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
    new_date = pd.to_numeric(new_date)
    new_date = new_date.fillna(0)
    df['Date of Publication'] = new_date

    # replace spaces in the name of columns
    df.columns = [c.replace(' ', '_') for c in df.columns]

    # set the index column; this will help us to find books with their ids
    df.set_index('Identifier', inplace=True)
    app.run(debug=True)
