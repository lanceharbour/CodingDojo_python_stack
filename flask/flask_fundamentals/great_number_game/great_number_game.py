from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'whatever I want this to be'

@app.route('/')
def index():
    if 'random' in session:
        print(f"random already set {session['random']}")
    else:
        session['random'] = random.randint(1,100)
        print(f"setting random {session['random']}")
    if 'game_result' in session:
        print(f"game in play")
    else:
        session['game_result'] = None
    return render_template("index.html")

@app.route('/user_guess', methods=['POST'])
def random_num():
    if int(request.form['guess']) == session['random']:
        session['game_result'] = "win"
        print(f"winner: random {session['random']} = {request.form['guess']} guess")
    if int(request.form['guess']) > session['random']:
        session['game_result'] = "high"
        print(f"loser: random {session['random']} < {request.form['guess']} guess")
    if int(request.form['guess']) < session['random']:
        session['game_result'] = "low"
        print(f"loser: random {session['random']} > {request.form['guess']} guess")
    return redirect('/')

@app.route('/reset_game', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == ("__main__"):
    app.run(debug=True)