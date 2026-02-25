import aiohttp

from src.config import settings
from src.schemas.verify_token_response import VerifyTokenResponse


class AuthService:
    @staticmethod
    async def verify_token(token:str):
        res: VerifyTokenResponse
        async with aiohttp.ClientSession() as session:
            session.headers.update({"Authorization": f"Bearer {token}"})
            resp = await session.get(settings.auth_service_url+'/api/verify')
            res = VerifyTokenResponse(**(await resp.json()))
        return res

if __name__ == '__main__':
    AuthService.verify_token("")