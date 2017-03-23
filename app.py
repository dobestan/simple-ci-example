import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"


@app.route("/about/")
def about():
	return "This is about page"

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
