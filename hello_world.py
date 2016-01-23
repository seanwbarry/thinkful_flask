from flask import Flask
from os import environ

app = Flask(__name__)
#tell the Flask application where it is being run from
#@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

#only one of the below functions will run - why is that???

"""
@app.route("/hello/<name>")    
def hi_person(name):
    return "Hello {}!".format(name.title())
"""
@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    print(__name__.split(".")[0])
    print('next')
    #print(__name__.split(".")[1])
    #print('next')
    print(__name__.split(".")[-1])
    print('next')
    return html.format(name.title())
    
@app.route("/jedi/<first>/<second>")
def jedi_name(first, second):
    part1 = second[:3]
    part2 = first[:2]
    html = """
        <h1>
            Hello {}{}!
        </h1>
    """
    return html.format(part1,part2)
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))