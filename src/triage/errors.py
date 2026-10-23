class TriageError(Exception):
    """Base exception for triage service failures."""


class TriageUnavailableError(TriageError):
    """Temporary OpenAI, network, rate-limit, or timeout failure."""


class TriageConfigurationError(TriageError):
    """Configuration, authentication, or permission problem."""
