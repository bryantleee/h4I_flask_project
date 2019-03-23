from flask import Flask, render_template, url_for, session
app = Flask(__name__)

from models import todo

ENTRY_POINT = ""

@app.route(ENTRY_POINT + '/', methods=['GET'])
def index():
  incompleted = db.session.query(todo).filter_by(completed=0).all()
  completed = db.session.query(todo).filter_by(completed=1).all()
  return render_template('index.html', incomplete_tasks=incompleted, completed_tasks=completed)

@app.route('/settings')
def settings():
  return render_template('settings.html')

@app.route('/todo/<name_of_task>')
def showTask(task_id):
  query = "SELECT * FROM tasks WHERE completed = 0 AND task_id =" + task_id + ";"

def todo():




  return render_template('todo.html')


@app.route('/completed/<name_of_task>')
def completed():
    return render_template('completed.html')


if __name__ == "__main__":
    app.run(debug=True)




