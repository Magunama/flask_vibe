from typing import Optional

from pydantic import BaseModel


class MediaTitle(BaseModel):
    romaji: str
    english: Optional[str]
