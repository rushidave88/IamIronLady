from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

todos = {}
next_id = 1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()
    task_text = data.get('task', '')
    if not task_text:
        return jsonify({"error": "Task content is required"}), 400
    task = {"id": next_id, "task": task_text, "done": False}
    todos[next_id] = task
    next_id += 1
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(list(todos.values()))

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id not in todos:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    todos[task_id]["task"] = data.get("task", todos[task_id]["task"])
    todos[task_id]["done"] = data.get("done", todos[task_id]["done"])
    return jsonify(todos[task_id])

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in todos:
        return jsonify({"error": "Task not found"}), 404
    deleted_task = todos.pop(task_id)
    return jsonify(deleted_task)

if __name__ == "__main__":
    app.run(debug=True)
