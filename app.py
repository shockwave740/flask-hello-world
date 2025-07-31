
from flask import Flask
import psycopg2
db_url = "postgresql://majeski_lab10_postgres_user:AZdm4W5PQxFcvAVRy0mnWFbsgt5B1MGj@dpg-d259skfdiees73asb150-a/majeski_lab10_postgres"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Zach Majeski in 3308!'

@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect(db_url)   # Step 1: Try to connect (from tutorial)
        conn.close()                      # Step 2: Close connection (from tutorial)
        return "Database connection successful!"   # Step 3: Confirmation message (from tutorial)
    except Exception as e:
        return f"Database connection failed: {e}"  # Step 4: Error, if connection fails


if __name__ == '__main__':
    app.run(debug=True)