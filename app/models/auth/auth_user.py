from beanie import Document


class AuthUser(Document):
    id: int
    name: str
    password: str
