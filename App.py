from flask import Flask, render_template, request, url_for, redirect
import json
app=Flask(__name__)
rules= """ 
# if state 0
0 x*** -> N 0
0 N*** -> W 1

# if state 1
1 ***x -> S 1
1 ***S -> X 0
"""
global state
state = 0
global step
step = 0
global board
board = []
row = []
global picolocation
picolocation = [10,10]
for i in range(0,25):
    for j in range(0,25):
        row.append("unvisited")
    board.append(row)
    row = []
board[picolocation[0]][picolocation[1]] = "picobot"

def step_forward():
    global state
    global step
    surr = get_surr()
    for v in rules.splitlines():
        rul = v.split()
        if len(rul) >= 5 and '#' not in rul[0]:
            if int(rul[0]) == state and match_surr(surr,rul[1]):
                if not is_stop(rul[3]):
                    move_dir(rul[3])
                state = int(rul[4])
                print("Rule applied: " + v)
                break
    step += 1

def is_stop(direction):
    w = '.'
    surr = get_surr()
    if  direction == 'N':
        w = surr[0]
    if direction == 'E':
        w = surr[1]
    if direction == 'W':
        w = surr[2]
    if direction == 'S':
        w = surr[3]
    return w==direction

def move_dir(direction):
    global picolocation
    global board
    board[picolocation[0]][picolocation[1]] = "visited"
    if direction == 'N':
        picolocation[1] -= 1
    if direction == 'E':
        picolocation[0] += 1
    if direction == 'W':
        picolocation[0] -= 1
    if direction == 'S':
        picolocation[1] += 1
    if direction == 'X':
        pass
    board[picolocation[0]][picolocation[1]] = "picobot"

def get_surr():
    surr = []
    for i in range(0,4):
        surr.append('x')
    if(picolocation[1]<=0 or board[picolocation[0]][picolocation[1] - 1] == "wall"):
        surr[0] = 'N'
    if(picolocation[0]>=24 or board[picolocation[0] + 1][picolocation[1]] == "wall"):
        surr[1] = 'E'
    if(picolocation[0]<=0 or board[picolocation[0] - 1][picolocation[1]] == "wall"):
        surr[2] = 'W'
    if(picolocation[1]>=24 or board[picolocation[0]][picolocation[1] + 1] == "wall"):
        surr[3] = 'S'
    return surr

def match_surr(surr, rul):
    rullst = [c for c in rul]
    for i in range(0,4):
        if surr[i] != rullst[i] and rullst[i] != '*':
            return False
    return True
 
def is_win():
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == "unvisited":
                return False
    return True

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/staging',methods=['GET','POST'])
def staging():
    if request.method == 'POST':
        #rules = request.form.get("rules")
        rool = request.form.get("textrules")
        global rules
        rules = rool
        return redirect(url_for('frame'))
    return render_template('staging.html',rules=rules)

@app.route('/frame',methods=['GET','POST'])
def frame():
    #print(board[0][0])
    step_forward()
    if(is_win()):
        return "you win!"
    return render_template('frame.html', board=board, rules=rules)

@app.route('/frame_anim', methods=['GET','POST'])
def frame_anim():
    step_forward()
    if(is_win()):
        return "you win!"
    return render_template('framez.html', board=board, rules=rules)

@app.route('/reset',methods=['GET'])
def reset():
    global step
    global board
    global picolocation
    global state
    state = 0
    step = 0;
    row = []
    board = []
    picolocation = [10,10]
    row = []
    for i in range(0,25):
        for j in range(0,25):
            row.append("unvisited")
        board.append(row)
        row = []
    return redirect(url_for('staging'))

if __name__ =="__main__":
    app.run("0.0.0.0", port=80)