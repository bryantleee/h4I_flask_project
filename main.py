from flask import Flask, render_template, url_for
app = Flask(__name__)

ENTRY_POINT = ""

@app.route(ENTRY_POINT + '/', methods=['GET'])
def index():
  return render_template('index.html')



@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/todo <name_of_task>')
def todo():
    return render_template('todo.html')


@app.route('/completed <name_of_task>')
def completed():
    return render_template('completed.html')


if __name__ == "__main__":
    app.run(debug=True)




