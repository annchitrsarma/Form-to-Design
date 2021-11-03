from flask import Flask, render_template, request, make_response
from flask.wrappers import Response
from flask import url_for
from fpdf import FPDF, HTMLMixin
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    firstname = request.form.get("first_name")
    lastname = request.form.get("last_name")
    language_choice = request.form.get("contact")
    selected = request.form.get("dropdown")
    about_yourself = request.form.get("description")
    
    
    output = render_template("output.html", firstname=firstname, lastname=lastname, language_choice=language_choice, selected=selected, about_yourself=about_yourself)
    return output
    


if __name__=="__main__":
    app.run(debug=True)