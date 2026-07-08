# generative-engine-optimizer-skill

> **GenPark AI Agent Skill** -- Generative Engine / LLM Search Optimizer.

## Quick Start

```python
from client import GenerativeEngineOptimizerClient
client = GenerativeEngineOptimizerClient()
res = client.optimize_text("Eco Bottle", "A reusable bottle", ["best eco bottle"])
print(res["optimized_copy"])
```
