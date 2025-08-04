from flask import Flask, render_template, request
import os
import json

os.environ['FLASK_ENV'] = 'development'
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True

app = Flask(__name__)

# Load IC data
with open('data/ic_data.json', 'r') as f:
    ic_data = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        code = request.form['ic_code'].lower()
        result = ic_data.get(code)
    return render_template('index.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
