'''
This is a Flask application that demonstrates basic operations on a PostgreSQL database hosted on Render and was used as an assignment
in CSPB 3308 at CU Boulder Spring 2024.
'''


from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    '''
    This function returns a simple greeting message.
    '''
    return 'Hello World from Lex in 3308'

@app.route('/db_test')
def testing():
    '''
    This function tests the connection to the PostgreSQL database.
    '''
    conn = psycopg2.connect("postgres://db_3308_lab_10_database_user:MdjBG8gwLpnfuMJonHc3TFWDZxmfaQBf@dpg-co0tg1gcmk4c73b7os60-a/db_3308_lab_10_database")
    conn.close()
    return "Database Connection Succesful"


@app.route('/db_create')
def create():
    '''
    This function creates a table named 'Basketball' in the PostgreSQL database if it doesn't exist.
    '''
    conn = psycopg2.connect("postgres://db_3308_lab_10_database_user:MdjBG8gwLpnfuMJonHc3TFWDZxmfaQBf@dpg-co0tg1gcmk4c73b7os60-a/db_3308_lab_10_database")
    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar (255),
                Number int
                );
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"


@app.route('/db_insert')
def inserting():
    '''
    This function inserts records into the 'Basketball' table in the PostgreSQL database.
    '''
    conn = psycopg2.connect("postgres://db_3308_lab_10_database_user:MdjBG8gwLpnfuMJonHc3TFWDZxmfaQBf@dpg-co0tg1gcmk4c73b7os60-a/db_3308_lab_10_database")
    cur = conn.cursor()
    cur.execute(
        '''
        INSERT INTO Basketball (First, Last, City, Name, Number)
            Values
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
            ('Lex', 'Bukowski', 'CU Boulder', 'Fantastic Four', 3308);
        '''
    )
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    '''
    This function retrieves all records from the 'Basketball' table and displays them in an HTML table format.
    '''
    conn = psycopg2.connect("postgres://db_3308_lab_10_database_user:MdjBG8gwLpnfuMJonHc3TFWDZxmfaQBf@dpg-co0tg1gcmk4c73b7os60-a/db_3308_lab_10_database")
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM Basketball;
                ''')
    records = cur.fetchall()
    conn.close()
    response_string=''
    response_string+='<table>'
    for player in records:
        response_string+='<tr>'
        for info in player:
            response_string+='<td>{}</td>'.format(info)
        response_string+='</tr>'
    response_string+='</table>'
    return response_string

@app.route('/db_drop')
def dropping():
    '''
    This function drops the 'Basketball' table from the PostgreSQL database.
    '''
    conn = psycopg2.connect("postgres://db_3308_lab_10_database_user:MdjBG8gwLpnfuMJonHc3TFWDZxmfaQBf@dpg-co0tg1gcmk4c73b7os60-a/db_3308_lab_10_database")
    cur = conn.cursor()
    cur.execute('''
                DROP TABLE Basketball;
                ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"