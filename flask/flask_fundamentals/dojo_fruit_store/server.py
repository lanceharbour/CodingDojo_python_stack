from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    total = int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {total} fruits")
    now=datetime.now()
    timestamp=now.strftime("%c")
    return render_template("checkout.html", strawberry_qty=request.form['strawberry'], 
    raspberry_qty=request.form['raspberry'], apple_qty=request.form['apple'], first_name=request.form['first_name'], 
    last_name=request.form['last_name'], student_id=request.form['student_id'],fruit_total=total,purchase_time=timestamp)

@app.route('/fruits')         
def fruits():
    import os
    path = os.getcwd()+"\\static\\img"
    imgs =  os.listdir(path)
    print(imgs)
    return render_template("fruits.html",fruits=imgs)

if __name__=="__main__":   
    app.run(debug=True)    