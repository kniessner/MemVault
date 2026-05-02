---
title: Llama 3.1
provider: Meta
release_date: 2024-07-23
context: 128000
status: active
tags: [model, meta, open-weight, local]
---

# Llama 3.1

> Meta's most capable open models — 8B, 70B, and 405B parameters with 128K context, competitive with leading closed models.

## Overview

Llama 3.1 is Meta's open-weight model family, offering state-of-the-art performance across multiple sizes. The 405B model is the largest open-weight model released, approaching GPT-4 level performance.

| Attribute | Value |
|-----------|-------|
| **Provider** | Meta AI |
| **Release** | July 2024 |
| **License** | Llama 3.1 Community License |
| **Context** | 128K tokens (all sizes) |
| **Knowledge Cutoff** | December 2023 |

---

## Model Sizes

| Model | Parameters | VRAM (Q4) | VRAM (FP16) | Best For |
|-------|------------|-----------|-------------|----------|
| **Llama 3.1 8B** | 8 billion | ~6 GB | ~16 GB | Edge devices, fast inference |
| **Llama 3.1 70B** | 70 billion | ~40 GB | ~140 GB | High quality, single node |
| **Llama 3.1 405B** | 405 billion | ~230 GB | ~810 GB | Frontier quality, multi-GPU |

---

## Specifications

| Capability | 8B | 70B | 405B |
|------------|-----|-----|------|
| **Text** | ✅ | ✅ | ✅ |
| **Tools** | ✅ | ✅ | ✅ |
| **Multilingual** | ✅ (8 langs) | ✅ (8 langs) | ✅ (8 langs) |
| **Long Context** | ✅ 128K | ✅ 128K | ✅ 128K |

---

## Performance Benchmarks

| Benchmark | 8B | 70B | 405B | GPT-4o |
|-----------|-----|-----|------|--------|
| MMLU | 73.0% | 86.0% | 88.6% | 88.7% |
| HumanEval | 72.6% | 84.1% | 89.0% | 90.2% |
| MATH | 51.9% | 68.0% | 78.5% | 76.6% |
| GPQA | 33.3% | 48.0% | 53.1% | 53.6% |

**405B approaches GPT-4o on many benchmarks.**

---

## Pricing (Inference)

Llama 3.1 is **free to use** (self-host) or via API providers:

| Provider | Model | Input | Output |
|----------|-------|-------|--------|
| **Groq** | 8B | $0.05/M | $0.08/M |
| **Groq** | 70B | $0.59/M | $0.79/M |
| **Together AI** | 405B | ~$3.50/M | ~$10.00/M |
| **Meta** | All | Free (self-host) | Free (self-host) |

---

## API Example

### Local with Ollama

```bash
# Pull and run
ollama pull llama3.1
ollama run llama3.1

# API mode
ollama serve
curl http://localhost:11434/api/chat -d '{
    "model": "llama3.1",
    "messages": [{"role": "user", "content": "Hello!"}]
}'
```

### Via Groq (fast inference)

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-groq-key",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Explain neural networks"}]
)
# 840+ tokens/second
```

### Together AI (405B)

```python
import openai

client = openai.OpenAI(
    api_key="your-together-key",
    base_url="https://api.together.xyz/v1"
)

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    messages=[{"role": "user", "content": "Complex reasoning task..."}]
)
```

---

## Use Cases

### Best For
- ✅ **Privacy-sensitive apps** — Self-host, no data leaves
- ✅ **Cost optimization** — Free if self-hosted
- ✅ **Customization** — Fine-tune on your data
- ✅ **Edge deployment** — 8B runs on consumer hardware
- ✅ **Research** — Full weights available
- ✅ **Avoiding vendor lock-in** — Open weights, multiple hosts

### By Size

| Size | Use Case |
|------|----------|
| **8B** | Mobile apps, edge, high-volume APIs |
| **70B** | Production apps, single GPU, balanced quality |
| **405B** | Frontier tasks, research, maximum quality |

---

## Tool Use (Function Calling)

Llama 3.1 supports native tool use:

```python
response = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[{"role": "user", "content": "What's the weather?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {"location": {"type": "string"}}
            }
        }
    }],
    tool_choice="auto"
)
```

---

## System Prompt

Llama 3.1 uses special tokens for system prompts:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a helpful assistant.<|eot_id|>
<|start_header_id|>user<|end_header_id|>

Hello!<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>

Hi there!<|eot_id|>
```

Most APIs handle this automatically.

---

## Limitations

1. **No vision** — Text only (unlike GPT-4o/Gemini)
2. **No internet** — Knowledge cutoff December 2023
3. **Hardware requirements** — 405B needs serious compute
4. **License restrictions** — Commercial use 700M+ users requires license
5. **Coding quality** — 405B good but Claude 3.5 better for coding

---

## Fine-tuning

```python
# Using PyTorch with PEFT/LoRA
from transformers import AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, get_peft_model

model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")

lora_config = LoraConfig(r=16, lora_alpha=32, target_modules=["q_proj", "v_proj"])
model = get_peft_model(model, lora_config)

# Train on your dataset
trainer = Trainer(
    model=model,
    args=TrainingArguments(output_dir="./results"),
    train_dataset=dataset
)
trainer.train()
```

---

## Comparison: Llama 3.1 vs Alternatives

| Model | Size | Open | Coding | Best For |
|-------|------|------|--------|----------|
| **Llama 3.1 8B** | Small | ✅ | ⭐⭐⭐ | Edge, high-volume |
| **Llama 3.1 70B** | Large | ✅ | ⭐⭐⭐⭐ | Self-hosted production |
| **Llama 3.1 405B** | Frontier | ✅ | ⭐⭐⭐⭐⭐ | Maximum quality open |
| **GPT-4o** | Unknown | ❌ | ⭐⭐⭐⭐⭐ | Ecosystem, multimodal |
| **Claude 3.5** | Unknown | ❌ | ⭐⭐⭐⭐⭐ | Coding, reliability |
| **Mixtral 8x22B** | 141B | ✅ | ⭐⭐⭐⭐ | MoE efficiency |

---

## Resources

- **Meta AI**: https://ai.meta.com/llama
- **Download**: https://llama.meta.com/llama-downloads
- **Hugging Face**: https://huggingface.co/meta-llama
- **License**: https://llama.meta.com/llama3_1/license

---

## Related

- [[20-knowledge/ai/providers/ollama|Ollama]] — Run Llama locally
- [[20-knowledge/ai/providers/groq|Groq]] — Fast Llama inference
- [[mixtral-8x22b|Mixtral 8x22B]] — Open alternative
- [[20-knowledge/ai/tools/llama-cpp|llama.cpp]] — Local inference engine

---

*Last updated: 2026-04-05*
