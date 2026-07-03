from fastapi import FastAPI , HTTPException
from schema.pydantic_model import LoginModel


app = FastAPI()


@app.post("/login")
def login(data :LoginModel):
    
    if data.email=="prem@gmail.com" and data.password=="12345678":
        return {"status" : "success", "message":"success fully logged in"}
    
    else:
        raise HTTPException(status_code=400, detail="wrong password or email plese re enter")

    