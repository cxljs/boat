"""
Termination conditions for orchestration patterns.

This package provides various termination conditions that determine when
orchestration should stop.
"""

from .base import BaseTermination
from .cancellation import CancellationTermination
from .composite import CompositeTermination
from .external import ExternalTermination
from .function_call import FunctionCallTermination
from .handoff import HandoffTermination
from .max_message import MaxMessageTermination
from .text_mention import TextMentionTermination
from .timeout import TimeoutTermination
from .token_usage import TokenUsageTermination

__all__ = [
    # Base
    "BaseTermination",
    # Individual conditions
    "MaxMessageTermination",
    "TextMentionTermination",
    "TokenUsageTermination",
    "TimeoutTermination",
    "HandoffTermination",
    "ExternalTermination",
    "CancellationTermination",
    "FunctionCallTermination",
    # Composite
    "CompositeTermination",
]
