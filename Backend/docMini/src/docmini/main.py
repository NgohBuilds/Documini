from fastapi import FastAPI,status, HTTPException, Path, Query, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from docmini.database import get_db
from docmini.schemas import Document, DocumentCreate, DocumentUpdate
from .crud import create_document, update_document, delete_document, get_document_by_id, get_documents


app = FastAPI(
    title= "DocuMini",
    description="Gestion simple des métadonnées de documents"
    )

@app.get("/documents" ,  response_model= list[Document], tags=["GET Request"])
def get_documents_route(categories : list[str] | None = Query(default= None ) , db : Session = Depends(get_db)):

    try:
        documents = get_documents(db, categories)

    except SQLAlchemyError:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Operations failed")

    return documents
  

@app.get("/documents/{document_id}", response_model = Document, tags=["GET Request"])
def get_document(document_id : Annotated[int, Path(gt = 0)], db : Session = Depends(get_db)):

    document = get_document_by_id(db, document_id)

    if document is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="document not found")

    return document


@app.post('/documents' , response_model = Document, status_code= status.HTTP_201_CREATED)
def create_document_route(document : DocumentCreate, db : Session = Depends(get_db)):
    try :
        document_created = create_document(db, document)

    except SQLAlchemyError:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR , detail= "Database operation failed.")

    return document_created

@app.patch('/documents/{document_id}', response_model= Document, status_code=status.HTTP_200_OK)
def update_document_route(document_id : Annotated[int, Path(gt=0)], document_update : DocumentUpdate, db : Session = Depends(get_db)):

    try:
        updated_document = update_document(db, document_id, document_update)

    except SQLAlchemyError:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Databse operation failed")

    if updated_document is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "Document Not Found")

    return updated_document

@app.delete('/documents/{document_id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_document_route(document_id : Annotated[int, Path(gt=0)], db : Session = Depends(get_db)):

    try :
       deleted = delete_document(db, document_id)

    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail= "Database operation failed")

    if deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document Not Found")

    return None
    
    


    
