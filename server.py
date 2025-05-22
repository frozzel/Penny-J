from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pennyj.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Make sure you have a templates/index.html file

if __name__ == '__main__':
    app.run(debug=True)