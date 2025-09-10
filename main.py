from fastapi import FastAPI

app = FastAPI()


@app.get("/World")
async def root():
    return {"message": "Salom FastAPI !"}

@app.get("/fikr")
async def root():
    return {"message": "FastAPI juda zo‘r framework!"}

@app.get("/ism ")
async def root():
    return {"message": "Mening ismim <..>"}

@app.get("/yosh")
async def root():
    return {"message": "Mening yoshim <..>"}  

@app.get("/fanlar")
async def root():
    return {"message": ""} 

@app.get("/talaba")
async def root():
    return {"message": ""} 

@app.get("/tasodifiy-son")
async def root():
    return {"message": ""} 

@app.get("/tasodifiy-fan")
async def root():
    return {"message": ""} 

@app.get("/tasodifiy-talaba")
async def root():
    return {"message": ""} 
