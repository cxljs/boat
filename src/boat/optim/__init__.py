"""Agent optimization for boat.

Optimization is search over an agent's configuration space against a metric. Every
optimizer here is the same loop - propose -> run -> evaluate -> select - reusing the
``boat.eval`` module to score candidates. It is active/online: every proposed
candidate is executed on the tasks and judged.

    >>> from boat.eval import EvalRunner, LLMEvalJudge, load_builtin_dataset, AgentConfig
    >>> from boat.optim import ReflectiveOptimizer
    >>>
    >>> runner = EvalRunner(judge=LLMEvalJudge(model_client))
    >>> dataset = load_builtin_dataset("quick_v1")
    >>> opt = ReflectiveOptimizer(runner, dataset, reflector=model_client, rounds=3)
    >>> result = await opt.optimize(AgentConfig(name="seed", system_prompt="You are helpful."))
    >>> print(result.best.system_prompt, result.eval_count)

The optimizable surface is declared via an ``OptimizationSpec`` of ``Tunable``s, so
you can optimize instructions (free-form), skills (free-form SKILL.md text), tool
descriptions (free-form), or tool selection / model (catalog-constrained).
"""

from .base import BaseOptimizer, Candidate, CostLog, OptimizationResult
from .gepa_adapter import (
    GEPA_AVAILABLE,
    BoatGepaAdapter,
    GepaRunResult,
    optimize_with_gepa,
)
from .mipro import MIPROOptimizer
from .reflective import ReflectiveOptimizer
from .reflective_pareto import ReflectiveParetoOptimizer, pareto_frontier
from .spec import (
    CatalogEntry,
    Component,
    Edit,
    InstructionTunable,
    Operation,
    OptimizationSpec,
    ProposalMode,
    SkillTunable,
    ToolDescriptionTunable,
    ToolSelectionTunable,
    Tunable,
)
from .trace import OptimizationTrace, load_trace, task_record

__all__ = [
    # loop
    "BaseOptimizer",
    "ReflectiveOptimizer",
    "ReflectiveParetoOptimizer",
    "MIPROOptimizer",
    "Candidate",
    "OptimizationResult",
    "CostLog",
    "pareto_frontier",
    # replayable record of a run
    "OptimizationTrace",
    "load_trace",
    "task_record",
    # real GEPA (optional dependency)
    "optimize_with_gepa",
    "BoatGepaAdapter",
    "GepaRunResult",
    "GEPA_AVAILABLE",
    # optimizable surface
    "OptimizationSpec",
    "Tunable",
    "InstructionTunable",
    "SkillTunable",
    "ToolDescriptionTunable",
    "ToolSelectionTunable",
    "Component",
    "Edit",
    "Operation",
    "ProposalMode",
    "CatalogEntry",
]
