"""
Contains the launcher creation logic for the API integration.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi import FastAPI


def create_app() -> FastAPI:
    from fastapi import FastAPI

    from infrastructure.config import settings
    from infrastructure.entrypoints.api.v1.router import router_v1
    from infrastructure.logging_config import setup_logging

    setup_logging(log_level=settings.LOG_LEVEL)

    app = FastAPI(
        title='SustratIO API',
        description='Design to monitor, notify and track soil quality.',
        version='0.0.1',
    )
    app.include_router(router_v1)

    return app
