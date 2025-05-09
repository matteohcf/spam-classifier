import asyncio
from service.classifier.utils.classifier import train_classifier, classify_italian_text
from service.classifier.utils.const import Dataset
from service.config import ClassificationType

email_dataset = Dataset()
classificationModel = train_classifier(email_dataset)

def get_classification_type(classification):
    if classification == 0:
        return ClassificationType.NOT_SPAM
    elif classification == 1:
        return ClassificationType.SPAM
    else:
        raise ValueError("Invalid classification result")

async def get_classification(text):
    print(text)
    result = await classify_italian_text(text, classificationModel, email_dataset)
    classificationType = get_classification_type(result)
    return classificationType