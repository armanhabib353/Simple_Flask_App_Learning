from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is Home Page"


#variable rules
@app.route('/<name>')
def variable(name):
    return "This is variable {}".format(name)


#integer value
@app.route('/blog/<int:blogid>')
def blog(blogid):
    return "this is blog id in integer {}".format(blogid)

# Float value
@app.route('/weight/<float:w>')
def weight(w):
    return "Your Weight is %s"%w



if __name__ == "__main__":
    app.run(debug=True)