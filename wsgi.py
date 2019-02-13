# application.py
from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy



application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    application.run()
