import asyncio

from app.db import init_db
from app.models.media.media import Media
from app.models.media.media_cover import MediaCover
from app.models.media.media_format import MediaFormat
from app.models.media.media_season import MediaSeason
from app.models.media.media_status import MediaStatus
from app.models.media.media_title import MediaTitle


def test_media_creation(client):
    asyncio.run(init_db())

    t = MediaTitle(romaji="Cowboyu Bebubopu", english="Cowboy Bebop")
    i = MediaCover(large="https://imgur.com")
    m = Media(id=19, siteUrl="https://google.com", title=t, description="Once upon a time...", coverImage=i,
              season=MediaSeason.WINTER, seasonYear=2021, format=MediaFormat.TV, status=MediaStatus.FINISHED,
              genres=["Comedy"], averageScore=81, meanScore=82)
    assert t.english == "Cowboy Bebop"
    assert m.id == 19
    assert m.format == MediaFormat.TV
    assert "Comedy" in m.genres
