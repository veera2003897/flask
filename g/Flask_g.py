from flask import Flask,g,jsonify

app = Flask(__name__)

# def get_db():
#     #if 'db' not in g:
#     g.db = 'Database connection done'
#     g.veera ='My name is veera'
#     return g.db

@app.route('/')
def index():
    #db_connection = get_db()
    g.db = 'Database connection done'
    g.veera = 'My name is veera'
    return jsonify({'g.db':g.db,'g.veera':g.veera})

# @app.teardown_appcontext
# def close_db():
#     db=g.pop('db',None)
#     return db

app.run(debug=True)