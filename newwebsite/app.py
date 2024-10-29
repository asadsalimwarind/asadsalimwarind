from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index2.html")

@app.route('/sports')
def sport():
    return render_template("sports.html")

@app.route('/skl')
def skl():
    return render_template("skl.html")

@app.route('/projects')
def proj():
    return render_template("projects.html")

@app.route('/projects/arduino')
def arduino():
    return render_template("arduino.html")

@app.route('/projects/application')
def application():
    return render_template("application.html")

@app.route('/projects/planning')
def planning():
    return render_template("planning.html")

@app.route('/honors')
def honors():
    return render_template("honors.html")

@app.route('/rand')
def rand():
    return render_template("rand.html")





if __name__ == '__main__':
    app.run(debug=True)