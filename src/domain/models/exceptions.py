"""
Domain model exceptions.
"""

from domain.exceptions import ValidationError


class NameTooLongError(ValidationError):
    """Raised when name exceeded characters limit."""

    def __init__(self, max_length: int, current_length: int):
        super().__init__(
            f'Name exceeded the maximum characters allowed ({max_length}).'
            f'Current: {current_length}'
        )


class UniqueNameTooLongError(ValidationError):
    """Raised when unique name exceeded characters limit."""

    def __init__(self, max_length: int, current_length: int):
        super().__init__(
            f'Name exceeded the maximum characters allowed ({max_length}).'
            f'Current: {current_length}'
        )
