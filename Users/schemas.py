from pydantic import BaseModel, EmailStr, Field

class CreateUser(BaseModel):
    username: str = Field(ge=1, le=20)
    email: EmailStr