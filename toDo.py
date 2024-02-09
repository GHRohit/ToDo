from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='')

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:Mang456%40@localhost/todo'

db = SQLAlchemy(app)

class Todo(db.Model):
    date_time = datetime.now()
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    descp=db.Column(db.String(1000),nullable=False)
    date=db.Column(db.String,default=date_time.strftime("%d/%m/%y"))
    time=db.Column(db.String,default=date_time.strftime("%I:%M"))
    

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method=='POST':
            sno=len(Todo.query.all())+1
            title=request.form.get['title']
            des=request.form.get['descp']
            todo=Todo(sno = sno,title=title,descp=des)
            db.session.add(todo)
            db.session.commit()

    todo=Todo.query.all()
    return render_template('todo.html',todos=todo)

@app.route('/submit', methods=["GET", "POST"])
def func():
    if request.method=='POST':
            sno=len(Todo.query.all())+1
            title=request.form['title']
            desc=request.form['descp']
            todo=Todo(sno=sno,title=title,descp=desc)
            db.session.add(todo)
            db.session.commit()
    
    mytodo = Todo.query.all()
    return render_template('todo.html', todos=mytodo)

app.run(debug=True)