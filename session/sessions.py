from flask import Flask,request,session,jsonify,Response

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/set_session')
def set_session():
    #data = request.get_json()
    #print(data)
    #session['username'] = data['username1']
    session['name'] = 'veera'
    session['id'] = 954252
    print(session.items())
    #a=session.get('username')
    #session.clear()
    print(session.items())
    return list(session.items())

@app.route('/get_session' , methods = ['GET'])
def get_session():
    username = session.get('username')
    print(username)
    print(session.get('username1'))
    print(session.items())

    return jsonify({"username":session.get('username')})

   # return jsonify({"message":"No session data found"})

@app.route('/clear_session',methods=['GET'])
def clear_session():
    session.clear()
    return jsonify({"message":"Session cleared"})

app.run(debug=True)