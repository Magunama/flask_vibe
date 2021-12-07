import typing
from datetime import datetime, timedelta

import jwt

from app.models.auth.auth_user import AuthUser


class AuthService:
    @staticmethod
    async def look_up_user(username: str, password: str) -> typing.Union[AuthUser, None]:
        return await AuthUser.find_one(AuthUser.name == username, AuthUser.password == password)

    @staticmethod
    def encode_auth(user_id: int, secret_key: str):
        payload = {
            'public_id': user_id,
            'exp': datetime.utcnow() + timedelta(minutes=45),
            'iat': datetime.utcnow(),
        }

        return jwt.encode(payload, secret_key)
