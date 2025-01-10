# from flask import Flask
# from flask import render_template # This is used to render the HTML file.
# from flask_sqlalchemy import SQLAlchemy # This is used to connect to the database.
# from datetime import datetime # This is used to get the current date and time.

# app = Flask(__name__) # This is the basic way to create a Flask app.

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # This is the database connection string.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is to suppress a warning message.

# db = SQLAlchemy(app) # This is the database object.

# # create table to store the todo list
# class Todo(db.Model): # This is the class for the database table.
#     sno = db.Column(db.Integer, primary_key=True) # This is the primary key column.
#     title = db.Column(db.String(200), nullable=False) # This is the title column.
#     desc = db.Column(db.String(500), nullable=False) # This is the description column.
#     date_created = db.Column(db.DateTime, default=datetime.utcnow) # This is the date column. utcnow is a function to get the current date and time.

# # always use this function and mention what you want to see insted of sno and title.
#     def __repr__(self): # This is the representation function.
#         return f"{self.sno} - {self.title}" # This is the representation string.

# @app.route('/')
# def home():
#     # return 'Hello, Flask!'
#     return render_template('index.html')

# @app.route('/page_1')
# def ABCD():
#     return 'Hello, this is page 01!'

# # This is the main function to run the app. 
# if __name__ == '__main__':
#     with app.app_context(): # This is to create the database table
#         db.create_all() # This is to create the database table.
#     app.run(debug=True) # we can specify the port number / change port here.


# mii
# mii
# mii


# from flask import Flask
# from flask import render_template # This is used to render the HTML file.
# from flask_sqlalchemy import SQLAlchemy # This is used to connect to the database.
# from datetime import datetime # This is used to get the current date and time.

# import sqlite3 # This is used to connect to the database.
# import os # This is used to get the current directory.
# currentdirectory = os.path.dirname(os.path.abspath(__file__)) # This is used to get the current directory where the file is located.

# app = Flask(__name__) # This is the basic way to create a Flask app.

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # This is the database connection string.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is to suppress a warning message.

# db = SQLAlchemy(app) # This is the database object.

# # create table to store the todo list
# class Todo(db.Model): # This is the class for the database table.
#     sno = db.Column(db.Integer, primary_key=True) # This is the primary key column.
#     title = db.Column(db.String(200), nullable=False) # This is the title column.
#     desc = db.Column(db.String(500), nullable=False) # This is the description column.
#     date_created = db.Column(db.DateTime, default=datetime.utcnow) # This is the date column. utcnow is a function to get the current date and time.

# # always use this function and mention what you want to see insted of sno and title.
#     def __repr__(self): # This is the representation function.
#         return f"{self.sno} - {self.title}" # This is the representation string.

# @app.route('/')
# def home():
#     # return 'Hello, Flask!'
#     return render_template('index.html')

# @app.route("/", methods = ['POST'])
# def insert():
#         title = request.form['title']
#         desc = request.form['desc']
#         connection = sqlite3.connect(currentdirectory + '/todo.db')
#         cursor = connection.cursor()
#         query1 = "INSERT INTO todo (title, desc) VALUES ('" + title + "', '" + desc + "')"
#         cursor.execute(query1)
#         connection.commit()


# @app.route('/page_1')
# def ABCD():
#     return 'Hello, this is page 01!'

# # This is the main function to run the app. 
# if __name__ == '__main__':
#     with app.app_context(): # This is to create the database table
#         db.create_all() # This is to create the database table.
#     app.run(debug=True) # we can specify the port number / change port here.




from flask import Flask
from flask import render_template # This is used to render the HTML file.
from flask_sqlalchemy import SQLAlchemy # This is used to connect to the database.
from datetime import datetime # This is used to get the current date and time.

app = Flask(__name__) # This is the basic way to create a Flask app.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # This is the database connection string.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is to suppress a warning message.

db = SQLAlchemy(app) # This is the database object.

app.app_context().push() # This is to create the database table

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

    # This is to insert the first task into the database.
    todo = Todo(title='First Task', desc='This is the first task')
    db.session.add(todo)
    db.session.commit()

    allTodo = Todo.query.all() # This is to get all the tasks from the database.

    # return 'Hello, Flask!'
    return render_template('index.html', allTodo=allTodo) # This is jinja2 and used to render the HTML file.



@app.route('/page_1')
def ABCD():
    return 'Hello, this is page 01!'

# This is the main function to run the app. 
if __name__ == '__main__':
#    with app.app_context(): # This is to create the database table
#        db.create_all() # This is to create the database table.
    app.run(debug=True,port=8000) # we can specify the port number / change port here.
