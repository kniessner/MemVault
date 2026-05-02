---
title: DeepSeek-R1
provider: DeepSeek
release_date: 2025-01-20
context: 131072
status: active
tags: [model, deepseek, open-weight, reasoning, chain-of-thought]
---

# DeepSeek-R1

> Open-source reasoning model that rivals o1 — shows its chain of thought, trained with RL, fully open weights.

## Overview

DeepSeek-R1 is a reasoning-focused LLM from DeepSeek AI that rivals OpenAI's o1 on math, code, and logic benchmarks. It's fully open-source (MIT license) and shows its thinking process, making it valuable for education and debugging.

| Attribute | Value |
|-----------|-------|
| **Provider** | DeepSeek AI |
| **Release** | January 2025 |
| **License** | MIT (fully open) |
| **Context** | 128K tokens |
| **Parameters** | 671B (37B active, MoE) |
| **Knowledge Cutoff** | July 2024 |

---

## Model Variants

| Model | Parameters | Active Parameters | Best For |
|-------|------------|-------------------|----------|
| **DeepSeek-R1** | 671B | 37B | Maximum reasoning |
| **DeepSeek-R1-Distill-Qwen-32B** | 32B | 32B | Balance of size/quality |
| **DeepSeek-R1-Distill-Llama-70B** | 70B | 70B | Llama ecosystem |
| **DeepSeek-R1-Distill-Qwen-14B** | 14B | 14B | Consumer GPUs |
| **DeepSeek-R1-Distill-Qwen-1.5B** | 1.5B | 1.5B | Edge devices |

---

## Specifications

| Capability | Description |
|------------|-------------|
| **Text** | ✅ Native |
| **Reasoning** | ✅ Visible chain-of-thought |
| **Vision** | ❌ Not native (V3 has vision) |
| **Coding** | ✅ Strong performance |
| **Math** | ✅ Frontier-level |
| **Long Context** | ✅ 128K |

---

## Performance Benchmarks

| Benchmark | DeepSeek-R1 | o1 | Claude 3.5 | GPT-4o |
|-----------|-------------|-----|------------|--------|
| MATH-500 | 97.3% | 96.4% | 71.1% | 76.6% |
| AIME 2024 | 79.8% | 74.6% | 16.0% | 9.3% |
| Codeforces (percentile) | 96.3% | 96.6% | — | — |
| MMLU | 90.8% | 91.8% | 88.7% | 88.7% |
| LiveCodeBench | 65.9% | 63.4% | 38.9% | 32.9% |

**Particularly strong on reasoning, math, and competitive programming.**

---

## Pricing (API)

| Provider | Model | Input | Output |
|----------|-------|-------|--------|
| **DeepSeek Official** | R1 | ~$0.55/M | ~$2.19/M |
| **DeepSeek Official** | R1-Distill | ~$0.14/M | ~$0.55/M |
| **Together AI** | R1 | ~$3.00/M | ~$7.00/M |
| **Ollama (local)** | R1 | Free | Free |

---

## API Example

### Via DeepSeek API

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-deepseek-key",
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{
        "role": "user",
        "content": "Solve this step by step: If a train travels 120 km in 2 hours, what's its speed?"
    }],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Local with Ollama

```bash
# Pull distilled version (recommended for most)
ollama pull deepseek-r1:32b

# Or full size (requires significant VRAM)
ollama pull deepseek-r1:671b

# Run
ollama run deepseek-r1:32b
```

### Output Format

```
<think>
The user is asking me to solve a simple physics problem.
Speed = Distance / Time
Speed = 120 km / 2 hours
Speed = 60 km/h
I should show the step-by-step reasoning clearly.
</think>

The train's speed is **60 km/h**.

Here's the step-by-step solution:
1. Given: Distance = 120 km, Time = 2 hours
2. Formula: Speed = Distance ÷ Time
3. Calculation: 120 ÷ 2 = 60
4. Answer: 60 km/h
```

---

## Use Cases

### Best For
- ✅ **Math problems** — Frontier-level math reasoning
- ✅ **Competitive programming** — Codeforces, LeetCode
- ✅ **Educational explanations** — Visible reasoning helps learning
- ✅ **Debugging complex logic** — Shows how it thinks
- ✅ **Research analysis** — Step-by-step reasoning
- ✅ **Science problems** — Physics, chemistry, logic puzzles

### Not For
- ❌ Quick, simple tasks (overkill)
- ❌ Creative writing (Claude better)
- ❌ Vision tasks (use V3 or other models)
- ❌ When latency matters (reasoning takes time)

---

## Reasoning Visibility

The `<think>` tag shows the model's internal monologue:

| Advantage | Description |
|-----------|-------------|
| **Education** | Students learn reasoning patterns |
| **Debugging** | See where it goes wrong |
| **Trust** | Understandable vs black box |
| **Validation** | Verify reasoning steps |

**Note**: OpenAI's o1 doesn't show reasoning chain.

---

## Training Approach

DeepSeek-R1 was trained with:

1. **Cold start** — Fine-tune on reasoning traces
2. **RL with GRPO** — Group Relative Policy Optimization
3. **Rejection sampling** — Filter best reasoning paths
4. **SFT + RL loop** — Iterate on quality

Key innovation: **Group Relative Policy Optimization (GRPO)** — efficient RL without value network.

---

## Distilled Models

Smaller models trained on R1's outputs:

| Model | Size | MATH-500 | AIME 2024 |
|-------|------|----------|-----------|
| Qwen-32B | 32B | 89.0% | 72.6% |
| Llama-70B | 70B | 88.5% | 70.0% |
| Qwen-14B | 14B | 83.9% | 69.7% |
| Qwen-7B | 7B | 83.5% | 55.5% |
| Qwen-1.5B | 1.5B | 75.7% | 28.9% |

**Distilled models rival original Qwen/Llama performance with reasoning added.**

---

## Limitations

1. **Speed** — Reasoning takes time (10-30s for complex problems)
2. **No vision** — Text-only (DeepSeek-V3 has vision)
3. **Chinese origin** — Some organizational trust concerns
4. **Resource intensive** — 671B full size needs serious compute
5. **Overthinking** — Can overcomplicate simple questions

---

## Comparison: DeepSeek-R1 vs Alternatives

| Model | Open | Show Reasoning | Math | Code | Best For |
|-------|------|----------------|------|------|----------|
| **DeepSeek-R1** | ✅ MIT | ✅ Yes | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Education, debugging |
| **o1** | ❌ | ❌ No | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Production, OpenAI ecosystem |
| **o3** | ❌ | ❌ No | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Best reasoning |
| **Claude 3.5** | ❌ | ❌ No | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Coding, agentic tasks |

---

## Hardware Requirements

| Model | VRAM (Q4) | VRAM (FP16) | Recommended |
|-------|-----------|-------------|-------------|
| R1 1.5B | ~1 GB | ~3 GB | Consumer GPU |
| R1 7B | ~5 GB | ~14 GB | Mid-range GPU |
| R1 14B | ~9 GB | ~28 GB | High-end GPU |
| R1 32B | ~20 GB | ~64 GB | Multi-GPU |
| R1 70B | ~40 GB | ~140 GB | Server GPU |
| R1 671B | ~400 GB | ~1.3 TB | Multi-node cluster |

---

## Resources

- **DeepSeek**: https://www.deepseek.com
- **GitHub**: https://github.com/deepseek-ai/DeepSeek-R1
- **Hugging Face**: https://huggingface.co/deepseek-ai
- **Paper**: *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*
- **API Docs**: https://platform.deepseek.com

---

## Related

- [[20-knowledge/ai/providers/ollama|Ollama]] — Run R1 locally
- [[o1|OpenAI o1]] — Closed alternative
- [[20-knowledge/ai/models/o3|o3]] — More powerful closed reasoning
- [[20-knowledge/ai/concepts/chain-of-thought|Chain-of-Thought]] — Reasoning pattern

---

*Last updated: 2026-04-05*
