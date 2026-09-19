"""
A lightweight framework for building LLM agents.
Supports tool calling, memory, streaming, and multi-agent orchestration.
"""

# Auto-instrument with OpenTelemetry if enabled
import os

if os.getenv("BOAT_ENABLE_OTEL", "false").lower() in ("true", "1", "yes"):
    try:
        from .otel import auto_instrument

        auto_instrument()
    except Exception:
        pass  # Gracefully continue if instrumentation fails

# Agent implementations
from .agents import (
    Agent,
    AgentConfigurationError,
    AgentError,
    AgentExecutionError,
    AgentToolError,
    BaseAgent,
)

# Cancellation support
from .cancellation_token import CancellationToken

# Compaction strategies
from .compaction import (
    CompactionStrategy,
    HeadTailCompaction,
    NoCompaction,
    SlidingWindowCompaction,
)

# Component configuration system
from .component_config import (
    Component,
    ComponentBase,
    ComponentFromConfig,
    ComponentLoader,
    ComponentModel,
    ComponentSchemaType,
    ComponentToConfig,
    ComponentType,
)

# Context system
from .context import (
    AgentContext,
    ToolApprovalRequest,
    ToolApprovalResponse,
)

# Evaluation system
from .eval import (
    AgentEvalTarget,
    EvalJudge,
    EvalRunner,
    LLMEvalJudge,
    ModelEvalTarget,
    OrchestratorEvalTarget,
    Target,
)

# Deterministic loop hooks
from .hooks import (
    BaseEndHook,
    BaseStartHook,
    CompletionCheckHook,
    LLMCompletionCheckHook,
    LoopContext,
    MaxRestartsTermination,
    PlanningHook,
    TerminationCondition,
)

# Instructions
from .instructions import get_instructions

# LLM clients
from .llm import (
    AuthenticationError,
    BaseChatCompletionClient,
    BaseChatCompletionError,
    InvalidRequestError,
    OpenAIChatCompletionClient,
    RateLimitError,
)

# Memory system
from .memory import (
    BaseMemory,
    FileMemory,
    ListMemory,
    MemoryContent,
    MemoryQueryResult,
)

# Core message types
from .messages import (
    AssistantMessage,
    Message,
    MultiModalMessage,
    SystemMessage,
    ToolCallRequest,
    ToolMessage,
    UserMessage,
)

# Middleware system
from .middleware import (
    BaseMiddleware,
    GuardrailMiddleware,
    LoggingMiddleware,
    MetricsMiddleware,
    MiddlewareChain,
    MiddlewareContext,
    PIIRedactionMiddleware,
    RateLimitMiddleware,
)

# Orchestration patterns
from .orchestration import (
    BaseOrchestrator,
    BaseTermination,
    CancellationTermination,
    CompositeTermination,
    ExternalTermination,
    FunctionCallTermination,
    HandoffTermination,
    MaxMessageTermination,
    RoundRobinOrchestrator,
    TextMentionTermination,
    TimeoutTermination,
    TokenUsageTermination,
)

# Tool system
from .tools import (
    ApprovalMode,
    BaseTool,
    FunctionTool,
    tool,
)

# Core data types
from .types import (
    AgentEvent,
    AgentResponse,
    ChatCompletionChunk,
    ChatCompletionResult,
    OrchestrationEvent,
    OrchestrationResponse,
    StopMessage,
    ToolResult,
    Usage,
)


def _detect_version() -> str:
    """Version from installed package metadata; pyproject.toml is the source
    of truth. Falls back for a source tree that was never installed."""
    from importlib.metadata import PackageNotFoundError, version

    try:
        return version("boat")
    except PackageNotFoundError:  # pragma: no cover - source checkout only
        return "0.0.0+unknown"


__version__: str = _detect_version()

__all__ = [
    # Context
    "AgentContext",
    "ToolApprovalRequest",
    "ToolApprovalResponse",
    # Compaction
    "CompactionStrategy",
    "HeadTailCompaction",
    "SlidingWindowCompaction",
    "NoCompaction",
    # Messages
    "Message",
    "SystemMessage",
    "UserMessage",
    "AssistantMessage",
    "ToolMessage",
    "MultiModalMessage",
    "ToolCallRequest",
    # Types
    "Usage",
    "ToolResult",
    "AgentResponse",
    "ChatCompletionResult",
    "ChatCompletionChunk",
    "AgentEvent",
    "StopMessage",
    "OrchestrationResponse",
    "OrchestrationEvent",
    # Cancellation
    "CancellationToken",
    # Hooks
    "BaseEndHook",
    "BaseStartHook",
    "CompletionCheckHook",
    "LLMCompletionCheckHook",
    "LoopContext",
    "MaxRestartsTermination",
    "PlanningHook",
    "TerminationCondition",
    # Component Configuration
    "ComponentModel",
    "ComponentFromConfig",
    "ComponentToConfig",
    "ComponentSchemaType",
    "ComponentLoader",
    "ComponentBase",
    "Component",
    "ComponentType",
    # Agents
    "BaseAgent",
    "Agent",
    "AgentError",
    "AgentExecutionError",
    "AgentConfigurationError",
    "AgentToolError",
    # Tools
    "BaseTool",
    "FunctionTool",
    "ApprovalMode",
    "tool",
    # Memory
    "BaseMemory",
    "MemoryContent",
    "MemoryQueryResult",
    "ListMemory",
    "FileMemory",
    # LLM
    "BaseChatCompletionClient",
    "BaseChatCompletionError",
    "RateLimitError",
    "AuthenticationError",
    "InvalidRequestError",
    "OpenAIChatCompletionClient",
    # Orchestration
    "BaseOrchestrator",
    "RoundRobinOrchestrator",
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
    # Evaluation
    "Target",
    "EvalJudge",
    "EvalRunner",
    "AgentEvalTarget",
    "ModelEvalTarget",
    "OrchestratorEvalTarget",
    "LLMEvalJudge",
    # Instructions
    "get_instructions",
    # Middleware
    "BaseMiddleware",
    "MiddlewareContext",
    "MiddlewareChain",
    "LoggingMiddleware",
    "RateLimitMiddleware",
    "PIIRedactionMiddleware",
    "GuardrailMiddleware",
    "MetricsMiddleware",
]
