from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View canvas."""

    return render_template('canvas.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
