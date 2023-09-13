import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from server.config import get_database_config, ServerAPIConfig
from server import database as database
from server.database import get_async_session

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
                'version': 0.01,
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


def run(config_server: ServerAPIConfig = None) -> None:
    config = get_database_config()
    print(database.registry_database(database_config=config))
    uvicorn.run(api_server, host=config_server.host, port=config_server.port, log_config=None)
