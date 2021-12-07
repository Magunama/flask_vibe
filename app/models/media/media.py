import typing

from beanie import Document

from app.models.media.media_cover import MediaCover
from app.models.media.media_format import MediaFormat
from app.models.media.media_status import MediaStatus
from app.models.media.media_title import MediaTitle
from app.models.media.media_type import MediaType


class Media(Document):
    id: int
    siteUrl: str
    title: MediaTitle
    description: str
    coverImage: MediaCover
    # type: typing.Optional[MediaType]
    format: MediaFormat
    status: MediaStatus
    genres: list
    averageScore: int
    meanScore: int
