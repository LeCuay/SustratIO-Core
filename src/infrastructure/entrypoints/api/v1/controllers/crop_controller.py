from typing import Annotated

from fastapi import APIRouter, Body, status

from infrastructure.entrypoints.api.v1.dtos.request.crop_requests import (
    CreateCropRequest,
)
from infrastructure.entrypoints.api.v1.dtos.response.crop_responses import (
    SingleCropResponse,
)

crops_router = APIRouter(prefix='/crops', tags=['Crops'])


@crops_router.post(
    '/',
    summary='Creates a single crop',
    response_model=SingleCropResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_crop(
    data: Annotated[
        CreateCropRequest,
        Body(description='Data for the crop creation.'),
    ],
):
    """
    Creates a single crop with the given data.
    """
