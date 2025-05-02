from flask import Flask, render_template,flash,url_for,redirect

app=Flask(__name__)
app.secret_key="your_secret_key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/action_success')
def action_success():
    flash("Action completed","succees")
    return redirect(url_for('home'))

@app.route('/action_error')
def action_error():
    flash("An error Occured","error")
    return redirect(url_for('home'))

app.run( debug = True )