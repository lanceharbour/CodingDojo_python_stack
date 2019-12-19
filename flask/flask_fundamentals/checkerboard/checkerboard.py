from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html",num_rows=8,num_columns=8)

@app.route('/<rows>')
def checkerboard_rows(rows):
    return render_template("index.html",num_rows=int(rows),num_columns=8)

@app.route('/<rows>/<columns>')
def checkerboard_rows_columns(rows,columns):
    return render_template("index.html",num_rows=int(rows),num_columns=int(columns))

if __name__=="__main__":
    app.run(debug=True)