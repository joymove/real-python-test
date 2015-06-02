from flask import Flask

# Create the application object
app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return "hello, world!"

if __name__ == "__main__":
    app.run()
