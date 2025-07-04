from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():
    return {"message":"Hello Prajjwal!"}


@app.get("/second-api-endpoint")
async def second_api():
    return {"message":"This is second api endpoint"}