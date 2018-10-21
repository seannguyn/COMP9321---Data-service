import sqlite3
import pandas as pd
import numpy as np
from pandas.io import sql
import re
import matplotlib.pyplot as plt

def merge():
    summer = pd.read_csv('Olympics_dataset1.csv', skiprows=1)
    summer.columns.values[0] = 'Country'

    winter = pd.read_csv('Olympics_dataset2.csv' , skiprows=1)
    winter.columns.values[0] = 'Country'

    merge_Res = pd.merge(summer, winter, how='right', left_on='Country', right_on='Country' ,suffixes=('_Summer', '_Winter'), copy=True, validate='one_to_one')

    # change column name for clarity
    for column in merge_Res.columns:
        if ('.1' in column):
            newName = column.replace('.1', '_combined')
            merge_Res.rename(columns={column:newName}, inplace=True)

    return merge_Res

def del_nan(merge_Res):

    columnList = ['Country',
    'Number of Games the country participated in_Summer','Gold_Summer','Silver_Summer','Bronze_Summer','Total_Summer',
    'Number of Games the country participated in_Winter','Gold_Winter','Silver_Winter','Bronze_Winter','Total_Winter',
    'Number of Games the country participated in_Combined','Gold_Combined','Silver_Combined','Bronze_Combined','Total_Combined']


    df = pd.DataFrame(columns=columnList)
    flag = 0

    merge_Res = del_rubbish(merge_Res)

    for row in merge_Res.itertuples():
        for i in range(0,len(row)):
            if pd.isnull(row[i]):
                flag = 1
        if flag == 0:
            # print(row[1],row[2],row[3],row[4],row[5])
            # print(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
            #         row[11],row[12],row[13],row[14],row[15],row[16])
            # print()
            df2 = pd.DataFrame([[row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],
                    row[11],row[12],row[13],row[14],row[15],row[16]]],columns=columnList)
            df = pd.concat([df, df2])

        flag = 0
    # print(df)
    return df

def del_rubbish(df):

    df = df.drop(columns='Rubish')
    return df

def set_index(df,index_str):
    return df.set_index(index_str)

def find_max(df,column_name):
    return

def getMaxMedal(merge_Res):

    merge_Res['Total_Combined'] = merge_Res['Total_Combined'].str.replace(',', '')
    merge_Res['Total_Combined'] = merge_Res['Total_Combined'].astype(int)

    res = merge_Res.sort_values(by=['Total_Combined'],ascending=False)
    return res

def convert_to_int(df,col_list):

    for item in col_list:
        df[item] = df[item].str.replace(',', '')
        df[item] = df[item].astype(int)

    return df

def question_1():

    print("question 1")

    # merge two csv, return the dataframe
    merge_Res = merge()

    # print first 5 rows
    print(merge_Res.head(5))


    merge_Res.to_csv("q1.csv")

def question_2():

    print("question 2")

    # merge
    merge_Res = merge()

    # set index to be Country
    merge_Res = set_index(merge_Res,'Country')

    print(merge_Res.head(1))
    (merge_Res.head(1)).to_csv("q2.csv")


def question_3():

    print("question 3")

    merge_Res = merge()
    merge_Res = set_index(merge_Res,"Country")
    merge_Res = del_rubbish(merge_Res)

    print(merge_Res.head(5))
    merge_Res.to_csv("q3.csv")



def question_4():

    print("question 4")

    # merging, delete NaN fields, set index to 'Country'
    df = merge()
    df = del_nan(df)
    res = set_index(df,'Country')

    # display last 10 rows
    print(res.tail(10))
    res.to_csv("q4.csv")


def question_5():

    print("question 5")

    # merge, delete last row (which is the Total row), delete NaN fields
    df = merge()
    df = df[:-1]
    merge_Res = del_nan(df)

    # convert Gold_Summer to int value
    merge_Res = convert_to_int(merge_Res,['Gold_Summer'])

    # sort
    res = merge_Res.sort_values(by=['Gold_Summer'],ascending=False)

    # create new DataFrame display country and Gold Medal in Summber
    MostSummerGold = pd.DataFrame([[res.iat[0,0],res.iat[0,2]]],columns=['Country','Gold_Summer'])
    MostSummerGold = set_index(MostSummerGold,'Country')

    print(MostSummerGold)

    MostSummerGold.to_csv("q5.csv")

def question_6():
    print("Question 6")

    # merge, delete last row (which is the Total row), delete NaN fields
    df = merge()
    df = df[:-1]
    merge_Res = del_nan(df)

    # convert these 2 columns into integer
    merge_Res = convert_to_int(merge_Res,['Gold_Winter','Gold_Summer'])

    # find the Difference, convert to absolute value
    merge_Res['Val_Diff'] = (merge_Res['Gold_Winter'] - merge_Res['Gold_Summer']).abs()

    # sort
    res = merge_Res.sort_values(by=['Val_Diff'],ascending=False)

    # create new DataFrame, showing Country, Gold in Summer, Winter, and the Difference
    columnList = ['Country','Gold_Summer','Gold_Winter','Difference']
    Gold_diff = pd.DataFrame([[res.iat[0,0],res.iat[0,2],res.iat[0,7],res.iat[0,16]]],columns=columnList)
    Gold_diff = set_index(Gold_diff,'Country')

    print(Gold_diff)

    res.to_csv("q6.csv")

def question_7():

    print("question 7")

    # merge, delete last row (which is the Total row), delete NaN fields
    df = merge()
    df = df[:-1]
    merge_Res = del_nan(df)

    # sort medal in terms of Total_medal_combined
    res = getMaxMedal(merge_Res)
    res = set_index(res,'Country')

    print(res.head(5))
    print(res.tail(5))

    res.to_csv("q7.csv")

def question_8():
    print("question 8")

    # merge, delete last row (which is the Total row), delete NaN fields
    df = merge()
    df = df[:-1]
    merge_Res = del_nan(df)

    # sort medal in terms of Total_medal_combined
    res = getMaxMedal(merge_Res)
    columnList = ['Country','Total_Summer','Total_Winter']
    Total_medal = pd.DataFrame(columns=columnList)

    # get the top 10 country with most medals in Summer and Winter
    for i in range(0,10):
        df1 = pd.DataFrame([[res.iat[i,0],res.iat[i,5],res.iat[i,10]]],columns=columnList)
        Total_medal = pd.concat([Total_medal, df1])


    # set index
    Total_medal=set_index(Total_medal,'Country')

    # convert columns to integer
    Total_medal = convert_to_int(Total_medal,['Total_Winter','Total_Summer'])

    # plot
    Total_medal.plot.barh(stacked=True);
    plt.tight_layout()
    plt.show()

def question_9():
    print("question 9")

    country_list = ['United States', 'Australia', 'Great Britain', 'Japan', 'New Zealand']
    columnList = ['Country','Gold_Winter','Silver_Winter','Bronze_Winter']

    # merge, delete last row (which is the Total row), delete NaN fields
    df = merge()
    df = df[:-1]
    merge_Res = del_nan(df)

    # dataframe
    five_country = pd.DataFrame(columns=columnList)

    # get row that is (USA, AUS, JAP, NZ, GREAT BRITAIN)
    for row in merge_Res.itertuples():
        if ('United States' in row[1] or
            'Australia' in row[1] or
            'Great Britain' in row[1] or
            'Japan' in row[1] or
            'New Zealand' in row[1]):

            df2 = pd.DataFrame([[row[1],row[8],row[9],row[10]]],columns=columnList)
            five_country = pd.concat([five_country, df2])


    # set index
    five_country = set_index(five_country,'Country')

    # convert to columns to integer
    five_country = convert_to_int(five_country,['Gold_Winter','Silver_Winter','Bronze_Winter'])

    # plot
    five_country.plot.bar();
    plt.tight_layout()
    plt.show()
    five_country.to_csv("q9.csv")


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    # question_1()
    # question_2()
    # question_3()
    # question_4()
    question_5()
    # question_6()
    # question_7()
    # question_8()
    # question_9()
