from app.models.media.anime import Anime
from app.models.media.manga import Manga
from app.models.media.media_type import MediaType
from app.utils.request import BaseRequest

ani_anime = """
        query ($id: Int) {
            Media (id: $id, type: ANIME) {
                id
                siteUrl
                coverImage {
                    large
                }
                title {
                    romaji
                    english
                }
                format
                status
                episodes
                duration
                averageScore
                meanScore
                rankings{
                    rank
                    type
                    allTime
                }
                description
                season
                seasonYear
                genres
                relations{
                    edges{
                        relationType
                        node{
                            title{
                                romaji
                            }
                            siteUrl
                            type
                        }
                    }
                }
            } 
        }
    """

ani_manga = """
        query ($id: Int) {
            Media (id: $id, type: MANGA) {
                id
                siteUrl
                coverImage {
                    large
                }
                title {
                    romaji
                    english
                }
                format
                status
                chapters
                volumes
                isAdult
                averageScore
                meanScore
                rankings{
                    rank
                    type
                    allTime
                }
                description
                season
                seasonYear
                genres
                studios{
                    nodes{
                        name
                        isAnimationStudio
                    }
                }
                relations{
                    edges{
                        relationType
                        node{
                            title{
                                romaji
                            }
                            siteUrl
                            type
                        }
                    }
                }
            } 
        }
    """


class MediaService:
    ani_url = "https://graphql.anilist.co"

    @staticmethod
    async def fetch_media_by(media_id: int, media_type: MediaType):
        variables = {"id": media_id}
        query = {MediaType.ANIME: ani_anime, MediaType.MANGA: ani_manga}.get(media_type)
        payload = {"query": query, "variables": variables}
        data = await BaseRequest.post_json(url=MediaService.ani_url, payload=payload, headers={})
        data = data["data"]["Media"]
        return data

    @staticmethod
    async def get_anime_by(anime_id: int):
        return await Anime.find_one(Anime.id == anime_id)

    @staticmethod
    async def get_manga_by(manga_id: int):
        return await Manga.find_one(Manga.id == manga_id)

    @staticmethod
    async def add_anime(data: dict) -> Anime:
        nm = Anime(**data)
        await nm.insert()
        return nm

    @staticmethod
    async def add_manga(data: dict) -> Manga:
        nm = Manga(**data)
        await nm.insert()
        return nm
