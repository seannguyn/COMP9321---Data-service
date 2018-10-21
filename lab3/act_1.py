import sqlite3
import pandas as pd
from pandas.io import sql

def print_dataframe(dataframe, print_column=True, print_rows=True):
    # print column names
    if print_column:
        print(",".join([column for column in dataframe]))

    # print rows one by one
    if print_rows:
        for index, row in dataframe.iterrows():
            print(",".join([str(row[column]) for column in dataframe]))

# drop column and calculate null cell
def activity_1():
    columns_to_drop = ['Edition Statement',
                       'Corporate Author',
                       'Corporate Contributors',
                       'Former owner',
                       'Engraver',
                       'Contributors',
                       'Issuance type',
                       'Shelfmarks'
                       ]



    df = pd.read_csv("Books.csv")

    row_num = df.shape[0]

    for col in df:
        percent = 100 * df[col].isnull().sum() / row_num
        print(col, percent)


    df.drop(columns_to_drop, inplace=True, axis=1)
    print("(=============)")
    for col in df:
        percent = 100 * df[col].isnull().sum() / row_num
        print(col, percent)


def clean(x):
    if "London" in x:
        return "London"
    else:
        return x.replace("-","")

def activity_2():
    columns_to_drop = ['Edition Statement',
                       'Corporate Author',
                       'Corporate Contributors',
                       'Former owner',
                       'Engraver',
                       'Contributors',
                       'Issuance type',
                       'Shelfmarks'
                       ]

    df = pd.read_csv("Books.csv")
    df['Place of Publication'] = df['Place of Publication'].apply(clean)
    # print(df['Place of Publication'])

    new_date = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)

    new_date = pd.to_numeric(new_date)
    # print(df['Date of Publication'])

    # replace all NaN with 0
    new_date = new_date.fillna(0)
    df['Date of Publication'] = new_date
    print(df['Date of Publication'])

    return df

def activity_3():
    df = activity_2()
    # df.columns = [c.replace(' ', '_') for c in df.columns]

    #######################################################
    col_list = []
    for col in df.columns:
        col_list.append(col.replace(' ','_'))

    df.columns = col_list
    #######################################################

    print(df.columns)

    print(df.query('Place_of_Publication == "London" and Date_of_Publication > 1866'))

if __name__ == '__main__':
    activity_1()
    activity_2()
    activity_3()
