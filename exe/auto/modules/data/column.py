def add_column(name_table,cursor,name_column,type_column):
    try:
        cursor.execute(f"ALTER TABLE {name_table} ADD COLUMN {name_column} {type_column}")
    except:
        print("Error")