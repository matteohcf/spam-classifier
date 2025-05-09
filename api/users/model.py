import datetime
from beanie import Document, before_event, Insert, Indexed
from passlib.context import CryptContext
from pydantic import Field
from service.config import UserRole

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



class User(Document):
    email: str = Indexed(unique=True)
    password: str
    role: UserRole = Field(default=UserRole.USER)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)

    def get_password_hash(self):
        return pwd_context.hash(self.password)

    @before_event(Insert)
    def before_insert(self):
        self.password = self.get_password_hash()