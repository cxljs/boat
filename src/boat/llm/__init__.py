"""
Provides unified interface for OpenAI-compatible language model providers
with standardized response formats and error handling.
"""

from .base import (
    AuthenticationError,
    BaseChatCompletionClient,
    BaseChatCompletionError,
    InvalidRequestError,
    RateLimitError,
)
from .openai import OpenAIChatCompletionClient

__all__ = [
    "BaseChatCompletionClient",
    "BaseChatCompletionError",
    "RateLimitError",
    "AuthenticationError",
    "InvalidRequestError",
    "OpenAIChatCompletionClient",
]
