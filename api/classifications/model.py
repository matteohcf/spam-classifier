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

    def get_classification(self, plain_password):
        return 'd'

    #@before_event(Insert)
    #def before_insert(self):
    #   self.password = self.get_password_hash()