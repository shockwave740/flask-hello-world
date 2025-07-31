
from flask import Flask
import psycopg2
db_url = "postgresql://majeski_lab10_postgres_user:AZdm4W5PQxFcvAVRy0mnWFbsgt5B1MGj@dpg-d259skfdiees73asb150-a/majeski_lab10_postgres"

app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello World from Zach Majeski in 3308!'

@app.route('/db_create')
def db_create():
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        ''')
        conn.commit()
        conn.close()
        return "Basketball Table Created"
    except Exception as e:
        return f"Table creation failed: {e}"

@app.route('/db_insert')
def db_insert():
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
            ('Zach', 'Majeski', 'CU Boulder', 'Bulls', 3308);
        ''')
        conn.commit()
        conn.close()
        return "Basketball Table Populated"
    except Exception as e:
        return f"Insert failed: {e}"

@app.route('/db_select')
def db_select():
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute('SELECT * FROM Basketball;')
        records = cur.fetchall()
        conn.close()
        response = "<table border=1><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
        for row in records:
            response += "<tr>"
            for item in row:
                response += f"<td>{item}</td>"
            response += "</tr>"
        response += "</table>"
        return response
    except Exception as e:
        return f"Select failed: {e}"

@app.route('/db_drop')
def db_drop():
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS Basketball;')
        conn.commit()
        conn.close()
        return "Basketball Table Dropped"
    except Exception as e:
        return f"Drop failed: {e}"

@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect(db_url)   
        conn.close()                      
        return "Database connection successful!"   
    except Exception as e:
        return f"Database connection failed: {e}"  


if __name__ == '__main__':
    app.run(debug=True)