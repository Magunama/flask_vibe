from flask import Blueprint, Response
from werkzeug.exceptions import NotFound

from app.models.media.media_type import MediaType
from app.service.media_service import MediaService

media_blueprint = Blueprint('media', __name__)


# media_api = Api(media_blueprint)


@media_blueprint.route("/anime/<int:anime_id>/", methods=["GET"])
async def get_anime_by_id(anime_id: int):
    m = await MediaService.get_anime_by(anime_id)
    if not m:
        data = await MediaService.fetch_media_by(anime_id, MediaType.ANIME)
        if not data:
            raise NotFound()

        # store data for future use
        m = await MediaService.add_anime(data)

    return Response(m.json(indent=4), mimetype="application/json")


@media_blueprint.route("/manga/<int:manga_id>/", methods=["GET"])
async def get_manga_by_id(manga_id: int):
    m = await MediaService.get_manga_by(manga_id)
    if not m:
        data = await MediaService.fetch_media_by(manga_id, MediaType.MANGA)
        if not data:
            raise NotFound()

        # store data for future use
        m = await MediaService.add_manga(data)

    return Response(m.json(indent=4), mimetype="application/json")
