"""Quickstart: optimize an agent's instructions with the reflection loop.

Reuses the eval module to score candidates. Run:

    python -m boat.optim.examples.reflective_quickstart
"""

import asyncio

from boat.eval import AgentConfig, EvalRunner, LLMEvalJudge, load_builtin_dataset
from boat.llm import OpenAIChatCompletionClient
from boat.optim import (
    InstructionTunable,
    OptimizationSpec,
    ReflectiveOptimizer,
    ReflectiveParetoOptimizer,
)


def make_client() -> OpenAIChatCompletionClient:
    return OpenAIChatCompletionClient(model="gpt-4o-mini")


async def main() -> None:
    client = make_client()
    dataset = load_builtin_dataset("quick_v1")
    runner = EvalRunner(judge=LLMEvalJudge(client))

    seed = AgentConfig(
        name="seed",
        model_provider="openai",
        system_prompt="You are a helpful assistant.",
    )

    # Optimize instructions only (the simplest surface).
    spec = OptimizationSpec(tunables=[InstructionTunable()])

    opt = ReflectiveOptimizer(
        runner, dataset, spec, reflector=client, rounds=3, weak_k=2
    )
    result = await opt.optimize(seed)

    print(f"\nrollouts spent: {result.eval_count}")
    for c in sorted(result.pool, key=lambda c: c.avg, reverse=True):
        print(f"  {c.config.name:12s} avg={c.avg:5.2f}  parent={c.parent}")
    print(f"\nbest instructions:\n{result.best.system_prompt}")

    # Swap one knob to get Pareto-frontier selection - same loop, same seed.
    _ = ReflectiveParetoOptimizer  # identical call site, different select()


if __name__ == "__main__":
    asyncio.run(main())
