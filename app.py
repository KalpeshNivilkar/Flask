from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def home():
    name = "kalpesh"
    city = "pune"
    age = 23
    return render_template("index.html",
                           name =name,
                           city = city,
                           age= age)

if __name__ == '__main__':
    app.run(debug=True)