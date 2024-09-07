"""Custom exception definitions."""


class DatabaseSessionInitialisationError(Exception):
    """Raise custom exception when database session uninitialised."""

    def __str__(self) -> str:
        """Error representation.

        Returns
        -------
        str
            Error message.
        """
        return "Database session manager is not initialised. Please initialise."
