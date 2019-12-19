from flask import Flask, render_template, redirect, request, session
from random import randint
from datetime import datetime

app = Flask(__name__)
app.secret_key = "my super secret key"

@app.route('/')
def index():
    if "user_gold" not in session:
        session['activities'] = []
        session['user_gold'] = 0
        print(f"setting user_gold = {session['user_gold']}")
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    print('*'*60)
    gold = 0
    building = ""
    if request.form['building'] == 'farm':
        gold = randint(10,20)
        session['user_gold'] += gold
        building = 'farm'
        print(f"farm: {session['user_gold']}")
    if request.form['building'] == 'cave':
        gold = randint(5,10)
        session['user_gold'] += gold
        building = 'cave'
        print(f"cave: {session['user_gold']}")
    if request.form['building'] == 'house':
        gold = randint(2,5)
        session['user_gold'] += gold
        building = 'house'
        print(f"house: {session['user_gold']}")
    if request.form['building'] == 'casino':
        gold = randint(-50,50)
        session['user_gold'] += gold
        building = 'casino'
        print(f"casino: {session['user_gold']}")

    if gold < 0:
        result = f"Entered the casino and lost {gold} gold! {datetime.now()}"
    else:
        result = f"Earned {gold} from {building}, {datetime.now()}"
        session['activities'].append({'result': result})
    print(session['activities'])

    return redirect('/')

@app.route('/reset_game', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == ("__main__"):
    app.run(debug=True)