"""
Authentication errors on the adapters.
"""

from domain.exceptions import DomainError


class JWTAuthenticationError(DomainError):
    """Raised when failed to authenticate a user using a JWT token."""
