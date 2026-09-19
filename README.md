# Boat

Boat is a multi-agent framework.

## Installation

```bash
pip install boat
```

**Requirements:**

- Python 3.10+
- OpenAI API key (set `OPENAI_API_KEY` environment variable)

**Optional extras:**

```bash
pip install "boat[web]"      # Web UI, MCP playground, evaluation dashboard
pip install "boat[mcp]"      # MCP client (requires mcp>=2.0.0, protocol 2026-07-28)
pip install "boat[persist]"  # Run and eval persistence behind the History page
```

## Quick Start

```python
from boat import Agent, OpenAIChatCompletionClient

def get_weather(location: str) -> str:
    """Get current weather for a given location."""
    return f"The weather in {location} is sunny, 75°F"

# Create an agent
agent = Agent(
    name="assistant",
    instructions="You are helpful. Use tools when appropriate.",
    model_client=OpenAIChatCompletionClient(model="gpt-4.1-mini"),
    tools=[get_weather]
)

# Use the agent
response = await agent.run("What's the weather in Paris?")
print(response.messages[-1].content)
```

## What's Included

Boat implements complete, working examples of:

- **Agents** - Reasoning loops, tool calling, memory, middleware, streaming
- **Orchestration** - Round-robin, AI-driven, and plan-based multi-agent coordination
- **Tools** - Built-in tools (file ops, code execution, search, todos, skills)
- **MCP** - Client plus a playground for testing servers with full wire visibility
- **Evaluation** - LLM-as-judge patterns, reference-based validation, datasets and batch runs
- **Web UI** - Auto-discovery, streaming chat, run history, MCP playground

## Project Structure

```
boat/
├── src/boat/
│   ├── agents/            # Agent implementations
│   ├── orchestration/     # Autonomous coordination
│   ├── tools/             # Tool system and built-in tools
│   ├── eval/              # Evaluation framework
│   ├── webui/             # Web interface with auto-discovery
│   ├── llm/               # LLM clients (OpenAI-compatible)
│   ├── memory/            # Memory implementations
│   └── termination/       # Termination conditions
└── tests/                 # Comprehensive test suite
```

## Web UI

Launch the web interface with auto-discovery of agents and orchestrators:

```bash
boat ui
```

Features streaming responses, real-time debug events, and session management.

## Development

```bash
# Clone repository
git clone https://github.com/cxljs/boat.git
cd boat

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
python -m pytest tests/

# Type checking
python -m mypy src/
python -m pyright src/

# Linting and formatting
ruff check src/ tests/
ruff format src/ tests/
```
