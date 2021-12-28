from enum import Enum

from pydantic import BaseModel

from app.models.media.media_cover import MediaCover
from app.models.media.media_title import MediaTitle


class MediaRelationNode(BaseModel):
    id: int
    siteUrl: str
    title: MediaTitle
    coverImage: MediaCover


class MediaRelationType(Enum):
    ADAPTATION = "ADAPTATION"
    PREQUEL = "PREQUEL"
    SEQUEL = "SEQUEL"
    PARENT = "PARENT"
    SIDE_STORY = "SIDE_STORY"
    CHARACTER = "CHARACTER"
    SUMMARY = "SUMMARY"
    ALTERNATIVE = "ALTERNATIVE"
    SPIN_OFF = "SPIN_OFF"
    OTHER = "OTHER"
    SOURCE = "SOURCE"
    COMPILATION = "COMPILATION"
    CONTAINS = "CONTAINS"


class MediaRelationEdge(BaseModel):
    relationType: MediaRelationType
    node: MediaRelationNode


class MediaRelation(BaseModel):
    edges: list[MediaRelationEdge]
