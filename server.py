from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Make sure you have a templates/index.html file

if __name__ == '__main__':
    app.run(debug=True)