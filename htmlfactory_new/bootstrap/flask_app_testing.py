from flask import Flask, render_template
from htmlfactory_new.TagFactory import Tagged

# export FLASK_APP=flask_app_testing
# export FLASK_ENV=development
# flask run


app = Flask(__name__)

first_div = Tagged(raw_tag="div.jumbotron.text-center")
first_div.add_child(Tagged(raw_tag="h1", innerHTML="My first bootstrap page"))
first_div.add_child(
    Tagged(raw_tag="p", innerHTML="Resize this responsive page to see the effect!")
)


@app.route("/")
def hello() -> str:
    return render_template("index.html", bootstrap_html=first_div.get_pretty_str())
