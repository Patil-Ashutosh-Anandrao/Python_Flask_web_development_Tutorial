from flask import Flask;
from flask import render_template;

app = Flask(__name__)

@app.route('/')
def home():
    # return 'Hello, Flask!'
    return render_template('index.html')

@app.route('/page_1')
def ABCD():
    return 'Hello, this is page 01!'

if __name__ == '__main__':
    app.run(debug=True, port=8000) # we can specify the port number / change port here.



# https://www.linkedin.com/in/nageamol/
# https://www.linkedin.com/in/prashantpallati/
# https://www.linkedin.com/in/arun-salokhe-9b168296/