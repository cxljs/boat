"""
Tests for model client implementations.

This module tests various LLM client implementations including:
- OpenAI
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from pydantic import BaseModel

from boat.llm import (
    BaseChatCompletionClient,
    OpenAIChatCompletionClient,
)
from boat.messages import (
    AssistantMessage,
    SystemMessage,
    ToolCallRequest,
    ToolMessage,
    UserMessage,
)


class TestOutput(BaseModel):
    """Test structured output model."""

    name: str
    value: int


class TestModelClients:
    """Test suite for model client implementations."""

    @pytest.fixture
    def messages(self):
        """Sample messages for testing."""
        return [
            SystemMessage(content="You are a helpful assistant", source="system"),
            UserMessage(content="Hello, how are you?", source="user"),
        ]

    def test_client_inheritance(self):
        """Test that all clients inherit from BaseChatCompletionClient."""
        assert issubclass(OpenAIChatCompletionClient, BaseChatCompletionClient)

    def test_client_initialization(self):
        """Test client initialization with various parameters."""
        # OpenAI client
        openai_client = OpenAIChatCompletionClient(model="gpt-4", api_key="test-key")
        assert openai_client.model == "gpt-4"
        assert openai_client.api_key == "test-key"

    def test_component_types(self):
        """Test that all clients have correct component type."""
        openai_client = OpenAIChatCompletionClient(api_key="test")

        assert openai_client.component_type == "model_client"

    @pytest.mark.asyncio
    async def test_openai_message_conversion(self, messages):
        """Test OpenAI message format conversion."""
        client = OpenAIChatCompletionClient(api_key="test")

        # Test basic message conversion
        converted = client._convert_messages_to_api_format(messages)
        assert len(converted) == 2
        assert converted[0]["role"] == "system"
        assert converted[0]["content"] == "You are a helpful assistant"
        assert converted[1]["role"] == "user"
        assert converted[1]["content"] == "Hello, how are you?"

        # Test with tool calls
        messages_with_tools = messages + [
            AssistantMessage(
                content="I'll check the weather",
                source="assistant",
                tool_calls=[
                    ToolCallRequest(
                        tool_name="get_weather",
                        parameters={"location": "Paris"},
                        call_id="call_123",
                    )
                ],
            ),
            ToolMessage(
                content="It's sunny in Paris",
                tool_call_id="call_123",
                tool_name="get_weather",
                success=True,
                source="tool",
            ),
        ]

        converted = client._convert_messages_to_api_format(messages_with_tools)
        assert len(converted) == 4
        assert "tool_calls" in converted[2]
        assert converted[3]["role"] == "tool"
        assert converted[3]["tool_call_id"] == "call_123"

    @pytest.mark.asyncio
    async def test_openai_create_with_mock(self, messages):
        """Test OpenAI client create method with mocked API."""
        with patch("boat.llm.openai.AsyncOpenAI") as MockOpenAI:
            # Setup mock
            mock_client = AsyncMock()
            MockOpenAI.return_value = mock_client

            mock_response = MagicMock()
            mock_response.choices = [MagicMock()]
            mock_response.choices[0].message.content = "Hello! I'm doing well."
            mock_response.choices[0].message.tool_calls = None
            mock_response.choices[0].finish_reason = "stop"
            mock_response.model = "gpt-4"
            mock_response.usage.prompt_tokens = 10
            mock_response.usage.completion_tokens = 5

            mock_client.chat.completions.create = AsyncMock(return_value=mock_response)

            # Test
            client = OpenAIChatCompletionClient(model="gpt-4", api_key="test")
            result = await client.create(messages)

            assert result.message.content == "Hello! I'm doing well."
            assert result.model == "gpt-4"
            assert result.usage.tokens_input == 10
            assert result.usage.tokens_output == 5

    def test_serialization_configs(self):
        """Test that all clients can be serialized to config."""
        # OpenAI
        openai_client = OpenAIChatCompletionClient(model="gpt-4", api_key="test-key")
        openai_config = openai_client._to_config()
        assert openai_config.model == "gpt-4"
        assert openai_config.api_key == "test-key"

    def test_deserialization_from_config(self):
        """Test that clients can be deserialized from config."""
        # OpenAI
        openai_client = OpenAIChatCompletionClient(model="gpt-4", api_key="test-key")
        config = openai_client._to_config()
        restored = OpenAIChatCompletionClient._from_config(config)
        assert restored.model == "gpt-4"
        assert restored.api_key == "test-key"

    @pytest.mark.asyncio
    async def test_streaming_interface(self):
        """Test that all clients implement the streaming interface."""
        clients = [
            OpenAIChatCompletionClient(api_key="test"),
        ]

        for client in clients:
            assert hasattr(client, "create_stream")
            assert callable(client.create_stream)

    def test_cost_estimation(self):
        """Test cost estimation methods."""
        # OpenAI cost estimation
        openai_client = OpenAIChatCompletionClient(model="gpt-4", api_key="test")

        # Mock usage object
        mock_usage = MagicMock()
        mock_usage.prompt_tokens = 100
        mock_usage.completion_tokens = 50

        cost = openai_client._estimate_cost(mock_usage)
        assert isinstance(cost, float)
        assert cost > 0
