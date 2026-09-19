"""
MCP (Model Context Protocol) integration for Boat.

This module provides integration with MCP servers, allowing agents to use
tools from any MCP-compliant server as if they were native Boat tools.

Example:
    ```python
    from boat.tools import create_mcp_tools, StdioServerConfig

    # Configure MCP server
    config = StdioServerConfig(
        server_id="filesystem",
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
    )

    # Create tools
    manager, tools = await create_mcp_tools([config])

    # Use with agent
    agent = Agent(name="mcp_agent", tools=tools, ...)
    ```
"""

from .client import MCPClientManager
from .config import (
    HTTPServerConfig,
    InMemoryServerConfig,
    MCPServerConfig,
    StdioServerConfig,
    TransportType,
)
from .integration import create_mcp_tools
from .tap import WireFrame, WireTap
from .tool import MCPTool

__all__ = [
    "MCPTool",
    "MCPClientManager",
    "MCPServerConfig",
    "StdioServerConfig",
    "HTTPServerConfig",
    "InMemoryServerConfig",
    "TransportType",
    "WireFrame",
    "WireTap",
    "create_mcp_tools",
]
