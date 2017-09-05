from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route("/")
def hello():
	return "Hello World!"

if __name__ == '__main__':
	app.run(host = '0.0.0.0',debug = True)