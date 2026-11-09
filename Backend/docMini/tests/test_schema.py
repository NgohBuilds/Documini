from docmini.schemas import DocumentCreate

def test_create_document_valid():
    data = {"title" : "Les Oiseaux du Ciel","category":"musico-theatrale", "description" : "Film fictif"}

    document = DocumentCreate.model_validate(data)

    assert document.title == "Les Oiseaux du Ciel"
    assert document.category == "musico-theatrale"


