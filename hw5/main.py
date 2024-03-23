from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class StatusTask(Enum):
    completed = 'Выполнена'
    not_completed = 'Не выполнена'


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: StatusTask


app = FastAPI()

tasks = []


@app.get('/')
async def index():
    return {'hello': 'Hello'}


@app.get('/tasks/')
async def get_tasks():
    return {'tasks': tasks}


@app.get('/tasks/{task_id}')
async def get_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            return {'task': tasks[i]}


@app.post('/tasks')
async def create(task: Task):
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}')
async def edit_task(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            tasks[i] = task
    return {'task': task}


@app.delete('/tasks/{task_id}')
async def del_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
    return {'task_id': task_id}