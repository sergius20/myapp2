from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    message = "Hola Mundo, soy Python! Ahora con CloudBuild y hablando con JSON (Soy Sergio)"
    response = {
            "message": message,
            "length": len(message)
            }
    return jsonify(response)
@app.route('/bye')
def bye_world():
    return ("Adiós mundo cruel")

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
