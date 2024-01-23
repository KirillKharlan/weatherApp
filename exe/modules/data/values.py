def get_value(name_table,cursor,name_column = "*"):
    cursor.execute(f"SELECT {name_column} FROM {name_table}")
    return cursor.fetchall()
 