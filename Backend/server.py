from flask import Flask
from routes import auth

app = Flask(__name__)
app.register_blueprint(auth.sign_in)
app.register_blueprint(auth.sign_up)

@app.route("/test")
def test():
    return "Hello, World!"

if __name__ == "__main__":
    app.run("localhost", 6969)
