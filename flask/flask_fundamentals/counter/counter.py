from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
        print(session['counter'])
    else:
        session['counter'] = 0
    return render_template("index.html", count=session['counter'])

@app.route('/increment_counter', methods=['POST'])
def increment():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset_counter', methods=['POST'])
def reset():
    session.pop('counter')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)