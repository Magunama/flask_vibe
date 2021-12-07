import aiohttp


class BaseRequest:
    @staticmethod
    async def post_json(url, headers=None, payload=None):
        async with aiohttp.ClientSession() as session:
            data = await session.request('POST', url, json=payload, headers=headers)
            return await data.json()

    @staticmethod
    async def get_json(url, headers=None, params=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, params=params) as response:
                return await response.json()

    @staticmethod
    async def get_text(url, headers=None, params=None):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, params=params) as response:
                return await response.text()
