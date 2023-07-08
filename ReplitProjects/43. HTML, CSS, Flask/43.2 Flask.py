from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask number 2!'

@app.route('/home')
def home():
    page = """
    <html>
    <body>
        <h1>Welcome to the Home Page of Alex!</h1>
    </body>
    </html>
    """
    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

# Access the Flask application in a web browser by visiting http://localhost:81/ to see the "Hello from Flask!" message
# To see the HTML code returned by the home route visit http://localhost:81/home