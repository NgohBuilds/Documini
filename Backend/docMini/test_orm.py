from docmini.models import DocumentModel
from docmini.database import SessionLocal

db = SessionLocal()

try :

    document = DocumentModel(
        title = "Annah et les cochons",
        category= "Comedie",
        description= "oeuvre litteraire qui retrace les aventure de Annah dans le monde des cochons"

    )

    db.add(document)
    db.commit()
    db.refresh(document)

    print("Document Saved Successfully !")

except Exception:

    db.rollback()
    raise

finally :
    db.close()



