import sqlite3
import os
def create_table(name_table,list_values,cursor):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {name_table} ({list_values[0]},{list_values[1]})")
def delete_table(name_table,cursor):#я отойду не на долго
    cursor.execute(f"DROP TABLE {name_table}")