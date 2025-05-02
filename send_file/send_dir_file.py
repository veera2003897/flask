from flask import Flask,send_from_directory


app=Flask(__name__)

@app.route('/vs')
def send_dir():
    dir_path='/home/veeranjaneyulu/PyCharmMiscProject'
    return send_from_directory(dir_path,"Dates lines (1).xlsx",as_attachment=True)

app.run(debug=True)