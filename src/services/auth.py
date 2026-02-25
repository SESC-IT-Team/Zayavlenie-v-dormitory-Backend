from fastapi import HTTPException, status

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
            if resp.status == 401:
                if resp.status == 401:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Incorrect or empty access token.",
                    )
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
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect or empty access token.",
                )
            resp = await resp.json()
            res = GetCurrentUserResponse(**resp)
        return res


async def main():
    print(await AuthService.get_current_user(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1Zjc4YmU0My03OGNlLTQ0YzQtOGY2Zi01ZjNjNjlkMTZjOGQiLCJyb2xlIjoiYWRtaW4iLCJwZXJtaXNzaW9ucyI6WyJhdXRoOmxvZ2luIiwiYXV0aDp2ZXJpZnkiLCJ1c2VyczpjcmVhdGUiLCJ1c2Vyczp1cGRhdGUiLCJ1c2VyczpyZWFkIiwidXNlcnM6ZGVsZXRlIiwiYXV0aDpsb2dvdXQiXSwiZXhwIjoxNzcyMDM2NTEwLCJ0eXBlIjoiYWNjZXNzIn0.oCT_o6daHTa6rGIZ_bEE8G0SMoIdlAUjqG2KDs9e-ls"))

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())