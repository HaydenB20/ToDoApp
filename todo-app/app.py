from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if not task:
        return redirect(url_for('index', error="Task cannot be empty"))
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    else:
        return redirect(url_for('index', error="Invalid task ID"))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)