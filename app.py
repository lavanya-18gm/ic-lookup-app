from flask import Flask, render_template, request
import json

app = Flask(__name__)
import os
print("Flask is using this folder:", os.getcwd())


with open('data/ic_data.json') as f:
    ic_data = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        code = request.form['ic_code'].strip().upper()
        result = ic_data.get(code)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
print("Rendering index.html from:", __file__)
