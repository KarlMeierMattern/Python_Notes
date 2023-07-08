from flask import Flask, request

app = Flask(__name__)

logins = {}
logins["david"] = {"email" : "a@a.com", "password" : "Baldy1"}
logins["katie"] = {"email" : "b@b.com", "password" : "k8t"}
logins["yul"] = {"email" : "c@c.com", "password" : "etc"}

@app.route("/login", methods = ["POST"])
def login():
  form = request.form
  try:
    # store the process of accessing the logins dictionary for a particular username in the variable details
    details = logins[form["username"]]
  except:
    return "Username incorrect"
  if form["email"] == details["email"] and form["password"] == details["password"]:
    return "You are logged in"
  else:
    return "Username, email or password incorrect"

@app.route('/')
def index():
  page = """<form method="post" action="/login">
    <p>Username: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="email" required></p>
    <p>Password: <input type="password" name="password" required></p>
    <button type="submit">Login</button>
      
  </form>"""
  return page


app.run(host='0.0.0.0', port=5400)

# http://localhost:5400/
