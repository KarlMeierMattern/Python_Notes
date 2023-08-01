from flask import Flask, request, redirect
# imports request and redirect as well as flask

# used to create a Flask application object named app with a specified static URL path.
app = Flask(__name__, static_url_path='/static')
# path to the static file that stores my images

users = {}
users["david"] = {"password" : "Baldy1"}
users["katie"] = {"password" : "k8t"}
# A dictionary hard coded into the program that stores the login details for two users
# "static" refers to the directory where you can store static files such as images, CSS stylesheets, JavaScript files, etc.
# These files are typically served directly by the web server without any processing by the Flask application.
# By default, Flask expects the static files to be located in a directory named "static" within the root directory of the application. 
# However, the static_url_path='/static' parameter is used to explicitly define the URL path where the static files will be served from.

@app.route('/login', methods=["POST"])
def login():
  form = request.form
  # request.form is used to access the form data submitted in the POST request.
  # It returns a dictionary-like object that contains the form field names as keys and their corresponding values as values.
 
  try:
    if users[form["username"]]["password"] == form["password"]:
      return redirect("/yup")
    # By using form["username"], the code retrieves the value of the "username" field from the form data. This value is then used as a key to access the users dictionary.
    # The subsequent ["password"] is used to retrieve the value associated with the "password" key within the dictionary entry corresponding to the provided username. 
    # Essentially, it retrieves the password associated with the username entered in the form.
    else:
      return redirect("/nope")
  except:
    return redirect("/nope")
# Login checking code - uses POST because it's dealing with usernames & passwords so we want encryption
# If the user details are correct, they get a lovely success gif, if not, they get a 'nope' gif.
# Try except used to load the 'nope' in case there's an error.

@app.route("/nope")
def nope():
  return """<img src="static/nerdy.gif" height="100">"""

@app.route("/yup")
def yup():
  page = """<img src="static/yup.gif" height="100">"""
  f = open("change.html", "r")
  page += f.read()
  f.close()
  return page

# page += f.read() combines the contents of "change.html" with the image HTML previously assigned to the page variable.
# The two methods above load the relevant gif depending on the result of the '/login' method

@app.route('/')
def index():
  page = ""
  f = open("login.html", "r")
  page = f.read()
  f.close()
  return page

# Loads the login HTML page that I've built separately on run.

app.run(host='0.0.0.0', port=81)