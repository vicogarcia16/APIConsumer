from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Víctor Manuel García Negrete",
                "email": "mg_619@hotmail.com",
                "password": "password"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "mg_619@hotmail.com",
                "password": "password"
            }
        }