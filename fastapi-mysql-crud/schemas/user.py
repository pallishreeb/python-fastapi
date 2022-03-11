from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    
class UserCount(BaseModel):
    total: int    
