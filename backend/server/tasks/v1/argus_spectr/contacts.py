import logging
import traceback

from bs4 import BeautifulSoup

from server.tasks.classes import LoaderValue, ReturnedValue, ErrorValue, ContactsData
from server.tasks.utils import download

logger = logging.getLogger(__name__)

async def contacts_parse(url: str, headers: dict) -> ReturnedValue:
    try:
        logger.info('Downloading Argus contacts data')
        response: ReturnedValue = await download(url=url, headers=dict())
        if response.is_success:
            logger.info('Download Argus complete')
            download_data: LoaderValue = response.data

            soup = BeautifulSoup(download_data.content, 'html.parser')
            addr = soup.find('div', class_='DraftEditor-editorContainer')
            item = addr.find('div', class_='_17fgIIn___block normal')

            print(item)
            # postal = item.find('span', {'itemprop': 'postalCode'}).text
            # region = item.find('span', {'itemprop': 'addressRegion'}).text
            # locality = item.find('span', {'itemprop': 'addressLocality'}).text
            # street = item.find('span', {'itemprop': 'streetAddress'}).text
            # phone = item.find('span', {'itemprop': 'telephone'}).text
            # mail = item.find('a', {'itemprop': 'email'})['href'].split(':')[-1]

            return ReturnedValue(
                is_success=True,
                data=download_data
            )
            # return ReturnedValue(
            #     is_success=True,
            #     data=ContactsData(
            #         postal=postal,
            #         region=region,
            #         locality=locality,
            #         street=street,
            #         phone=phone,
            #         mail=mail
            #     )
            # )

        else:
            error_data: ErrorValue = response.data
            error_data.message = f'Parsing contacts for Argus is uncompilable, {error_data.message}'
            return ReturnedValue(
                is_success=False,
                data=error_data
            )

    except Exception as error:
        return ReturnedValue(
            is_success=False,
            data=ErrorValue(
                message=f'Parsing contacts for Argus is uncompilable, error: {str(error)}',
                traceback=traceback.format_exc(limit=None, chain=True)
            )
        )
