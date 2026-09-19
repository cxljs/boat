"""
Provides database-backed storage for agent runs, eval results,
datasets, and target configurations. Uses SQLModel with async
SQLAlchemy for database access.

Usage:
    from boat.store import BoatStore, get_default_store

    # Default SQLite store
    store = get_default_store()
    await store.save_agent_run(agent, response)

    # Custom connection
    store = BoatStore("postgresql+asyncpg://user:pass@host/db")
"""

from .models import (
    DBDataset,
    DBEvalResult,
    DBEvalRun,
    DBRun,
    DBTargetConfig,
    DBTask,
)
from .store import BoatStore, get_default_store

__all__ = [
    "BoatStore",
    "get_default_store",
    "DBRun",
    "DBDataset",
    "DBTask",
    "DBTargetConfig",
    "DBEvalRun",
    "DBEvalResult",
]
