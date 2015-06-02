from flask import Flask

# Create the application object
app = Flask(__name__)

# Error handling
app.config["DEBUG"] = True
@app.route("/")
@app.route("/hello")
def hello_world():
    return "hello, world!?!?!?!?!"

# Dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    #print value + 1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"

# Dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"
    
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()
