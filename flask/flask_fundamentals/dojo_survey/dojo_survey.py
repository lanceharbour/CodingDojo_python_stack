from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey', methods=['POST'])
def submit_survey():
    print(("*")*80)
    print("submitting survey")
    print(request.form)
    name_from_form = request.form['name']
    dojo_location = request.form['location']
    fav_language = request.form['language']
    comments_from_form = request.form['comments']
    return render_template("result.html", result_name=name_from_form, result_location=dojo_location, 
    result_fav=fav_language, result_comment=comments_from_form)

if __name__ == "__main__":
    app.run(debug=True)