from flask import Flask, request, render_template,jsonify


app=Flask(__name__)

@app.route('/square',methods=['GET'])
def square_Number():
    #render_template('get_http_method.html')
    name1 = request.args.get('name')
    number = request.args.get('number')
    number1= int(number) * int(number)
    return render_template('square_number.html',name_=name1,number1=number1)

@app.route("/")
def number():
    output=render_template('get_http_method.html')
    return jsonify({"prakash":""})

if(__name__ == "__main__"):

    app.run(debug=True)