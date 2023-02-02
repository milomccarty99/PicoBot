from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import json
import TextInterpreter
import Board

app=Flask(__name__)

mongoclient = MongoClient("mongodb://127.0.0.1:27017")
db = mongoclient["picodatabase"]
pbrules = db["pbrules"]


@app.route('/')
def landing():
    return redirect(url_for('home'))
@app.route('/home', methods=['GET','POST'])
def home(xsize =25, ysize=25):
    x = xsize
    y = ysize
    if(request.method == 'POST'):
        pbrules.insert_one({'rules':request.form['rules']})

        
        return redirect(url_for('run',rules=request.form['rules']))
    return render_template('index.html', x=xsize,y=ysize)

@app.route('/run', methods=['GET','POST'])
def run():
    if(request.method == 'POST'):
        return redirect(url_for('runstep', step=0))
    textInterp = TextInterpreter.StateMachine(pbrules.find()[0]['rules'], 10,10)

    tiles = textInterp.getBoard()
    return render_template('anim.html',board=tiles)


@app.route('/run/step<step>', methods=['GET','POST'])
def runstep( step):
    if(request.method == 'POST'):
        return redirect(url_for('runstep',step=int(step)+1))
    textInterp = TextInterpreter.StateMachine(pbrules.find()[0]['rules'], 10,10)
    for i in range(0,int(step)):
        textInterp.stepforward()

    tiles = textInterp.getBoard()
   
    return render_template('anim.html',board=tiles, step=step)
if __name__ == "__main__":
    app.run("0.0.0.0", port=80)

