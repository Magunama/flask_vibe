import typing
from datetime import date

from app.models.media.anime import Anime
from app.models.media.manga import Manga
from app.models.media.media_type import MediaType
from app.utils.request import BaseRequest

ani_search_media = """
    query ($q: String, $type: MediaType) {
        Page(perPage: 10){
            media(search: $q, type: $type){
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
                            id
                            title{
                                romaji
                                english
                            }
                            siteUrl
                            coverImage {
                                large
                            }
                        }
                    }
                }
            }
        }
    }
"""


class SearchService:
    ani_url = "https://graphql.anilist.co"

    @staticmethod
    async def media_search_for(query: str, m_type: MediaType):
        variables = {"q": query, "type": m_type.value}
        payload = {"query": ani_search_media, "variables": variables}
        data = await BaseRequest.post_json(url=SearchService.ani_url, payload=payload, headers={})
        data = data["data"]["Page"]["media"]
        return data

    @staticmethod
    def _should_persist(m: typing.Union[Anime, Manga]) -> bool:
        """returns whether media is from current season year"""
        if type(m) is Anime:
            today = date.today()
            if m.seasonYear == today.year:
                return True
        return False

    @staticmethod
    async def persist_relevant_media(converted_media: list[typing.Union[Anime, Manga]]):
        media_should_persist = list(filter(lambda m: SearchService._should_persist(m), converted_media))
        if not media_should_persist:
            return

        for m in media_should_persist:
            await m.save()
