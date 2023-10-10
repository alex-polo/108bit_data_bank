import logging
import traceback

from bs4 import BeautifulSoup

from server.tasks.classes import LoaderValue, ReturnedValue, ErrorValue, ContactsData
from server.tasks.utils import download

logger = logging.getLogger(__name__)

async def contacts_parse(url: str, headers: dict) -> ReturnedValue:
    try:
        logger.info('Downloading Parsec contacts data')
        response: ReturnedValue = await download(url=url, headers=dict())
        if response.is_success:
            logger.info('Download Parsec complete')
            download_data: LoaderValue = response.data

            postal: str = '107553'
            region: str = 'Москва'
            locality = None
            street: str = 'ул. Большая Черкизовская, д. 24А, стр. 1, 7-й эт.'
            phone_1: str = '8 800 333-14-98'
            phone_2: str = '+7 495 565-31-12'
            mail: str = 'info@parsec.ru'

            soup = BeautifulSoup(download_data.content, 'html.parser')
            items = soup.find('span', class_='common contacts ')
            addr = items.find('div', class_='address')
            div_block = addr.find_all('p').parent
            text: str = div_block.p.text

            print(text)

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
            error_data.message = f'Parsing contacts for Parsec is uncompilable, {error_data.message}'
            return ReturnedValue(
                is_success=False,
                data=error_data
            )

    except Exception as error:
        return ReturnedValue(
            is_success=False,
            data=ErrorValue(
                message=f'Parsing contacts for Parsec is uncompilable, error: {str(error)}',
                traceback=traceback.format_exc(limit=None, chain=True)
            )
        )
