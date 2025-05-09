from fastapi import APIRouter, HTTPException, Depends
from api.classifications.model import Classification

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
    print('here')
    await classification.create()
    return classification

