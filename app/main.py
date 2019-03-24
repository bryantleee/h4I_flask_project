from flask import Flask, render_template, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from init_db import Tasks

Base = declarative_base()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

engine = create_engine('sqlite:///tasks.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

ENTRY_POINT = ""

@app.route(ENTRY_POINT + '/', methods=['GET'])
def index():
  incompleted = session.query(Tasks).filter_by(completed=0).all()
  completed = session.query(Tasks).filter_by(completed=1).all()
  return render_template('index.html', incomplete_tasks=incompleted, completed_tasks=completed)

@app.route('/settings')
def settings():
  return render_template('settings.html')

@app.route('/todo/<name_of_task>', methods=['POST'])
def showTask(task_id):
  task = session.query(Tasks).filter_by(id=task_id)
  return render_template('task.html', task=task)

@app.route('/completed/<name_of_task>')
def completed(task_id):
  task = session.query(Tasks).filter_by(id=task_id)
  return render_template('completed.html', task=task)

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port = 8000)




