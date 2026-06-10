"""Starter code for Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {"id": 1, "title": "Read the FastAPI docs", "completed": False},
    {"id": 2, "title": "Build first endpoint", "completed": True},
]


@app.get("/")
def health_check():
    return {"message": "Welcome to the Task Manager API"}


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskInput):
    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {"id": new_id, **payload.model_dump()}
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskInput):
    for task in tasks:
        if task["id"] == task_id:
            task.update(payload.model_dump())
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(index)
            return {"deleted": removed}
    raise HTTPException(status_code=404, detail="Task not found")
