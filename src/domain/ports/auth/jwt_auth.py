from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from domain.models.auth import AuthenticatedUser


class AsymmetricTokenServicePort(Protocol):
    """
    Port for the implementation of OAuth2 via JWT authentication via Asymmetric
    Key Pair.
    """

    def decode_and_verify_token(self, token: str) -> AuthenticatedUser:
        """
        Given a token it returns an :class:`AuthenticatedUser`.

        :param token: Received token.
        :type token: str
        :return: The user from this token.
        :rtype: :class:`AuthenticatedUser`
        """
        ...
