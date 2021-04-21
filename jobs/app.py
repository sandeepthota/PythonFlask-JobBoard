from flask import render_template, Flask

app = Flask(__name__)


@app.route('/')
@app.route('/jobs')
def jobs():
    render_template('index.html')
