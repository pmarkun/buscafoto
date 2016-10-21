from flask import Flask
from urllib2 import urlopen
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/<tag>")
def hello(tag):
    url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyBXD0uxwA6BDsyJ-23F4GayFYYZVL3-LQo&cx=012056724307537808486:0k_cvmulyz0&searchType=image&q="
    soup = urlopen(url+tag)
    return soup.read()

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')