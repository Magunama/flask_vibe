from app.models.media.media import Media


class Manga(Media):
    chapters: int
    volumes: int

    @property
    def should_persist(self) -> bool:
        # todo: implementation
        return False
