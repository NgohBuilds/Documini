from sqlalchemy import select
from docmini.database import SessionLocal
from docmini.models import DocumentModel

db = SessionLocal()

statement = select(DocumentModel)

try : 
    documents = db.execute(statement).scalars().all()

    for doc in documents:
        print(f"Title : {doc.title} \n ID : {doc.id}")

finally:
    db.close()

