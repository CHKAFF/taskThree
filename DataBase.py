import psycopg2
from psycopg2 import Error
conn = psycopg2.connect(dbname = "d5mhrq9t2vc1rv", user = "olwjzezmhvmmtn", password = "98cbebb2f545dae6c3bc6b501e9ceef5b6b4835de6a1f18c742984f6f7edf2e5", host = "ec2-54-247-178-166.eu-west-1.compute.amazonaws.com")
cursor = conn.cursor()

class DataBase:
    def insert_id(ids):
        insert_query = '''INSERT INTO id VALUES ids'''
        cursor.execute(insert_query)
        conn.commit()
        cursor.close()
        conn.close()
#create_table_query = '''CREATE TABLE counter (id integer, cash integer, costs text, costsi integer);'''

#cursor.execute(create_table_query)
#conn.commit()


