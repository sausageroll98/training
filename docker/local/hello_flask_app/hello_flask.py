import waitress
from flask import Flask
import os
app = Flask(__name__)
hostname = os.environ['HOSTNAME']
@app.route('/', methods=['GET'])
def index():
    return f"Hello Flask from inside Docker container id {hostname}"
