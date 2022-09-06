from enum import Enum
from fastapi import FastAPI

app_handle=FastAPI()

@app_handle.get('/')
async def root():
    return {"message": "Hello World"}

# Dynamic route
@app_handle.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app_handle.get("/users/me")
async def read_user_me():
    return {'user_id': 'the current user'}

@app_handle.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": f"Hi, {user_id} user, welcome !"}

# Predefined path parameters value

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet="resnet"
    lenet="lenet"

@app_handle.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning FTW"}
    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN algorithm"}
    
    return {"model_name": model_name, "message":"Have some models"}


@app_handle.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}