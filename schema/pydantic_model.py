from pydantic import BaseModel , Field , EmailStr , model_validator
from typing import Annotated


class LoginModel(BaseModel):
    email : EmailStr = Field(...,description="Enter Registerd Email", examples=["abc@gmail.com"])
    password : Annotated[str, Field(...,max_length=30, min_length=8, description="please enter password")]


class RegisterModel(BaseModel):
    name : Annotated[str,Field(..., description="enter user's name",examples=["John"])]
    email : EmailStr = Field(...,description="Enter Registerd Email", examples=["abc@gmail.com"])
    district :  Annotated[str,Field(..., description="enter user's city",examples=["Mumbai"])]
    land_in_hectors:  Annotated[float,Field(..., description="enter lands in hectors",examples=["12.44"])]
    password: Annotated[str,Field(...,max_length=30,min_length=8,description="enter new password ")]
    re_password : Annotated[str,Field(...,max_length=30,min_length=8, description="re-enter the new password")]

    @model_validator(mode="after")
    def check_password(self):
        if self.password != self.re_password:
            raise ValueError("Both new password and re enter password must be same ")
        return self
