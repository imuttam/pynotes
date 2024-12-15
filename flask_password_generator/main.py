from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pwd = db.Column(db.String(100))
    account = db.Column(db.String(50))

    def __repr__(self):
        return f'Password: {self.account}'



@app.route('/')
def indexdb():
    return render_template('index_db.html')

@app.route('/add', methods=['POST'])
def add_password():
    account = request.form['account']
    pwd = request.form['pwd']
    
    # Create a new Password object and add it to the database
    new_password = Password(account=account, pwd=pwd)
    db.session.add(new_password)
    db.session.commit()

    return redirect(url_for('indexdb'))

if __name__ == '__main__':
    app.run(debug=True)


#py shell prompt

#from app import db,Password
# app.app_context().push()
#db.create_all()
#Password.query.all()
