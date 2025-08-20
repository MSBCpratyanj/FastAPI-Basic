from pydantic import BaseModel,field_validator

class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None

    @field_validator('title')
    def title_must_be_longer_than_3_chars(cls,value):
        if len(value) < 3:
            raise ValueError("Title msut beat least longer then 3 characters long")
        return value
    @field_validator('author')
    def author_can_not_be_anonymous(cls,value):
        if value.lower == "anonymous":
            raise ValueError("user name can not be Anonymous")
        return value
    
class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    
    class Config:
        from_attributes = True
