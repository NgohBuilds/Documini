from pydantic import BaseModel, Field, ConfigDict, model_validator

class Document(BaseModel):

    model_config = ConfigDict(from_attributes= True) # Permet a pydantic de lire les attributs du modele sqlalchemy
    
    id : int = Field(gt=0)
    title : str = Field (min_length=3)
    category : str = Field(min_length=3)
    description : str | None = None

    model_config = {
         "json_schema_extra": 
              {
                   "examples" : 
                   [
                        {
                            "id" : "13",
                            "title" : "Les Fourberies de Scapin",
                            "category" : "Théâtre",
                           " description" :  "Une pièce Théatrale qui raconte sous un ton amusant les aventures de Scapin."  
                        }
                   ]
              }
             }

class DocumentCreate(BaseModel):
    title : str = Field(min_length=3)
    category : str = Field(min_length = 3)
    description : str | None = None

    model_config = {
         "json_schema_extra" : {
              "examples" : [
                   {
                        "title" : "Les tribus de Capitoline",
                        "category" : "drame"
                   },
                   {
                        "title" : "Petites gouttes de champs pour creer l'Homme",
                        "category" : "Poesie",
                        "description" : "Il s'agit d'une oeuvre africaine qui recouvre toutes les meilleurs poesies"
                   }
              ]
         }
    }

class DocumentUpdate(BaseModel):
    title : str | None = Field(default=None, min_length=3)
    category : str | None = Field(default= None, min_length = 3)
    description : str | None = None

    @model_validator(mode= 'after')
    def validate_non_nullable_fields(self):

        for field in ('title', 'category'):
            if field in self.model_fields_set and getattr(self, field) is None: 
                    raise ValueError(f"The field {field} must be non-nullable")
                
        return self
