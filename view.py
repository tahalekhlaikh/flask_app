from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='./templates',static_folder='./templates')
def func(x):
    return x + 1


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)