from flask import Flask, render_template
from routes.conversions import conversions

app = Flask(__name__)
app.register_blueprint(conversions)

@app.route('/', methods = ['GET'])
def index():
    return(render_template('index.html'))