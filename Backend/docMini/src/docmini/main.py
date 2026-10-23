from fastapi import FastAPI,status, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI(title= "DocuMini", description="Gestion simple des métadonnées de documents")

docs = [
    {"id" : 1 , "title" : "A software crafmanship"  , "category" : "education","description" : "learn how to write clean code" },
    {"id" : 2 , "title" : "Atomic Habits"  , "category" : "lifestyle","description" : "learn how to get better at organising" },
    {"id" : 3 , "title" : "Demon slayer"  , "category" : "manga","description" : "a manga about chasing demons" },
]

class document(BaseModel):
    id : int = Field(gt=0)
    title : str = Field (min_length=3)
    category : str = Field(min_length=3)
    description : str
    

@app.get("/document/about")
async def get_description():

    return {
  "application": "DocuMini",
  "description": "Gestion simple des métadonnées de documents",
  "version": "0.1.0"
}


@app.get("/documents")
async def get_documents(category : list[str] = Query(default= None )):

    if not category is None:
        document_filtered_by_category = list(filter(lambda doc : doc["category"] in category , docs))

        return document_filtered_by_category

    return {"Documents" : docs}
  

@app.get("/documents/{document_id}", summary="Retrieve a specific document", response_model = document)
async def get_document(document_id : Annotated[int, Path(gt = 0)]):

    is_exists = any(doc["id"] == document_id for doc in docs )

    if not is_exists :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Aucun doc avec cet ID")

    for doc in docs :
        if doc["id"] == document_id:
            trouve = doc

    return trouve
        