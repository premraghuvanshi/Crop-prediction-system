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


class CropRecommendModel(BaseModel):
    
    N: Annotated[float, Field(...,ge=0, description='Nitrogen level in soil', examples=[90])]
    P: Annotated[float, Field(...,ge=0, description='Phosphorus level in soil', examples=[42])]
    K: Annotated[float, Field(...,ge=0, description='Potassium level in soil', examples=[43])]
    temperature : Annotated[float, Field(...,ge=0, description='tempreture in Celcius', examples=[20])]
    humidity : Annotated[float, Field(...,ge=0, description='humidity percentage', examples=[82])]
    ph : Annotated[float, Field(...,ge=0, description='ph level of soil', examples=[6.5])]
    rainfall : Annotated[float, Field(..., ge=0, description='Rainfall in mm', examples=[202])]