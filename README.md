
# API FastAPI pour une Application de QCM (Questionnaire à Choix Multiples)

## Description

Ce projet implémente une API simple en utilisant **FastAPI** pour gérer un questionnaire à choix multiples (QCM). L'API permet :
- D'ajouter des questions.
- De lister toutes les questions.
- De répondre à une question et vérifier si la réponse est correcte ou non.

## Fonctionnalités

1. **Ajouter une question QCM**
   - Endpoint : `POST /questions/`
   - Permet d'ajouter une nouvelle question avec plusieurs choix et une réponse correcte.
   
2. **Lister toutes les questions**
   - Endpoint : `GET /questions/`
   - Permet de récupérer toutes les questions ajoutées à la base.

3. **Répondre à une question**
   - Endpoint : `POST /repondre/`
   - Permet de répondre à une question en soumettant l'identifiant de la question et le choix sélectionné.

## Prérequis

- **Python 3.7+**
- **FastAPI** et **Uvicorn** pour lancer le serveur.

## Installation

1. **Cloner le projet :**

   ```bash
   git clone https://github.com/votre-repo/api-qcm.git
   cd api-qcm
   ```

2. **Créer un environnement virtuel et installer les dépendances :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Pour Linux/Mac
   venv\Scripts\activate     # Pour Windows

   pip install fastapi uvicorn
   ```

3. **Lancer le serveur FastAPI :**

   ```bash
   uvicorn main:app --reload
   ```

   Cela démarrera le serveur sur `http://127.0.0.1:8000`.

## Endpoints de l'API

### 1. **Ajouter une question QCM**

- **Méthode** : `POST`
- **URL** : `http://127.0.0.1:8000/questions/`
- **Body** : (au format JSON)

Exemple de corps de requête :
```json
{
  "id": 1,
  "texte": "Quelle est la capitale de la France ?",
  "choix": ["Paris", "Londres", "Berlin"],
  "bonne_reponse": 0
}
```

- **Réponse** :

```json
{
  "message": "Question ajoutée avec succès"
}
```

### 2. **Lister toutes les questions**

- **Méthode** : `GET`
- **URL** : `http://127.0.0.1:8000/questions/`

- **Réponse** :

```json
[
  {
    "id": 1,
    "texte": "Quelle est la capitale de la France ?",
    "choix": ["Paris", "Londres", "Berlin"],
    "bonne_reponse": 0
  }
]
```

### 3. **Répondre à une question**

- **Méthode** : `POST`
- **URL** : `http://127.0.0.1:8000/repondre/`
- **Body** : (au format JSON)

Exemple de corps de requête :
```json
{
  "question_id": 1,
  "choix_selectionne": 0
}
```

- **Réponse** (si la réponse est correcte) :
```json
{
  "correct": true
}
```

- **Réponse** (si la réponse est incorrecte) :
```json
{
  "correct": false
}
```

### Exemple d'utilisation avec Postman

#### 1. **Ajouter une question**
- Méthode : **POST**
- URL : `http://127.0.0.1:8000/questions/`
- Dans **Postman** :
  - Choisissez **Body** > **raw** > **JSON**.
  - Collez le contenu suivant dans le corps de la requête :

```json
{
  "id": 2,
  "texte": "Quelle est la capitale de l'Allemagne ?",
  "choix": ["Paris", "Londres", "Berlin"],
  "bonne_reponse": 2
}
```

#### 2. **Lister toutes les questions**
- Méthode : **GET**
- URL : `http://127.0.0.1:8000/questions/`

#### 3. **Répondre à une question**
- Méthode : **POST**
- URL : `http://127.0.0.1:8000/repondre/`
- Exemple de corps de requête :
```json
{
  "question_id": 2,
  "choix_selectionne": 2
}
```

## Test via cURL

Si vous préférez utiliser **cURL**, voici quelques exemples :

### Ajouter une question :
```bash
curl -X POST "http://127.0.0.1:8000/questions/" -H "Content-Type: application/json" -d '{
  "id": 1,
  "texte": "Quelle est la capitale de la France ?",
  "choix": ["Paris", "Londres", "Berlin"],
  "bonne_reponse": 0
}'
```

### Lister les questions :
```bash
curl -X GET "http://127.0.0.1:8000/questions/"
```

### Répondre à une question :
```bash
curl -X POST "http://127.0.0.1:8000/repondre/" -H "Content-Type: application/json" -d '{
  "question_id": 1,
  "choix_selectionne": 0
}'
```

## Conclusion

Ce projet vous permet de créer une API simple avec **FastAPI** pour gérer des questions de type QCM et permettre aux utilisateurs de répondre à ces questions. Vous pouvez tester l'API avec **Postman** ou **cURL** en suivant les instructions fournies ci-dessus.
