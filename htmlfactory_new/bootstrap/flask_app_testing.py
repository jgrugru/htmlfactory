from flask import Flask
from htmlfactory_new.TagFactory import Tagged

# export FLASK_APP=hello
# export FLASK_ENV=development


app = Flask(__name__)

beginning = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
"""

ending = """
</body>
</html>
"""

first_div = Tagged(raw_tag="div.jumbotron.text-center")
first_div.add_child(Tagged(raw_tag="h1", innerHTML="My first bootstrap page"))
first_div.add_child(
    Tagged(raw_tag="p", innerHTML="Resize this responsive page to see the effect!")
)

html_str = beginning + first_div.get_pretty_str() + ending


@app.route("/")
def hello():
    return html_str


# <div class="jumbotron text-center">
#   <h1>My First Bootstrap Page</h1>
#   <p>Resize this responsive page to see the effect!</p>
# </div>

# <div class="container">
#   <div class="row">
#     <div class="col-sm-4">
#       <h3>Column 1</h3>
#       <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
#       <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
#     </div>
#     <div class="col-sm-4">
#       <h3>Column 2</h3>
#       <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
#       <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
#     </div>
#     <div class="col-sm-4">
#       <h3>Column 3</h3>
#       <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit...</p>
#       <p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris...</p>
#     </div>
#   </div>
# </div>
