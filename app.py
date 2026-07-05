from fastapi import FastAPI , HTTPException , Depends
from schema.pydantic_model import LoginModel , RegisterModel
from Authentication.user_authentication import user_register , user_login
from database.connection import get_db
from fastapi.responses import JSONResponse
from utility_func.password_hash import hash_password , verify_password
from sqlalchemy.ext.asyncio import AsyncSession



app = FastAPI()


    
   


@app.post("/register")
async def register(data : RegisterModel , db : AsyncSession=Depends(get_db)):

    user_data = data.model_dump(exclude=["re_password"])

    user_data["password"] = hash_password(user_data["password"])


    result =await user_register(user_data  , db=db)

    if result["status"] =="success" :

        return JSONResponse(status_code=201, content={"message" : result["message"]})
    
    raise HTTPException(status_code=400, detail=result["message"])





@app.post("/login")
async def login(data :LoginModel, db : AsyncSession = Depends(get_db)):

    try :

        user_data =  await user_login(data.email , db=db)

    except Exception as e :

        raise HTTPException(status_code=500, detail="Database connection failed")

    if user_data["status"] == "success":

        user_metadata= user_data["data"]

        if verify_password(data.password,user_metadata["password"]) :

            payload = {
                "id": user_metadata["id"],
                "email" : user_metadata["email"],
                "district" : user_metadata["district"]
            }

            return JSONResponse(status_code=200, content={"message": user_data["message"],"payload":payload})
        
    raise HTTPException(status_code=401 , detail="Invalid email or password")


