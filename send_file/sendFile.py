from flask import Flask,send_file,Response

app = Flask(__name__)

@app.route('/')
def download_file():
    file_path='/home/veeranjaneyulu/Downloads/Dates lines.xlsx'
    a=send_file(file_path,as_attachment=True)
    return Response(a)

app.run(debug=True)