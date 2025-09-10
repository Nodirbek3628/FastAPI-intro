from fastapi import FastAPI
from random import randint,choice


app = FastAPI()


@app.get("/World")
async def root():
    return {"message": "Salom FastAPI !"}


@app.get("/fikr")
async def fikr():
    return {"message": "FastAPI juda zo‘r framework!"}


@app.get("/ism ")
async def name():
    return {"message": "Mening ismim Nodirbek"}


@app.get("/yosh")
async def age():
    return {"message": "Mening yoshim 20 da "}  


@app.get("/fanlar")
async def sciences():
    return ["Matematika", "Fizika", "Ingliz tili"]

@app.get("/talaba")
async def student():
    return {
  "ism": "Ali",
  "yosh": 20
}

@app.get("/tasodifiy-son")
async def random_son():
    n = randint(1,100)

    return {
        "son": n
    }

@app.get("/tasodifiy-fan")
async def random_science():
    sciences = ["Matematika", "Fizika", "Ingliz tili", "Tarix", "Biologiya"]
    fan = choice(sciences)

    return {
        "fan": fan
    }

@app.get("/tasodifiy-talaba")
async def random_student():
    students  = [{
        "name": "ALi",
        "yosh": 20
    },
    {
         "name": "Vali",
        "yosh": 22
    },
    {
         "name": "John",
        "yosh": 25
    },
    {
         "name": "Dinara",
        "yosh": 18
    }
    ]

    random_student = choice(students)

    return random_student
