from pydantic import BaseModel
from typing import List

DB = "fb"
PAGE_COLLECTION = "pages"


class Post(BaseModel):
    post_id:int
    post_text:str

class Page(BaseModel):
    page_id:str
    name: str
    adress: str
    phone_nb: str
    website:str
    description:str
    status:str #open or close now
    posts:List[Post]


