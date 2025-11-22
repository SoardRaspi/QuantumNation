from flask import Flask

# Create an instance of the Flask class.
# __name__ is a shortcut for the module's name,
# which Flask uses to locate resources like templates.
app = Flask(__name__)

# The route() decorator tells Flask what URL should trigger the function.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# This ensures the Flask application runs only when the script is executed directly.
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables debug mode, useful for development