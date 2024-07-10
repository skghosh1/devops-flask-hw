from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"Welcome to the containerized flask application\"}"
if __name__== "_main_":
    helloworld.run(host="0.0.0.0", port=int("5000"),debug=True)