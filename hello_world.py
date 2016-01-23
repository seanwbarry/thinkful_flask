from flask import Flask, render_template
from os import environ

app = Flask(__name__)
#tell the Flask application where it is being run from
@app.route("/")
def template_teset():
    return render_template('base.html',name="asdf")


@app.route("/hello")
def say_hi():
    return render_template('basic.html', name='world')

@app.route("/hello/<name>")
def hello_person(name):
    print(name)
    print('tried to print name')
    return render_template('basic.html', greeting=name)

@app.route("/jedi/<first>/<second>")
def jedi_name(first, second):
    part1 = second[:3]
    part2 = first[:2]
    return render_template('basic.html', greeting=(part1+part2))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)