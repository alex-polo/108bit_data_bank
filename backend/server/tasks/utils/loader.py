import aiohttp


def download(url: str, headers: dict, timeout: int = 60, verify_ssl: bool = False) -> None:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=verify_ssl)) as session:
        async with session.get(url=url, timeout=timeout, headers=headers) as response:

            if response.status == 200:
                # return SuccessResponse(status=Status.Ok, content=await response.text())
                pass
            else:
                # logger.error(f'Failed to download site content: {site.get("site_name")}, '
                #              f'response code: {response.status}, url: "{site.get("url")}"', )

                # return loader_error_response(site=site,
                #                              description=f'От сайта "{site.get("site_name")}" получен неверный '
                #                                          f'код ответа.\nURL: {site.get("url")}'
                #                                          f'\nПолучен код ответа: {response.status}',
                #                              error_text=f'Полученный код ответа {response.status}',
                #                              text_details=None,
                #                              image_download_error=grubber_config.image_download_error)

                pass