import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/random")
async def random_number():
    n = random.randint(0,999)
    return n

@app.get("/nk")
async def nk_number(): 
    n = 69420
    return n 

@app.get("/rags")
async def rags_number(): 
    a ="Welcome to your mum gay.org"
    return a


