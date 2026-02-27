import aiohttp

from src.config import settings
from src.schemas.get_current_user_response import GetCurrentUserResponse
from src.schemas.verify_token_response import VerifyTokenResponse


class AuthService:
    @staticmethod
    async def verify_token(token:str) -> VerifyTokenResponse | None:
        res: VerifyTokenResponse | None = None
        async with aiohttp.ClientSession() as session:
            session.headers.update({"Authorization": f"Bearer {token}"})
            resp = await session.post(settings.auth_service_url+'/api/v1/auth/verify')
            if resp.status != 200:
                resp.raise_for_status()
            resp = await resp.json()
            res = VerifyTokenResponse(**resp)
        return res

    @staticmethod
    async def get_current_user(token:str) -> GetCurrentUserResponse | None:
        res: GetCurrentUserResponse | None = None
        async with aiohttp.ClientSession() as session:
            session.headers.update({"Authorization": f"Bearer {token}"})
            resp = await session.get(settings.auth_service_url+'/api/v1/auth/me')
            if resp.status == 401:
                return None
            resp = await resp.json()
            res = GetCurrentUserResponse(**resp)
        return res
