"""Greeting Flask app."""

# from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    # """
    return """
    <!doctype html>
    <html>
      <head>
        <title>hi! this is the home page</title>
      </head>
      <body>
      
        <h1>Hi! This is the home page.</h1>
        <a href= "/hello">click me</a>
       
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
      
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          take your pick? <br> <br> 
          <input type='radio' name='complement' value = "awesome">  awesome <br>
          <input type='radio' name='complement' value='terrific'> terrific  <br>
          <input type='radio' name='complement' value='terrific'> terrific  <br>
          <input type='radio' name='complement' value='fantastic'> fantastic  <br>
          <input type='radio' name='complement' value='neato'> neato  <br>
          <input type='radio' name='complement' value='fantabulos'> fantabulous  <br>
          <input type='radio' name='complement' value='wowza'> wowza  <br>
          <input type='radio' name='complement' value='oh-so-not-meh'> oh-so-not-meh  <br>
          <input type='radio' name='complement' value='brilliant'> brilliant  <br>
          <input type='radio' name='complement' value='ducky'> ducky  <br>
          <input type='radio' name='complement' value='coolio'> coolio  <br>
          <input type='radio' name='complement' value='incredible'> incredible  <br>
          <input type='radio' name='complement' value='wonderful'> wonderful  <br>
          <input type='radio' name='complement' value='smashing'> smashing <br>
          <input type='radio' name='complement' value='lovely'> lovely <br>

          <br>
           <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet', methods=["GET"])
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("complement")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0", port=5001)
