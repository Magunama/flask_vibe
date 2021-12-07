from pydantic import BaseModel

from app.models.media.media_title import MediaTitle
from app.models.media.media_type import MediaType


class CharacterMedia(BaseModel):
    title: MediaTitle
    siteUrl: str
    type: MediaType
