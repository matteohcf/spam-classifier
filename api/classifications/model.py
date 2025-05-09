import datetime
from beanie import Document
from pydantic import Field
from typing import Optional
from service.config import ClassificationType


class Classification(Document):
    text: str
    disabled: bool = False
    type: Optional[ClassificationType] = Field(default=ClassificationType.NOT_SPAM)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)