from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def home():
    courses = ["python","css", "html"]
    
    return render_template("index.html",
                           courses= courses)
    

if __name__ == '__main__':
    app.run(debug=True)