from beanie import init_beanie
from motor import motor_asyncio

from app.models.auth.auth_user import AuthUser
from app.models.media.anime import Anime
from app.models.media.manga import Manga
from app.models.media.media import Media


async def init_db():
    db_url = ""

    db = motor_asyncio.AsyncIOMotorClient(
        f"mongodb+srv://root:{db_url}?retryWrites=true&w=majority")

    # Init beanie with the document classes
    await init_beanie(database=db.animevibe, document_models=[Anime, Manga, Media, AuthUser])
