from .main import Document, DocumentCreate
from pydantic import BaseModel, ValidationError
# Dico for Document model 

documents_test = [
    {
        "id": 1,
        "title": "Clean Code",
        "category": "education",
        "description": "Livre sur le code propre"
    },
    {
        "id": 2,
        "title": "Atomic Habits",
        "category": "lifestyle",
        "description": "Livre sur les habitudes"
    },
    {
        "id": 3,
        "title": "Demon Slayer",
        "category": "manga",
        "description": "Histoire de chasseurs de demons"
    },
    {
        "id": 0,  # Invalide : id doit être > 0
        "title": "Python Guide",
        "category": "education",
        "description": "Guide Python"
    },
    {
        "id": 4,
        "title": "AI",  # Invalide : titre trop court
        "category": "education",
        "description": "Introduction à l'IA"
    },
    {
        "id": 5,
        "title": "Python Guide",
        "category": "IT",  # Invalide : catégorie trop courte
        "description": "Guide Python"
    }
]


# Dico for DocumentCreate
documents_create_test = [
    {
        "title": "Clean Architecture",
        "category": "education",
        "description": "Principes d'architecture logicielle"
    },
    {
        "title": "Deep Work",
        "category": "productivity",
        "description": "Améliorer sa concentration"
    },
    {
        "title": "One Piece",
        "category": "manga",
        "description": "Aventure de pirates"
    },
    {
        "title": "AI",  # Invalide : titre trop court
        "category": "education",
        "description": "Introduction à l'IA"
    },
    {
        "title": "Python Guide",
        "category": "IT",  # Invalide : catégorie trop courte
        "description": "Guide Python"
    },
    {
        "title": "Atomic Habits",
        "category": "lifestyle"  # Valide si description est facultative
    }
]

def validate_documents(model : type[BaseModel], data:list[dict])-> list[str]:
    results = []

    for index, value in enumerate(data, start=1):
        try:
            model.model_validate(value)
        except ValidationError as error:
            results.append(f"Cas {index} : Failed")
            print(f"Cas {index} : {error}")
        else:
            results.append(f"Cas {index} : Success")

    return results
            
print(validate_documents(Document, documents_test))
print(validate_documents(DocumentCreate, documents_create_test))