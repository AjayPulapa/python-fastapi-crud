from pydantic import BaseModel

# Schema for creating a new user
class UserCreate(BaseModel):
    name: str
    email: str


# Schema to return user response
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    # Pydantic v2 config for ORM mode
    model_config = {
        "from_attributes": True
    }
