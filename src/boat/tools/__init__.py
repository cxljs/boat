"""
This module provides the foundation for tools that agents can use to
interact with the world.
"""

from .base import ApprovalMode, BaseTool, FunctionTool
from .coding_tools import create_coding_tools

# Context engineering tools
from .context_tools import (
    MultiEditTool,
    SkillsTool,
    TaskTool,
    TodoListSessionsTool,
    TodoReadTool,
    TodoWriteTool,
    create_context_engineering_tools,
    create_multi_edit_tool,
    create_skills_tool,
    create_task_tool,
    create_todo_tools,
    get_current_session_id,
    list_todo_sessions,
    set_session_id,
    set_todo_path,
)
from .core_tools import (
    CalculatorTool,
    DateTimeTool,
    JSONParserTool,
    RegexTool,
    TaskStatusTool,
    ThinkTool,
    create_core_tools,
)
from .decorator import tool
from .memory_tool import MemoryBackend, MemoryTool

# MCP support (optional dependency)
try:
    from .mcp import (
        HTTPServerConfig,
        InMemoryServerConfig,
        MCPClientManager,
        MCPServerConfig,
        MCPTool,
        StdioServerConfig,
        TransportType,
        WireTap,
        create_mcp_tools,
    )

    MCP_AVAILABLE = True
except ImportError as e:
    # Only "mcp is not installed" is a valid optional-extra condition. An
    # installed-but-incompatible SDK (mcp 1.x) must fail loudly, not become
    # a sea of None symbols.
    import importlib.util

    if importlib.util.find_spec("mcp") is not None:
        raise ImportError(
            "boat MCP integration requires mcp>=2.0.0 "
            "(protocol 2026-07-28). Upgrade with: pip install 'mcp>=2.0.0'"
        ) from e
    MCP_AVAILABLE = False
    MCPTool = None  # type: ignore
    MCPClientManager = None  # type: ignore
    MCPServerConfig = None  # type: ignore
    StdioServerConfig = None  # type: ignore
    HTTPServerConfig = None  # type: ignore
    InMemoryServerConfig = None  # type: ignore
    WireTap = None  # type: ignore
    TransportType = None  # type: ignore
    create_mcp_tools = None  # type: ignore

__all__ = [
    "ApprovalMode",
    "BaseTool",
    "FunctionTool",
    "tool",
    "create_core_tools",
    "create_coding_tools",
    "MemoryTool",
    "MemoryBackend",
    "ThinkTool",
    "TaskStatusTool",
    "CalculatorTool",
    "DateTimeTool",
    "JSONParserTool",
    "RegexTool",
    # Context engineering tools
    "TaskTool",
    "TodoWriteTool",
    "TodoReadTool",
    "TodoListSessionsTool",
    "SkillsTool",
    "MultiEditTool",
    "create_task_tool",
    "create_todo_tools",
    "create_skills_tool",
    "create_multi_edit_tool",
    "create_context_engineering_tools",
    "set_todo_path",
    "set_session_id",
    "get_current_session_id",
    "list_todo_sessions",
    # MCP integration
    "MCPTool",
    "MCPClientManager",
    "MCPServerConfig",
    "StdioServerConfig",
    "HTTPServerConfig",
    "InMemoryServerConfig",
    "WireTap",
    "TransportType",
    "create_mcp_tools",
    "MCP_AVAILABLE",
]
