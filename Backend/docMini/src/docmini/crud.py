from .models import DocumentModel
from sqlalchemy.orm import Session
from .schemas import DocumentCreate, DocumentUpdate
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

# Create a document in database
def create_document(db : Session , document: DocumentCreate) -> DocumentModel:
    """Create a document.
    """

    new_document = DocumentModel(**document.model_dump())

    try : 
        db.add(new_document)
        db.commit()
        db.refresh(new_document)

    except SQLAlchemyError:
        db.rollback()
        raise

    return new_document

def get_document_by_id(db : Session , document_id : int) -> DocumentModel:

    document_orm = db.get(DocumentModel, document_id)

    return document_orm

def get_documents( db: Session , categories : None | list[str]) -> list[DocumentModel]:

    statement = select(DocumentModel).order_by(DocumentModel.id)

    if categories is not None :
        statement = statement.where(DocumentModel.category.in_(categories))

    try:
        results = db.execute(statement).scalars().all()

    except SQLAlchemyError:
        raise

    return results

def update_document(db: Session, document_id:int, document: DocumentUpdate) -> None | DocumentModel:
    """Update a document with a specific Id."""

    document_orm = db.get(DocumentModel , document_id)

    if document_orm is None : 
        return None

    new_document_data = document.model_dump(exclude_unset=True)

    for k, v in new_document_data.items():
        setattr(document_orm, k, v)

    try:
        db.commit()
        db.refresh(document_orm)

    except SQLAlchemyError:
        db.rollback()
        raise

    return document_orm

def delete_document(
        db:Session , document_id : int 
) -> None | bool:
    document_orm = db.get(DocumentModel,document_id )

    if document_orm is None:
        return None

    try :
        db.delete(document_orm)
        db.commit()

    except SQLAlchemyError:
        db.rollback()
        raise

    return True
        
