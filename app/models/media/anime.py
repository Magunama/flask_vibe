import typing
from datetime import date

from app.models.media.media import Media
from app.models.media.media_season import MediaSeason


class Anime(Media):
    episodes: typing.Optional[int]
    duration: int
    season: typing.Optional[MediaSeason]
    seasonYear: typing.Optional[int]

    @property
    def should_persist(self):
        today = date.today()
        if self.seasonYear == today.year:
            return True

        return False
