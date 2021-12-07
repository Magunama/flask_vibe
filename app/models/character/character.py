from beanie import Document

from app.models.character.character_media import CharacterMedia
from app.models.character.character_name import CharacterName


class Character(Document):
    id: int
    siteUrl: str
    name: CharacterName
    favourites: int
    media: list[CharacterMedia]
