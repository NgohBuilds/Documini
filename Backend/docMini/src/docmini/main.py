from fastapi import FastAPI


app = FastAPI(title= "DocuMini", description="Gestion simple des métadonnées de documents")

@app.get("/", tags=["First Route"])
def root():
    return {"Greeting" : "Hello Route"}

@app.get("/document/about")
def get_description():

    return {
  "application": "DocuMini",
  "description": "Gestion simple des métadonnées de documents",
  "version": "0.1.0"
}