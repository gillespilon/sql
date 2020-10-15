#! /usr/bin/env python3
"""
Example of an sqlite3 db

- Create a dataframe
- Save as a table in a database
"""

from sqlalchemy import create_engine
import datasense as ds
import pandas as pd
import sqlite3

# connection = sqlite3.connect('food.db')
# cursor = connection.cursor()

# list tables in database
# cursor.execute(
#     "SELECT name FROM sqlite_master\
#     WHERE type = 'table'\
#     ORDER BY name;"
# )
# print(cursor.fetchall())
# print()

# read table into dataframe
# query = "SELECT * FROM groceries;"
# df = pd.read_sql(query, connection)
# print(df)
# print()

# cursor.execute("DROP table 'test'")
# save dataframe to new database
# df.to_sql('test', connection, if_exists='replace', index = False)


def main():
    # engine = create_engine('sqlite://', echo=False)
    connection = sqlite3.connect('groceries.db')
    df = create_dataframe()
    print(df.head())
    print(df.dtypes)
    df.to_sql(
        name='my_groceries',
        con=connection,
        if_exists='replace',
        index=False
    )
    # list tables in database
    cursor = connection.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master\
        WHERE type = 'table'\
        ORDER BY name;"
    )
    print(cursor.fetchall())
    print()


def create_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(
        {
            'a': ds.random_data(
                distribution='uniform',
                size=42,
                loc=13,
                scale=70
            ),
            'b': ds.random_data(distribution='bool'),
            'c': ds.random_data(distribution='categories'),
            'd': ds.timedelta_data(),
            'i': ds.random_data(
                distribution='uniform',
                size=42,
                loc=13,
                scale=70
            ),
            'r': ds.random_data(
                distribution='strings',
                strings=['0', '1']
            ),
            's': ds.random_data(distribution='strings'),
            't': ds.datetime_data(),
            'u': ds.datetime_data(),
            'x': ds.random_data(distribution='norm'),
            'y': ds.random_data(distribution='randint'),
            'z': ds.random_data(distribution='uniform')
        }
    )
    return df


if __name__ == '__main__':
    main()
