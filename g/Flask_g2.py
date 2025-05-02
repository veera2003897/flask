from flask import Flask, g

app = Flask(__name__)

@app.before_request
def before_request():
    # Store multiple pieces of data in `g`
    g.user = "Veera"
    g.db_connection = "Database connection active"
    g.request_id = 12345
    return f'{g.user}-----{g.db_connection}------{g.request_id}'

@app.route('/')
def index():
    # Access the data stored in `g`
    return f"User: {g.user}, Request ID: {g.request_id}"

# @app.route('/details')
# def details():
#     return f"Database: {g.db_connection}, User: {g.user}"
