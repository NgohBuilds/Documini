from fastapi import FastAPI,status, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Annotated



app = FastAPI(
    title= "DocuMini",
    description="Gestion simple des métadonnées de documents"
    )

class Document(BaseModel):
    id : int = Field(gt=0)
    title : str = Field (min_length=3)
    category : str = Field(min_length=3)
    description : str | None = None

class DocumentCreate(BaseModel):
    title : str = Field(min_length=3)
    category : str = Field(min_length = 3)
    description : str | None = None


docs = [

    {"id" : 1 , "title" : "A software crafmanship"  , "category" : "education","description" : "learn how to write clean code"},
    {"id" : 2 , "title" : "Atomic Habits"  , "category" : "lifestyle","description" : "learn how to get better at organising" },
    {"id" : 3 , "title" : "Demon slayer"  , "category" : "manga","description" : "a manga about chasing demons" },
]



@app.get("/document/about")
async def get_description():

    return {
  "application": "DocuMini",
  "description": "Gestion simple des métadonnées de documents",
  "version": "0.1.0"
}


@app.get("/documents", response_model= list[Document])
async def get_documents(category : list[str] | None = Query(default= None )):

    if  category is not None:
        return [doc for doc in docs if doc["category"] in category]

    return docs
  

@app.get("/documents/{document_id}", summary="Retrieve a specific document", response_model = Document)
async def get_document(document_id : Annotated[int, Path(gt = 0)]):

    doc = next((doc for doc in docs if doc["id"] == document_id)  , None)

    if doc is None :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Aucun doc avec cet ID")

    return doc

@app.post('/documents' , response_model = Document, status_code= status.HTTP_201_CREATED)
def create_document(document : DocumentCreate):

    id_document = max((doc["id"] for doc in docs ), default= 1) + 1
    document_created =  {"id": id_document, **document.model_dump()} 

    docs.append(document_created)

    return document_created

@app.put('/documents/{document_id}', response_model= Document)
def update_document(document_id : Annotated[int, Path(gt=0)], document_update : DocumentCreate):

    doc_index = next((index for index, doc in enumerate(docs) if doc['id'] == document_id ), None)

    if doc_index is None :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "There's No Document with this ID")

    new_document = {"id" : document_id , **document_update.model_dump()}

    docs[doc_index] = new_document
    

    return new_document

@app.delete('/documents/{document_id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_document(document_id : Annotated[int, Path(gt=0)]):

    doc_to_delete = next((doc for doc in docs if doc['id'] == document_id ), None)

    if doc_to_delete is None :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "There's No Document with this ID")

    docs.remove(doc_to_delete)
    
