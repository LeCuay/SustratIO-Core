"""
Domain logic-related exceptions.
"""


class DomainError(Exception):
    """Embodies all exceptions within the domain logic."""


class ValidationError(DomainError):
    """Data validation exceptions."""
