from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default=False)

    def __repr__(self):
        return f'Task(name={self.name}, date={self.date}, status={self.status})'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_task():
    name = request.form['name']
    date  =   request.form['date']
    status =  request.form.get('status')

    date = datetime.fromisoformat(date)
    
    # try:
    #     # Parse the ISO-8601 date string to a Python datetime object
    #     date = datetime.fromisoformat(date)  
    # except ValueError:
    #     # Handle invalid date formats gracefully
    #     return "Invalid date format", 400
    
    new_task = Task(name=name, date=date, status=status)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('view'))

@app.route('/view', methods=['GET'])
def view():
    # Retrieve all data from the Password table
    tasks = Task.query.all()
    return render_template('view.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)


#py shell prompt

#from app import db,Password
# app.app_context().push()
#db.create_all()
#Password.query.all()
