from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class ClassificationType(str, Enum):
    SPAM = "SPAM"
    NOT_SPAM = "not-spam"