from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Arman New AI"

@app.route('/route1')
def route1():
    return "This is excuted from route1 functions"

def route2():
    return "This is executed from route2"

app.add_url_rule('/route2', 'route2', route2)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)