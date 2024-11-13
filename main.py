from fastapi import FastAPI
from models import Todo

app = FastAPI()
todo = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

#get todo
@app.get("/todo")
async def get_todos():
    return {"todo": todo}

# create todo
@app.post("/todo")
async def create_todo(todos: Todo):
    todo.append(todos)
    return {"message": "This message has been added"}

# single todo
@app.get("/todo/{todo_id}")
async def get_todo(todo_id: int):
    for x in todo:
        if x.id == todo_id:
            return  {"todo": todo}
    return {"message": "Not founded"}

#Delete todo
@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for x in todo:
        if x.id == todo_id:
            todo.remove(x)
            return  {"message": "DELETE"}
    return {"message": "Not founded"}

#update todo
@app.put("/todo/{todo_id}")
async def update_todo(todo_id: int, todos:Todo):
    for x in todo:
        if x.id == todo_id:
            x_id = todo_id
            x.item = todos.item
            return  {"todo": todo}
    return {"message": "Not founded"}