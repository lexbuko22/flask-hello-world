from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Lex in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://db_3308_lab_10_database_user:MdjBG8gwLpnfuMJonHc3TFWDZxmfaQBf@dpg-co0tg1gcmk4c73b7os60-a/db_3308_lab_10_database")
    conn.close()
    return "Database Connection Succesful"
