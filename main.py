from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Simuler une base de données de questions
questions_db = []

# Modèle pour une question
class Question(BaseModel):
    id: int
    texte: str
    choix: List[str]
    bonne_reponse: int

# Modèle pour la réponse de l'utilisateur
class ReponseUtilisateur(BaseModel):
    question_id: int
    choix_selectionne: int

# Endpoint pour ajouter une question
@app.post("/questions/")
def ajouter_question(question: Question):
    questions_db.append(question)
    return {"message": "Question ajoutée avec succès"}

# Endpoint pour lister toutes les questions
@app.get("/questions/")
def lister_questions():
    return questions_db

# Endpoint pour répondre à une question
@app.post("/repondre/")
def repondre_question(reponse: ReponseUtilisateur):
    for question in questions_db:
        if question.id == reponse.question_id:
            return {"correct": question.bonne_reponse == reponse.choix_selectionne}
    raise HTTPException(status_code=404, detail="Question non trouvée")
