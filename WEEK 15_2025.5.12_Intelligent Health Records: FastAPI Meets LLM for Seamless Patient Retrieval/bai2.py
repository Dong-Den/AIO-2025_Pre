#
# API máy tính
from fastapi import FastAPI
from fastapi import HTTPException

app=FastAPI()

@app.get("/add")
async def add(a: int, b: int):
    return a+b

@app.get("/subtract")
async def subtract(a: int, b: int):
    return a-b

@app.get("/multiply")
async def multiply(a: int, b:int):
    return a*b

@app.get("/divide")
async def divide(a: int, b:int):
    if b==0:
        raise HTTPException(status_code=400, detail="không thể chia cho 0")
    return a/b

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
    
 