from pydantic import BaseModel , Field , EmailStr
from typing import Annotated


class LoginModel(BaseModel):
    email : EmailStr = Field(...,description="Enter Registerd Email", examples=["abc@gmail.com"])
    password : Annotated[str, Field(...,max_length=30, min_length=8, description="please enter password")]



