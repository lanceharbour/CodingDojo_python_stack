from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def playground():
    return render_template("index.html",num_times=0)

@app.route('/play')
def play():
    return render_template("index.html",num_times=3)

@app.route('/play/<times>')
def play_times(times):
    return render_template("index.html",num_times=int(times))

@app.route('/play/<times>/<color>')
def times_color(times, color):
    return render_template("index.html",num_times=int(times),new_color=color)

if __name__=="__main__":
    app.run(debug=True)