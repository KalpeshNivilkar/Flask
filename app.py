from flask import Flask, request
from uuid import UUID

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Home page '

# static route
'''@app.route('/about')
def about():
    return "This is about page"

@app.route('/contact us')
def contact_us():
    return "This is contact page"'''

'''# dynamic route
@app.route('/users/<name>')
def users_name(name):
    return f"Welcome {name}"'''

'''# multi-parameter dynamic routing
@app.route('/student/<name>/<course>')
def student_info(name,course):
    return f"the {name} is learning {course}"'''

# URL convertor 
# int convertor
'''@app.route('/product/<int:id>')
def product(id):
    return f"product id is: {id}"

# float convertor
@app.route('/price/<float:amount>')
def price(amount):
    return f"the product amount is {amount}"

# string convertor
@app.route('/student/<string:name>')
def student(name):
    return f"the name of staudent is {name}"

# path
@app.route('/website/<path:file_path>')
def website_link(file_path):
    return f"th file path is :{file_path}"

#  UUID
@app.route('/unique/<uuid:user_id>')
def unique(user_id):
    return f"this is unique id:{user_id}"'''

# Query parameter
@app.route('/search')
def search():
    name = request.args.get("name","geust")
    return f"hello {name}"

# multiple query parameters
@app.route('/multiple')
def multiple():
    name = request.args.get("name","guest")
    course = request.args.get("course", "unknown")
    return f"{name} is learning {course}"

if __name__ == '__main__':
    app.run(debug=True)