from flask import Flask, render_template
app = Flask(__name__)

# http://127.0.0.1:5000

#task 1
@app.route('/')
def success():
  return "Hello World!"

#task 2
@app.route('/dojo')
def dojo():
  return "Dojo!"

#task 3
@app.route('/say/<name>')
def hi_name(name):
  return f"Hi {name}!"

#task 4
@app.route('/repeat/<int:number>/<text>')
def number_text(number, text):
    return render_template('index.html', number=number, text=text)

#NINJA Bonus 1
@app.route('/say/<string:name>')
def ninja_1(name):
    return f"Hi {name}!"

#NINJA Bonus 2
@app.route('/repeat/<int:number>/<string:text>')
def ninja_2(number, text):
    return render_template('index.html', number=number, text=text)

if __name__=="__main__":
    app.run(debug=True)