import typing

from app.models.media.media import Media
from app.models.media.media_season import MediaSeason


class Anime(Media):
    episodes: typing.Optional[int]
    duration: int
    season: typing.Optional[MediaSeason]
    seasonYear: typing.Optional[int]
