import sqlite3

DB_NAME = "test.db"
courses_list = [(1, "Python", 1000, 30), (2, "JavaScript", 400, 50),
                (3, "C++", 1400, 130), (4, "Kotlin", 2000, 230),]

with sqlite3.connect(DB_NAME) as conn:
    print(conn)
    print(sqlite3.version_info)

# Create table
with sqlite3.connect(DB_NAME) as sql_conn:
    sql_request = f"""CREATE TABLE IF NOT EXISTS courses(
    id integer PRIMARY KEY,
    title text NOT NULL,
    students_qty integer,
    reviews_qty integer
    );"""
    sql_conn.execute(sql_request)

# Create data in table courses
with sqlite3.connect(DB_NAME) as sql_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    for course in courses_list:
        sql_conn.execute(sql_request, course)
    sql_conn.commit()

# Read data is courses
with sqlite3.connect(DB_NAME) as sql_conn:
    sql_request = "SELECT * FROM courses"
    data_response = sql_conn.execute(sql_request)
    print(data_response.fetchall())
