from pydantic import BaseModel, Field, ConfigDict

class Document(BaseModel):

    model_config = ConfigDict(from_attributes= True) # Permet a pydantic de lire les attributs du modele sqlalchemy
    
    id : int = Field(gt=0)
    title : str = Field (min_length=3)
    category : str = Field(min_length=3)
    description : str | None = None

class DocumentCreate(BaseModel):
    title : str = Field(min_length=3)
    category : str = Field(min_length = 3)
    description : str | None = None