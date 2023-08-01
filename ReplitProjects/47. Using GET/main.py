from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return "hello"

@app.route("/blog/hello")
def hr():
    return redirect("/hello")

@app.route("/blog/bye")
def br():
    return redirect("/bye")

@app.route('/hello', methods=["GET"])
def hello():
    data = request.args
    template = "fancy"
    if data != {}:
      template = data["template"]
    title = "Hello World"
    date = "October 25th"
    text = "Here is my first blog entry."
    return render_template('blogs.html', title=title, date=date, text=text, template=template)

@app.route('/bye', methods=["GET"])
def bye():
    data = request.args
    template = "default"
    if data != {}:
      template = data["template"]
    title = "Bye World"
    date = "October 25th"
    text = "Here is my last blog entry."
    return render_template('blogs.html', title=title, date=date, text=text, template=template)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)



# Access the Flask application in a web browser by visiting http://localhost:8000/ to see the "hello" message