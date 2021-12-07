from app.models.media.media import Media


class Manga(Media):
    chapters: int
    volumes: int
