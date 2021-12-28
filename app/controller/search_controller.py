from flask import Blueprint, jsonify, request, redirect
from werkzeug.exceptions import NotFound

from app.models.media.anime import Anime
from app.models.media.manga import Manga
from app.models.media.media_type import MediaType
from app.service.search_service import SearchService

search = Blueprint('search', __name__)


@search.route("/search/media/", methods=["GET"])
async def media_search_for():
    query = request.args.get("query")
    m_type = request.args.get("type")

    # basic MediaType validation
    if m_type not in set(mt.value for mt in MediaType):
        raise NotFound()
    m_type = MediaType[m_type]

    data = await SearchService.media_search_for(query, m_type)
    if not data:
        raise NotFound()

    # persist relevant search results
    cls = Anime if m_type == MediaType.ANIME else Manga
    converted_media = [cls(**m) for m in data]
    await SearchService.persist_relevant_media(converted_media)

    return jsonify(data)


@search.route("/search/<string:m_type>/", methods=["GET"])
async def media_type_search_for(m_type: str):
    query = request.args.get("query")

    return redirect(f"/search/media/?query={query}&type={m_type.upper()}")
