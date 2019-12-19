from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry! No response. Try diffent path."
#****************************
@app.route('/')
def hello_world():
    print("*"*60)
    print("hello_world function")
    return 'Hello World!'
#****************************
@app.route('/dojo')
def dojo():
    print("*"*60)
    print("dojo function")
    return 'Dojo'
#****************************
@app.route("/say/<name>")
def say_name(name):
    print("*"*60)
    print("say_name function")
    print(name)
    return F"Hi {name}!"
#****************************
@app.route("/repeat/<int:repeat>/<text>")
def repeat(repeat,text):
    print("*"*60)
    print("repeat function")
    print(repeat,text)
    return (text+" ")*int(repeat)
if __name__=="__main__":
    app.run(debug=True)