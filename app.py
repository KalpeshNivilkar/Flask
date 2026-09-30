from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello My World '

@app.route('/about')
def about():
    return "This is about page"

@app.route('/contact us')
def contact_us():
    return "This is contact page"

if __name__ == '__main__':
    app.run(debug=True)