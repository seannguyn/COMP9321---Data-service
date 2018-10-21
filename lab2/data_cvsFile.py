import pandas as pd
import numpy as np

def hello():
    raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
    df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
    df.drop(columns=['last_name'])
    # save data to csv on db
    df.to_csv('example.csv')

    # load a csv file

    # No header
    # df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', header=None)

    # specifying columns
    # df = pd.read_csv('pandas_dataframe_importing_csv/example.csv',
            # names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])

    #
    # df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', index_col='UID', names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])

    # Load a csv while specifying “.” as missing values
    # sentinels = {'Last Name': ['.', 'NA'], 'Pre-Test Score': ['.']}
    # df = pd.read_csv('pandas_dataframe_importing_csv/example.csv', na_values=sentinels, skiprows=3)
    # pd.isnull(df)




    print("hello")

    df = pd.DataFrame(np.arange(12).reshape(3,4),columns=['A', 'B', 'C', 'D'])
    df.drop(['B', 'C'], axis=1)
    print(df)
    df.to_csv('new.csv')

if __name__ == '__main__':
    hello()
