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



##mii
##mii
##mii
##mii
##mii



from flask import Flask
from flask import request # This is used to get the form data.
from flask import render_template # This is used to render the HTML file.
from flask import redirect # This is used to redirect to another page.
from flask_sqlalchemy import SQLAlchemy # This is used to connect to the database.
from datetime import datetime # This is used to get the current date and time.
import os # This is used to get the current directory.
from datetime import timedelta, date # This is used to get the next 7 days and the current date.
import sqlite3 # This is used to connect to the database.
from flask import url_for # This is used to get the URL.
from sqlalchemy import and_ # This is used to get the tasks between two dates.

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
    date_created = db.Column(db.Date, default=date.today) # This is the date column. utcnow is a function to get the current date and time.
    final_date = db.Column(db.String(10), nullable=False)



# always use this function and mention what you want to see insted of sno and title.
    def __repr__(self): # This is the representation function.
        return f"{self.sno} - {self.title} - {self.final_date}" # This is the representation string.






@app.route('/', methods=['GET', 'POST'])
# This is the home route. methods is used to get the form data.

def home():
    current_date = datetime.now().strftime("%Y-%m-%d") # This is to get the current date and time.
    if request.method == 'POST': # This is to check if the form is submitted.
        title = request.form['title'] # This is to get the title from the form.
        desc = request.form['desc'] 
        final_date = request.form['final_date']
        todo = Todo(title=title, desc=desc,final_date=final_date) # This is to create a new task.
        db.session.add(todo) # This is to add the task to the database.
        db.session.commit() # This is to commit the task to the database.

    # This is to insert the first task into the database.
    # todo = Todo(title='First Task', desc='This is the first task')
    # db.session.add(todo)
    # db.session.commit()

    allTodo = Todo.query.filter(Todo.final_date <= current_date).all() # This is to get all the tasks from the database.

    # return 'Hello, Flask!'
    return render_template('index.html', allTodo=allTodo, current_date=current_date, ) # This is jinja2 and used to render the HTML file.






@app.route("/weekly",methods=['GET', 'POST'])
def weekly():
    # if request.method == 'POST': # This is to check if the form is submitted.
    #     title = request.form['title'] # This is to get the title from the form.
    #     desc = request.form['desc']

    #     todo = Todo.query.filter_by(sno=sno).first()
    #     todo = Todo(title=title, desc=desc) # This is to create a new task.
    #     db.session.add(todo) # This is to add the task to the database.
    #     db.session.commit() # This is to commit the task to the database.

    # Generate a list of dates from today to the next 7 days
    today = datetime.now().strftime("%B %d, %Y") # This is to get the current date and time.
    date_after_7_days = (datetime.now() + timedelta(days=7)).strftime("%B %d, %Y")

    allTodo = Todo.query.filter(Todo.final_date <= today).all() # This is to get all the tasks from the database.
    
    #allTodo = Todo.query.filter(Todo.final_date.between(today, date_after_7_days)).all()
    #allTodo = Todo.query.all() # This is to get all the tasks from the database.

    # allTodo = Todo.query.filter(
    #     and_(
    #         Todo.final_date >= today,
    #         Todo.final_date <= date_after_7_days
    #     )
    # ).all()


    return render_template('weekly.html', today=today,date_after_7_days=date_after_7_days, allTodo=allTodo) # This is jinja2 and used to render the HTML file.







@app.route("/monthly",methods=['GET', 'POST'])
def monthly():
    # if request.method == 'POST': # This is to check if the form is submitted.
    #     title = request.form['title'] # This is to get the title from the form.
    #     desc = request.form['desc']

    #     todo = Todo.query.filter_by(sno=sno).first()
    #     todo = Todo(title=title, desc=desc) # This is to create a new task.
    #     db.session.add(todo) # This is to add the task to the database.
    #     db.session.commit() # This is to commit the task to the database.

    # Generate a list of dates from today to the next 7 days
    today = datetime.now().strftime("%B %d, %Y") # This is to get the current date and time.
    date_after_30_days = (datetime.now() + timedelta(days=30)).strftime("%B %d, %Y")

    # allTodo = Todo.query.all() # This is to get all the tasks from the database.

    allTodo = Todo.query.filter(
        and_(
            Todo.final_date >= today,
            Todo.final_date <= date_after_30_days
        )
    ).all()

    return render_template('monthly.html', today=today,date_after_30_days=date_after_30_days, allTodo=allTodo) # This is jinja2 and used to render the HTML file.






@app.route('/update/<int:sno>', methods=['GET','POST']) # <int:sno> is used to get the sno from the URL and /update/ is the route which is used to update the task.
def update(sno):
    if request.method == 'POST':    # This is to check if the form is submitted.
        title = request.form['title'] # This is to get the title from the form.
        desc = request.form['desc']
        final_date = request.form['final_date']

        todo = Todo.query.filter_by(sno=sno).first() # This is to get the task from the database. first() is used to get the first task.
        todo.title = title # This is to update the title of the task.
        todo.desc = desc 
        todo.final_date = final_date

        db.session.add(todo) # This is to add the task to the database.
        db.session.commit()

        return redirect("/") # This is to redirect to the home page.


    todo = Todo.query.filter_by(sno=sno).first() # This is to get the task from the database. first() is used to get the first task.
    return render_template('update.html', todo=todo) # This is jinja2 and used to render the HTML file.

    # allToday = Todo.query.all() # This is to get all the tasks from the database.
    # print(allToday) # This is to print all the tasks.
    # return 'This is the update page!'



@app.route('/delete/<int:sno>') # <int:sno> is used to get the sno from the URL.
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first() # This is to get the task from the database. first() is used to get the first task.
    # allToday = Todo.query.all() # This is to get all the tasks from the database.
    db.session.delete(todo) # This is to delete the task from the database.
    db.session.commit()
    return redirect('/') # This is to redirect to the home page.

    # print(allToday) 
    # return 'This is the delete page!'


@app.route('/page_1')
def ABCD():
    return 'Hello, this is page 01!'

# This is the main function to run the app. 
if __name__ == '__main__':
#    with app.app_context(): # This is to create the database table
#        db.create_all() # This is to create the database table.
    app.run(debug=True,port=8000) # we can specify the port number / change port here.
