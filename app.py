from fastapi import FastAPI , HTTPException , Depends
from fastapi.responses import JSONResponse
from fastapi.concurrency import run_in_threadpool
from sqlalchemy.ext.asyncio import AsyncSession
from Schema.pydantic_model import LoginModel , RegisterModel , CropRecommendModel
from Authentication.user_authentication import user_register , user_login
from Authentication.json_token import create_token , token_decoder
from Database.connection import get_db
from Utility_func.password_hash import hash_password , verify_password
from Model.prediction_function import crop_recommendation





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

    DUMMY_BCRYPT_HASH = "$2b$12$KbN3r4Yf1rUas3P8q0H9O.fV8p0Kz1e0Z0Z0Z0Z0Z0Z0Z0Z0Z0Z0Z"

    user_data =  await user_login(data.email , db=db)

    if user_data.get("status")=="failed" and "Internal database error" in user_data.get("message") :

        raise HTTPException(status_code=500, detail=user_data.get("message"))
    
    if user_data.get("status") == "success":

        user_metadata= user_data.get("data")

        if verify_password(data.password,user_metadata.get("password")) :

            payload = {
                "id": user_metadata.get("id"),
                "email" : user_metadata.get("email"),
                "district" : user_metadata.get("district")
            }

            access_token = create_token(payload)

            return JSONResponse(status_code=200, content={"message": user_data.get("message"),"access_token":access_token})
        
    else: 
        verify_password(data.password,DUMMY_BCRYPT_HASH)
        
    
        
    raise HTTPException(status_code=401 , detail="Invalid email or password")


@app.post("/predict/Crop_recommendation")
async def prediction(raw_features: CropRecommendModel):

    features=raw_features.model_dump()

    result = await run_in_threadpool(crop_recommendation, features)

    if result.get("status") == "success" :

        return JSONResponse(status_code=200, content={"message":result.get("message"), "predicted_output" : result.get("data")})
    
    else :
        
        print(result.get("message"))

        raise HTTPException(status_code=500 , detail=f"Internal Machine Learning Model Error")






