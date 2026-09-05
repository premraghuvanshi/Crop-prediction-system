from pydantic import BaseModel , Field , EmailStr , model_validator , field_validator
from typing import Annotated , Literal


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


class PredictedOutput(BaseModel):
    prediction : Annotated[str, Field(..., description="predicted crop")]
    confidence : Annotated[float , Field(..., ge=0 , le=100 , description="confidence of the prediction")]

    @field_validator('prediction')
    @classmethod
    def transform_crop_name(cls, value):
        return value.title()

class CropPredicted(BaseModel):
    message : Annotated[str , Field(..., description="status of prediction")]
    predicted_output : PredictedOutput

    

class CropProductionModel(BaseModel):
    District_Name : Annotated[str , Field(..., description="Enter your dictrict", examples=["Khargone"])]
    Crop_Year : Annotated[int, Field(..., description="Enter the year ", examples=[2026])]
    Season : Annotated[Literal["Whole Year", "Kharif", "Rabi"], Field(..., description="enter the season of crop", examples=["Whole Year"])]
    Crop : Annotated[str , Field(..., description="Enter Crop ", examples=["Rice"])]
    Area : Annotated[float, Field(..., description="Enter Area in Hectors", examples=[2.0])]

    @field_validator('District_Name')
    @classmethod
    def transform_name(cls, value):
        return value.title()
    
    @field_validator('Crop')
    @classmethod
    def transform_Cropname(cls, value):
            return value.title()



class ProductionOutput(BaseModel):
    prediction : Annotated[float, Field(..., description="predicted total production in metric tonne")]
    production_per_hector : Annotated[float, Field(..., description="predicted production per hector in metric tonne")]
   

class CropProduction(BaseModel):
    message : Annotated[str , Field(..., description="status of prediction")]
    predicted_output : ProductionOutput