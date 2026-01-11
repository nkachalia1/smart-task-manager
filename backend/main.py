from fastapi import FastAPI
from datetime import date
from models import Task
from storage import tasks, task_map
from structures.stack import Stack

app = FastAPI()
undo_stack = Stack()

@app.post("/tasks")
def add_task(title: str, priority: int, due_date: date):
    task = Task(len(tasks)+1, title, priority, due_date)
    tasks.append(task)
    task_map[task.id] = task
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = task_map.pop(task_id, None)
    if task:
        undo_stack.push(task)
        tasks.remove(task)
    return {"status": "deleted"}

@app.post("/undo")
def undo():
    task = undo_stack.pop()
    if task:
        tasks.append(task)
        task_map[task.id] = task
    return {"status": "undone"}
