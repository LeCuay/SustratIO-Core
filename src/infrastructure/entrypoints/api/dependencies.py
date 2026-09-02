from typing import Annotated

from fastapi import Depends

from domain.ports.auth.jwt_auth import AsymmetricTokenServicePort


def get_token_service() -> AsymmetricTokenServicePort:
    """
    Dependency injection for asymmetric authentication.

    :return: The asymmetric service instance.
    :rtype: :class:`AsymmetricTokenServicePort`
    """

    from infrastructure.adapters.jwt_asymmetric import Auth0RS256TokenAdapter

    return Auth0RS256TokenAdapter()


TokenServiceDeps = Annotated[
    AsymmetricTokenServicePort, Depends(get_token_service)
]
