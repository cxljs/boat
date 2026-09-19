"""
Memory system.

Provides persistent storage and retrieval capabilities for agent context,
enabling agents to maintain continuity across conversations.
"""

from .base import BaseMemory, FileMemory, ListMemory, MemoryContent, MemoryQueryResult

# The chromadb module imports cleanly without the optional dependency installed;
# ChromaDBMemory raises a clear ImportError on instantiation instead.
from .chromadb import (
    HAS_CHROMADB,
    ChromaDBMemory as ChromaDBMemory,
    ChromaDBMemoryConfig as ChromaDBMemoryConfig,
)

__all__ = [
    "BaseMemory",
    "MemoryContent",
    "MemoryQueryResult",
    "ListMemory",
    "FileMemory",
    "HAS_CHROMADB",
    "ChromaDBMemory",
    "ChromaDBMemoryConfig",
]
