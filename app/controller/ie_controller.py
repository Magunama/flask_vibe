from flask import Blueprint, request, abort, Response

from app.models.media.anime import Anime
from app.models.media.manga import Manga
from app.service.ie_service import IEService

ie_blueprint = Blueprint('import/export', __name__)


@ie_blueprint.before_request
def before_ie():
    # allow only from localhost
    if request.remote_addr != "127.0.0.1":
        abort(403)  # Forbidden


@ie_blueprint.route("/export/anime", methods=["GET"])
async def export_anime():
    # todo: also export JSON?
    accept_headers = request.headers.getlist('accept')
    if "text/csv" not in accept_headers:
        abort(406)  # Wrong accept headers

    anime_as_csv = await IEService.export_media_as_csv(Anime)
    return Response(anime_as_csv, mimetype="text/csv")


@ie_blueprint.route("/export/manga", methods=["GET"])
async def export_manga():
    accept_headers = request.headers.getlist('accept')
    if "text/csv" not in accept_headers:
        abort(406)  # Wrong accept headers

    manga_as_csv = await IEService.export_media_as_csv(Manga)
    return Response(manga_as_csv, mimetype="text/csv")


@ie_blueprint.route("/import/anime", methods=["POST"])
async def import_anime():
    uploaded_file = request.files.get("file", None)
    if uploaded_file and IEService.valid_file_extension(uploaded_file):
        # todo: BytesIO might be able to read the stream directly?
        imported_data = await IEService.import_media_from_csv(Anime, uploaded_file.stream.read().decode("utf-8"))
        return Response(imported_data, mimetype="application/json")

    if request.data and request.mimetype == "text/csv":
        imported_data = await IEService.import_media_from_csv(Anime, request.data.decode("utf-8"))
        return Response(imported_data, mimetype="application/json")

    abort(405)  # wrong input


@ie_blueprint.route("/import/manga", methods=["POST"])
async def import_manga():
    uploaded_file = request.files.get("file", None)
    if uploaded_file and IEService.valid_file_extension(uploaded_file):
        imported_data = await IEService.import_media_from_csv(Manga, uploaded_file.stream.read().decode("utf-8"))
        return Response(imported_data, mimetype="application/json")

    if request.data and request.mimetype == "text/csv":
        imported_data = await IEService.import_media_from_csv(Manga, request.data.decode("utf-8"))
        return Response(imported_data, mimetype="application/json")

    abort(405)  # wrong input
