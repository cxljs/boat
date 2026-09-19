"""
Orchestration patterns - autonomous control flow.

This package provides orchestration patterns for managing multi-agent interactions
with termination conditions and cancellation support.
"""

from ..termination import (
    BaseTermination,
    CancellationTermination,
    CompositeTermination,
    ExternalTermination,
    FunctionCallTermination,
    HandoffTermination,
    MaxMessageTermination,
    TextMentionTermination,
    TimeoutTermination,
    TokenUsageTermination,
)
from .ai import AIOrchestrator
from .base import BaseOrchestrator
from .plan import PlanBasedOrchestrator
from .round_robin import RoundRobinOrchestrator

__all__ = [
    # Orchestrators
    "BaseOrchestrator",
    "RoundRobinOrchestrator",
    "AIOrchestrator",
    "PlanBasedOrchestrator",
    # Termination conditions
    "BaseTermination",
    "MaxMessageTermination",
    "TextMentionTermination",
    "TokenUsageTermination",
    "TimeoutTermination",
    "HandoffTermination",
    "ExternalTermination",
    "CancellationTermination",
    "FunctionCallTermination",
    "CompositeTermination",
]
