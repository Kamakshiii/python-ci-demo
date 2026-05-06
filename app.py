from  flask import Flask
app = Flask(__name__)
def add(a, b):
    return a + b
@app.route("/")
def home():
    return ("hello DevOps")
@app.route("/test")
def test():
    return "This is test route"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


