import asyncio
from fastapi import APIRouter, HTTPException, Depends
from api.classifications.model import Classification
from service.classifier.utils.classifier import train_classifier, classify_italian_text
from service.classifier.utils.classifier_instance import get_classification
from service.classifier.utils.const import Dataset

router = APIRouter()

@router.get("/")
async def read_classifications():
    classifications = await Classification.find().to_list()
    return classifications

@router.get("/{classification_id}", response_model=Classification)
async def read_user(classification_id: str):
    classification = await Classification.get(classification_id)
    if not classification:
        raise HTTPException(status_code=404, detail="Classification not found")
    return classification


@router.post("/", response_model=Classification)
async def create_classification(classification: Classification):
    predicted_type = await get_classification(classification.text)

    classification.type = predicted_type

    # Salva il risultato della classificazione
    print(classification)
    classification = {
        "text": classification.text,
        "type": classification.type
    }

    # Salva nel database
    #await classification.cre#ate()
    return classification


