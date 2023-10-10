import logging
import traceback

from bs4 import BeautifulSoup

from server.tasks.classes import LoaderValue, ReturnedValue, ErrorValue, ContactsData
from server.tasks.utils import download

logger = logging.getLogger(__name__)

async def contacts_parse(url: str, headers: dict) -> ReturnedValue:
    try:
        logger.info('Downloading Bastion contacts data')
        response: ReturnedValue = await download(url=url, headers=dict())
        if response.is_success:
            logger.info('Download Bastion complete')
            download_data: LoaderValue = response.data

            soup = BeautifulSoup(download_data.content, 'html.parser')
            items = soup.find('div', class_='mb-3 relative z-10')

            with open('bastion.txt', 'w') as file:
                file.write(download_data.content)

            # addr = items.find('div', class_='text-white relative z-10 mb-3')
            # item = addr.find_all('p')
            print(items)

                      # postal = item.find_all('span')[1].text
            # print(postal)

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
            error_data.message = f'Parsing contacts for Bastion is uncompilable, {error_data.message}'
            return ReturnedValue(
                is_success=False,
                data=error_data
            )

    except Exception as error:
        return ReturnedValue(
            is_success=False,
            data=ErrorValue(
                message=f'Parsing contacts for Bastion is uncompilable, error: {str(error)}',
                traceback=traceback.format_exc(limit=None, chain=True)
            )
        )
