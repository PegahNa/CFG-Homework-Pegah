from flask import Flask

app = Flask(__name__)
# -------------------------



@app.route('/')
def hello():
    return 'This is our Flight API'

@app.route('/flights')
def get_flights():
    return 'Not Implemented'

# -------------------------
# I wonder how this works, maybe I should youtube this later.
if __name__ == '__main__':
    # start the app, in debug mode, when the above is true
    app.run(debug=True)
    # this code going to run flask


