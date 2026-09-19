"""
Evaluation system for boat.

This module provides a complete evaluation framework for testing
and comparing different boat components (agents, models, orchestrators).

    >>> from boat.eval import (
    ...     AgentConfig, EvalRunner, Dataset, EvalResults,
    ...     BoatTarget, LLMEvalJudge, load_builtin_dataset,
    ... )
    >>>
    >>> # Load dataset
    >>> dataset = load_builtin_dataset("coding_v1")
    >>>
    >>> # Define configurations to compare
    >>> configs = [
    ...     AgentConfig(name="baseline", compaction=None),
    ...     AgentConfig(name="head_tail", compaction="head_tail"),
    ... ]
    >>>
    >>> # Run evaluation
    >>> runner = EvalRunner(judge=LLMEvalJudge(model_client))
    >>> results = await runner.run(dataset, configs)
    >>>
    >>> # Analyze results
    >>> print_results(results)
"""

# Analysis
from .analysis import (
    format_file_read_analysis,
    format_summary_table,
    format_task_breakdown,
    format_token_growth,
    print_results,
)

# Base classes
from .base import EvalJudge, Target

# Config
from .config import AgentConfig

# Dataset
from .dataset import Dataset, list_builtin_datasets, load_builtin_dataset

# Judges
from .judges import (
    BaseEvalJudge,
    CompositeJudge,
    ContainsJudge,
    ExactMatchJudge,
    FuzzyMatchJudge,
    LLMEvalJudge,
)

# Middleware
from .middleware import RunMiddleware

# Results
from .results import (
    EvalResults,
    TargetSummary,
    TaskResult,
    list_eval_results,
    load_eval_results,
)

# Runner
from .runner import EvalRunner, Runnable

# Targets
from .targets import (
    AgentEvalTarget,
    BoatTarget,
    CallableTarget,
    ClaudeCodeTarget,
    ModelEvalTarget,
    OrchestratorEvalTarget,
)

__all__ = [
    # Base classes
    "Target",
    "EvalJudge",
    # Runner
    "EvalRunner",
    "Runnable",
    # Targets
    "AgentEvalTarget",
    "ModelEvalTarget",
    "OrchestratorEvalTarget",
    "BoatTarget",
    "ClaudeCodeTarget",
    "CallableTarget",
    # Judges
    "BaseEvalJudge",
    "LLMEvalJudge",
    "ExactMatchJudge",
    "FuzzyMatchJudge",
    "ContainsJudge",
    "CompositeJudge",
    # Dataset
    "Dataset",
    "load_builtin_dataset",
    "list_builtin_datasets",
    # Config
    "AgentConfig",
    # Results
    "TaskResult",
    "TargetSummary",
    "EvalResults",
    "load_eval_results",
    "list_eval_results",
    # Middleware
    "RunMiddleware",
    # Analysis
    "format_summary_table",
    "format_task_breakdown",
    "format_file_read_analysis",
    "format_token_growth",
    "print_results",
]
