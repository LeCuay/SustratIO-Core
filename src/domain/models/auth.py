"""
Authentication and authorization data modeling.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthenticatedUser:
    """
    Represents a user within the app with a set of permissions.

    :param id: Unique identifier for the user.
    :type id: str
    :param email: The email associated to the user.
    :type email: str
    :param role: The role for the user.
    :type role: str
    """

    id: str
    email: str
    role: str
