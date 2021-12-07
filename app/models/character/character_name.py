from pydantic import BaseModel


class CharacterName(BaseModel):
    full: str
    alternative: str
