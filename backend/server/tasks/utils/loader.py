import traceback

import aiohttp

from server.tasks.classes import ReturnedValue, LoaderValue, ErrorValue


async def download(url: str, headers: dict, timeout: int = 60, verify_ssl: bool = False) -> ReturnedValue:
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=verify_ssl)) as session:
            async with session.get(url=url, timeout=timeout, headers=headers) as response:
                if response.status == 200:
                    return ReturnedValue(
                        is_success=True,
                        data=LoaderValue(
                            response_code=response.status,
                            content=await response.text()
                        )
                    )
                else:
                    return ReturnedValue(
                        is_success=False,
                        data=ErrorValue(
                            message=f'The resource returned an incorrect response code, '
                                    f'url: {url}, response_code: {response.status}',
                            traceback=None
                        )
                    )
    except Exception as error:
        return ReturnedValue(
            is_success=False,
            data=ErrorValue(
                message=f'Download function error: {str(error)}',
                traceback=traceback.format_exc(limit=None, chain=True)
            )
        )
