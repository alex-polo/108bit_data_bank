import logging

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from server.config import get_database_config, ServerAPIConfig, get_api_server_config
from server import database as database
from server.database import get_async_session


logger = logging.getLogger()

api_server = FastAPI()


# @api_server.on_event("startup")
# async def startup(session: AsyncSession = Depends(get_async_session)) -> None:
#     pass


@api_server.get('/')
async def home(session: AsyncSession = Depends(get_async_session)):
    try:
        # res = await session.execute(select(Sites))
        return JSONResponse(
            status_code=200,
            content={
                'application': 'Data Bank',
                'version': '0.01a',
                'amount_resources': 0
            })
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail={
                'application': 'Data Bank',
                'version': '0.01a',
                'data': error
            })


def registry_middleware(config_server: ServerAPIConfig):
    api_server.add_middleware(
        CORSMiddleware,
        allow_origins=config_server.allow_origins,
        allow_credentials=config_server.allow_credentials,
        allow_methods=config_server.allow_methods,
        allow_headers=config_server.allow_headers,
    )


def run() -> None:
    server_config = get_api_server_config()
    logger.debug(f'Configuration API Server: {server_config}')

    database_config = get_database_config()

    database.registry_database(database_config=database_config)
    uvicorn.run(
        api_server,
        host=server_config.host,
        port=server_config.port,
        log_config='etc/server_logging.ini',
        access_log=True
    )
