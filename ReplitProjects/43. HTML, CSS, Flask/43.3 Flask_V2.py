from flask import Flask
import datetime

app = Flask(__name__) # Starts the Flask application. The 'app' variable is very important.


@app.route('/') # Tells the code what to do if we've gone to our web address with just a / after the URL
def index():
    page = """
    <html>
    <body>
        <p><a href="/home">Go home</a></p>
    </body>
    </html>
    """
    return page

@app.route('/home') # Creates the path to the home page
def home(): # Subroutine to create the home page
  # Three quotes followed by the html for the baldies site. Three more quotes to close. All the HTML is assigned to the 'page' variable
  today = datetime.date.today()
  page = f"""
  
  <html>
    
  <head>
    <title>David's World Of Baldies</title>
  </head>

  <body>
  <p><a href="/portfolio">Go portfolio</a></p>
  <h1>Dave's World of Baldies</h1> 
  <h2>Welcome to our website!</h2>
  <h2>{today}</h2>

  <p>We all know that throughout history some of the greatest have been Baldies, let's see the epicness of their heads bereft of hair.</p>

  <h2>Gallery of Baldies</h2>
  <p>Here are some of the legends of the bald world.</p>

  <img src="images/picard.jpg" width = 30%, alt = "Photo of Picard"> 
  <p><a href = "https://memory-alpha.fandom.com/wiki/Star_Trek:_Picard">Captain Jean Luc Picard: Baldest Star Trek captain, and legend.</a></p>

  <ul>
    <li>Beautiful bald man</li>
    <li>Calm and cool under pressure</li>
    <li>All the Picard memes</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>
  
</body>
  
</html>
  
  """
  return page # returns the contents of the page variable

@app.route('/portfolio')
def portfolio():
   page = f"""
   <!DOCTYPE html>

   <html>
   <head>
    <meta charset = "utf-8">
    <meta name = "viewport" content = "width=device-width">
    <title>My Portfolio</title>
    <link href = "style.css" rel = "stylesheet"/>
   </head>
   <body>
   <p><a href="/home">Go home</a></p>
   <h1>My Portfolio</h1>
   </body>

   </html>

   """

   return page


app.run(host='0.0.0.0', port=4050) # This line should ALWAYS come last. It's the line that turns on the Flask server.

# Access the Flask application in a web browser by visiting http://localhost:4050/ to see the "Hello from Flask!" message
# To see the HTML code returned by the home route visit http://localhost:4050/home
# To see the portfolio page visit http://localhost:4050/portfolio