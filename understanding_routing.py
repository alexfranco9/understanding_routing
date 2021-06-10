from flask import Flask
app = Flask(__name__)

@app.route('/') 
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<string:name>')
def say(name):
    print(name)
    return "Hi, " + name + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    print(num)
    print(word)
    return int(num) * str(word)

# BONUS!

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    return 'Sorry! No reponse. Try again.\n'

if __name__=="__main__":
    app.run(debug=True)
