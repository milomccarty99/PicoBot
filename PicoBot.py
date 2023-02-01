from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import json
import TextInterpreter

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
        pbrules.insert_one({'id':123, 'rules':request.form['rules']})

        
        return redirect(url_for('run',rules=request.form['rules']))
    return render_template('index.html', x=xsize,y=ysize)

@app.route('/run<rules>', methods=['GET','POST'])
def run(rules):
    if(request.method == 'POST'):
        return redirect(url_for('runstep', step=0))

    tiles = [["unvisited", "wall"],["picobot", "unvisited"]]
    return render_template('anim.html',board=tiles)


@app.route('/run<rules>/step<step>', methods=['GET','POST'])
def runstep(rules, step):
    if(request.method == 'POST'):
        return redirect(url_for('runstep',step=int(step)+1))
    tiles =[ ["unvisited", "wall"],["picobot", "unvisited"]]
    return render_template('anim.html',board=tiles, step=step, rules=pbrules.findOne({id:123}))
if __name__ == "__main__":
    app.run("0.0.0.0", port=80)

