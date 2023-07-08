from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello there"

@app.route('/home')
def home():
  print("Rendering portfolio.html")
  return render_template('portfolio.html', name='John Doe', title='My Title', text='Lorem ipsum...')

app.run(host='0.0.0.0', port=5000, debug=True)


# http://localhost:5000/