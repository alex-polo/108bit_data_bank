import logging
import traceback

from bs4 import BeautifulSoup

from server.tasks.classes import LoaderValue, ReturnedValue, ErrorValue, ContactsData
from server.tasks.utils import download

logger = logging.getLogger(__name__)


async def contacts_parse(url: str, headers: dict) -> ReturnedValue:
    try:
        logger.info('Downloading Ironlogic contacts data')
        response: ReturnedValue = await download(url=url, headers=dict())
        if response.is_success:
            logger.info('Download Ironlogic complete')
            download_data: LoaderValue = response.data

            postal: str = '105122'
            region: str = 'Москва'
            locality = None
            street: str = 'Щелковское шоссе, д.5, стр.1, офис 723, склад 730'
            phone_1: str = '8(495)241-30-85'
            phone_2: str = '8(499)653-12-22'
            mail: str = 'moscow@ironlogic.ru'

            soup = BeautifulSoup(download_data.content, 'html.parser')
            items = soup.find('div', class_='usl_tab_cent')
            div_block = items.find('span').parent
            text: str = div_block.p.text

            if postal not in text or region not in text or street not in text or phone_1 not in text \
                    or phone_2 not in text or mail not in text:
                return ReturnedValue(
                    is_success=False,
                    data=ErrorValue(
                        message='No valid contact information',
                        traceback=None
                    )
                )

            return ReturnedValue(
                is_success=True,
                data=ContactsData(
                    postal=postal,
                    region=region,
                    locality=locality,
                    street=street,
                    phone=f'{phone_1}, {phone_2}',
                    mail=mail
                )
            )

        else:
            error_data: ErrorValue = response.data
            error_data.message = f'Parsing contacts for Ironlogic is uncompilable, {error_data.message}'
            return ReturnedValue(
                is_success=False,
                data=error_data
            )

    except Exception as error:
        return ReturnedValue(
            is_success=False,
            data=ErrorValue(
                message=f'Parsing contacts for Ironlogic is uncompilable, error: {str(error)}',
                traceback=traceback.format_exc(limit=None, chain=True)
            )
        )
