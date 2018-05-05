from flask import Flask, render_template,redirect,request,session
app = Flask(__name__)
app.secret_key="myKey"

@app.route('/')
def index():
    
    session['count']+=1
    
    return render_template("index.html")
@app.route('/pls2')
def pls2():
    session['count']+=1
    return redirect('/')


@app.route('/reset')
def reset():
    session['count']-=session['count']+1
    return redirect('/')
app.run(debug=True)