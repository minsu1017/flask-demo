import yaml
from flask import Flask, render_template
app = Flask(__name__)

CONFIG_PATH = './flask.conf'

@app.route("/")
def hello():
    conf = loadConfig()
    title = conf['global']['title']
    host = conf['global']['host']
    return render_template("index.html", title=title, host=host)
    
def loadConfig():
    with open(CONFIG_PATH, 'r') as f:
        return yaml.load(f)
