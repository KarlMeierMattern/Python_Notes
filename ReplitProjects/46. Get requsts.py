from flask import Flask, request

app = Flask(__name__)

@app.route('/language', methods = ["GET"])
def lang():
  data = request.args
  if data == {}:
    return "Nothing here"
  if data["lang"]=="eng":
    return "Hello, and welcome to our wonderful website!"
  elif data["lang"]=="wel":
    return "Helo, a chroeso i'n gwefan wych!"
    
@app.route('/')
def index():
    return 'New page'


app.run(host='0.0.0.0', port=81)

# http://localhost:81/language?lang=eng
# http://localhost:81/language?lang=wel