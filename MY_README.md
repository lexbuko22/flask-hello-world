# README

This is the [Flask](http://flask.pocoo.org/) [quick start](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application) example for [Render](https://render.com).

## Deployment

Follow the guide at https://render.com/docs/deploy-flask.
* Follow the [Flask quick start tutorial](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)
* Sample project with [Render](https://render.com).
* Tutorial to [deploy a website](https://render.com/docs/deploy-flask).


# Flask PostgreSQL Example

This is a simple Flask application that demonstrates basic operations on a PostgreSQL database. The application utilizes the psycopg2 library to interact with the PostgreSQL database that is hosted on Render.

## Prerequisites
- Python 3
- Flask
- psycopg2
- PostgreSQL

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/cu-cspb-3308-software-dev-spring-2024/lab-10-lexbuko22.git
    ```
2. Navigate to the project directory:
    ```
    cd flask-hello-world
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set up a PostgreSQL database on Render and replace the database URL in the code with your database URL.

## Usage
1. Run the Flask application:
    ```
    Flask --app app.py run
    ```
2. Access the following routes in your web browser or using an API testing tool like Postman:
    - `/`: Displays a simple greeting message.
    - `/db_test`: Tests the connection to the PostgreSQL database.
    - `/db_create`: Creates a table named 'Basketball' in the database if it doesn't exist.
    - `/db_insert`: Inserts sample records into the 'Basketball' table.
    - `/db_select`: Retrieves all records from the 'Basketball' table and displays them in an HTML table format.
    - `/db_drop`: Drops the 'Basketball' table from the database.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License
