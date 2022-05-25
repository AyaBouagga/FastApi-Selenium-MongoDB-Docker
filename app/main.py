from pymongo import MongoClient
from fastapi import FastAPI, status
from app.model import DB,PAGE_COLLECTION ,Page
from app.scraping import FBPublicPageScraper

from random_object_id import generate

from typing import List
from app.model import Page ,Post

app =FastAPI()

    
@app.post("/{page_name}", status_code=status.HTTP_201_CREATED)
def add_page(page_name:str):

    '''
    FastApi Service that declenche the scraping job
    and store the results in a mongoDB database

    '''


    with MongoClient("mongodb://root:rootpassword@db:27017/") as client:
        page_collection = client[DB][PAGE_COLLECTION]
        about,list_posts=FBPublicPageScraper(page_name).get_page_info()
        new_scraped_page=Page(page_id=generate(),name=about[0].text,adress=about[5].text,phone_nb=about[8].text,website=about[7].text,description=about[1].text,status=about[10].text.split(" ")[0
],posts=list_posts) 
        
        result = page_collection.insert_one(new_scraped_page.dict())
        
        ack = result.acknowledged
        return {"insertion": ack}


@app.get("/pages/{name}", response_model=List[Page])
def get_data(name: str):

    ''' FastApi service that get all Data for a given page from our Mongo DB   '''

    with MongoClient("mongodb://root:rootpassword@db:27017/") as client:
        page_collection = client[DB][PAGE_COLLECTION]
        msg_list = page_collection.find({"name":name})
        response_msg_list = []
        for msg in msg_list:
            response_msg_list.append(Page(**msg))
        return response_msg_list



@app.get("/page/{name}/posts")

def get_posts(name: str):

    """Get all posts for the specified page_name."""

    with MongoClient("mongodb://root:rootpassword@db:27017/") as client:
        page_collection = client[DB][PAGE_COLLECTION]
        page_list = page_collection.find({"name":name})
        response_post_list =Page(**page_list[0]).posts

        return response_post_list




@app.get("/page/{name}/about")

def get_info(name: str):

    """Get the "About" section for a given page_name."""

    with MongoClient("mongodb://root:rootpassword@db:27017/") as client:
        page_collection = client[DB][PAGE_COLLECTION]
        page_list = page_collection.find({"name":name})
        response_ ={'name':Page(**page_list[0]).name,'adress':Page(**page_list[0]).adress,'phone number':Page(**page_list[0]).phone_nb,'website':Page(**page_list[0]).website,'descrpition':Page(**page_list[0]).description,'status':Page(**page_list[0]).status}

        return response_











