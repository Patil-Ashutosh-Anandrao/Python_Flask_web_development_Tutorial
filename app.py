from flask import Flask;
from flask import render_template; # This is used to render the HTML file.
from flask_sqlalchemy import SQLAlchemy; # This is used to connect to the database.
from datetime import datetime; # This is used to get the current date and time.

app = Flask(__name__) # This is the basic way to create a Flask app.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # This is the database connection string.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is to suppress a warning message.

db = SQLAlchemy(app) # This is the database object.

# create table to store the todo list
class Todo(db.Model): # This is the class for the database table.
    sno = db.Column(db.Integer, primary_key=True) # This is the primary key column.
    title = db.Column(db.String(200), nullable=False) # This is the title column.
    desc = db.Column(db.String(500), nullable=False) # This is the description column.
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # This is the date column. utcnow is a function to get the current date and time.

# always use this function and mention what you want to see insted of sno and title.
    def __repr__(self): # This is the representation function.
        return f"{self.sno} - {self.title}" # This is the representation string.

@app.route('/')
def home():
    # return 'Hello, Flask!'
    return render_template('index.html')

@app.route('/page_1')
def ABCD():
    return 'Hello, this is page 01!'

# This is the main function to run the app. 
if __name__ == '__main__':
    with app.app_context(): # This is to create the database table
        db.create_all() # This is to create the database table.
    app.run(debug=True) # we can specify the port number / change port here.
