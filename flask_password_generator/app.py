from flask import Flask, render_template,request
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    lst = []
    for i in range(length):
        ch = random.choice(characters)
        lst.append(ch)
    random_password = ''.join(lst)
    return random_password

@app.route('/', methods=['GET']) 
def index(): 
    return render_template('index.html') 

@app.route('/password', methods=['POST']) 
def password(): 
    length = int(request.form['length']) 
    password = generate_password(length) 
    return render_template('index.html', password=password) 

@app.route('/both', methods=['GET','POST'])
def both():
    if request.method == 'POST':
        length = int(request.form['length']) 
        password = generate_password(length) 
        return render_template('both.html', password=password) 
    else:
        return render_template('both.html') 
    
@app.route('/req')
def req():
    return '%s'%request.headers


if __name__ == '__main__':
    app.run(debug=True)
