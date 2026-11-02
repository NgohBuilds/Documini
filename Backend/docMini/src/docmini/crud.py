from .models import DocumentModel
from sqlalchemy.orm import Session
from .schemas import DocumentCreate

# Create a document in database
def create_document(db : Session , document: DocumentCreate) -> DocumentModel:
    """Create a document.
    """

    new_document = DocumentModel(**document.model_dump())

    try : 
        db.add(new_document)
        db.commit()

    finally:
        db.close()

    return new_document
    