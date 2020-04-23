from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

# Define the index/hello_world route
@home_routes.route("/")
def hello_world():
    print("YOU VISITED THE HOMEPAGE")
    return "Hello, World!"

# Define the about route
@home_routes.route("/about")
def about():
    print("YOU VISITED THE ABOUT PAGE")
    return "About Me"
