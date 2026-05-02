---
title: Hugging Face
url: https://huggingface.co
founded: 2016
headquarters: New York, USA
status: active
tags: [ai, provider, open-source, models, community]
---

# Hugging Face

> The home of open-source AI — models, datasets, and tools for building with machine learning.

![Hugging Face Logo](assets/huggingface-logo.png)

## Overview

Hugging Face is the largest community and platform for open-source machine learning. It hosts over 1 million models, 200,000 datasets, and provides tools to use, train, and deploy them.

| Attribute | Value |
|-----------|-------|
| **Founded** | 2016 |
| **Headquarters** | New York, USA |
| **Type** | Open-source platform + API services |
| **Community** | 5M+ users |
| **Models** | 1,000,000+ |
| **Datasets** | 200,000+ |
| **License** | Mixed (model-dependent) |

---

## Core Products

| Product | Description | Use Case |
|---------|-------------|----------|
| **Hub** | Model/dataset hosting and sharing | Discover and download |
| **Transformers** | Library for NLP/ML models | Use models in code |
| **Inference API** | Hosted model inference | Production APIs |
| **Spaces** | ML demo hosting (Gradio/Streamlit) | Showcase models |
| **Datasets** | Dataset library and hub | Training data |
| **Accelerate** | Distributed training/finetuning | Scale training |
| **PEFT** | Parameter-efficient fine-tuning | Cheap fine-tuning |

---

## Quick Start

### 1. Install Transformers

```bash
pip install transformers datasets accelerate
pip install huggingface-hub  # For CLI and model download
```

### 2. Authenticate (for uploads/gated models)

```bash
# Get token from https://huggingface.co/settings/tokens
huggingface-cli login
# Or in Python:
# from huggingface_hub import login; login()
```

### 3. Use a Model

```python
from transformers import pipeline

# Sentiment analysis
classifier = pipeline("sentiment-analysis")
result = classifier("I love using Hugging Face!")
# [{'label': 'POSITIVE', 'score': 0.9998}]

# Text generation
generator = pipeline("text-generation", model="gpt2")
result = generator("The future of AI is", max_length=30)
# [{'generated_text': 'The future of AI is bright and...'}]
```

---

## Using Models

### Pipeline API (Easiest)

```python
from transformers import pipeline

# Available tasks:
# - "text-generation"
# - "sentiment-analysis"
# - "question-answering"
# - "summarization"
# - "translation"
# - "image-classification"
# - "automatic-speech-recognition"
# - "feature-extraction"

# Load specific model
qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

result = qa(
    question="What is Hugging Face?",
    context="Hugging Face is a company that builds tools for AI."
)
# {'score': 0.99, 'start': 0, 'end': 24, 'answer': 'a company that builds tools for AI'}
```

### Direct Model Loading

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Inference
text = "Hugging Face is amazing!"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
print(predictions)  # tensor([[0.004, 0.996]]) - 99.6% positive
```

### With torch.cuda

```python
import torch
from transformers import pipeline

device = 0 if torch.cuda.is_available() else -1
classifier = pipeline("sentiment-analysis", device=device)
```

### Batch Processing

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
texts = ["I love this!", "This is bad.", "Neutral text."]
results = classifier(texts)  # Process all at once
```

---

## Model Types on Hub

| Type | Popular Models | Use Case |
|------|----------------|----------|
| **LLMs** | Llama, Mistral, Mixtral | Text generation |
| **Embedding** | BGE, E5, GTE | RAG, search, similarity |
| **Vision** | CLIP, DINOv2, DETR | Image understanding |
| **Audio** | Whisper, Wav2Vec2 | Speech recognition |
| **Multimodal** | LLaVA, CLIP | Vision + language |
| **Diffusion** | Stable Diffusion, SDXL | Image generation |
| **Code** | CodeLlama, StarCoder | Code generation |

---

## Search & Filter Models

### Web Interface

```
https://huggingface.co/models
```

### Programmatic

```python
from huggingface_hub import HfApi

api = HfApi()

# Search models
models = list(api.list_models(
    search="whisper",
    sort="downloads",
    direction=-1,
    limit=10
))

for model in models:
    print(f"{model.modelId}: {model.downloads} downloads")

# Filter by task
models = list(api.list_models(
    filter="text-generation",
    sort="downloads",
    limit=5
))
```

### Hugging Face CLI

```bash
# Search models
huggingface-cli search bert

# Download model
huggingface-cli download gpt2

# Download specific file
huggingface-cli download gpt2 config.json

# With cache
huggingface-cli scan-cache  # See cached models
huggingface-cli delete-cache  # Clean up
```

---

## Inference API (Serverless)

### Free Tier

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {api_key}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({"inputs": "The answer to life is"})
```

### Features

| Feature | Free | Pro |
|---------|------|-----|
| Rate limit | ~30 requests/min | Higher |
| Cold start | Yes (2-10s) | Warm instances |
| GPU | Shared | Dedicated |
| Price | Free | $0.012-0.048/s |

### Using with Python Client

```python
from huggingface_hub import InferenceClient

client = InferenceClient(api_key="your_key")

# Text generation
result = client.text_generation(
    prompt="The future of AI",
    model="gpt2",
    max_new_tokens=50
)

# Chat (for chat models)
result = client.chat_completion(
    model="meta-llama/Llama-2-7b-chat-hf",
    messages=[{"role": "user", "content": "Hello!"}]
)

# Images
result = client.text_to_image(
    prompt="A beautiful landscape",
    model="stabilityai/stable-diffusion-xl-base-1.0"
)
```

---

## Fine-tuning

### Basic Fine-tuning

```python
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    TrainingArguments,
    Trainer
)
from datasets import load_dataset

# Load model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

# Load dataset
dataset = load_dataset("imdb")

# Tokenize
def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)

# Training arguments
args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
)

# Train
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=dataset["train"].shuffle(seed=42).select(range(1000)),
    eval_dataset=dataset["test"].shuffle(seed=42).select(range(500)),
)
trainer.train()

# Save and push to hub
model.push_to_hub("my-username/my-finetuned-model")
tokenizer.push_to_hub("my-username/my-finetuned-model")
```

### PEFT / LoRA (Parameter-Efficient)

```python
from peft import LoraConfig, get_peft_model, TaskType
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("gpt2")

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# trainable params: 294,912 || all params: 124,734,720 || trainable%: 0.2364

# Train only LoRA adapters...
# Then save just the adapters (small!)
model.push_to_hub("my-username/gpt2-lora")
```

---

## Datasets Library

### Load Dataset

```python
from datasets import load_dataset

# From HuggingFace Hub
dataset = load_dataset("imdb")
dataset = load_dataset("glue", "mrpc")

# Local files
dataset = load_dataset("csv", data_files="data.csv")
dataset = load_dataset("json", data_files="data.jsonl")

# Streaming (for large datasets)
dataset = load_dataset("openwebtext", streaming=True)
```

### Explore Data

```python
print(dataset)
# DatasetDict({
#     train: Dataset({
#         features: ['text', 'label'],
#         num_rows: 25000
#     })
#     test: Dataset({
#         features: ['text', 'label'],
#         num_rows: 25000
#     })
# })

print(dataset["train"][0])
# {'text': 'This movie was...', 'label': 1}

# Filter
dataset = dataset.filter(lambda x: len(x["text"]) > 100)

# Map (transform)
dataset = dataset.map(lambda x: {"text_upper": x["text"].upper()})
```

### Create & Share Dataset

```python
from datasets import Dataset

# From dict
data = {
    "text": ["Hello", "World"],
    "label": [0, 1]
}
dataset = Dataset.from_dict(data)

# From pandas
import pandas as pd
df = pd.DataFrame(data)
dataset = Dataset.from_pandas(df)

# Push to hub
dataset.push_to_hub("my-username/my-dataset")
```

---

## Spaces

### Create a Demo

```python
# app.py
import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def predict(text):
    result = classifier(text)[0]
    return f"{result['label']} ({result['score']:.2f})"

gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Text"),
    outputs=gr.Textbox(label="Sentiment"),
    title="Sentiment Analysis"
).launch()
```

Deploy by creating a Space at huggingface.co/spaces and pushing to it.

---

## Deployment Options

| Method | Best For | Complexity |
|--------|----------|------------|
| **Inference API** | Testing, prototyping | Low |
| **Inference Endpoints** | Production, dedicated | Medium |
| **Spaces** | Demos, prototypes | Low |
| **Self-hosted** | Full control, compliance | High |

### Inference Endpoints (Production)

```bash
# Deploy via CLI
huggingface-cli endpoint create \
  --model "gpt2" \
  --instance-type "gpu-t4-small" \
  --vendor "aws" \
  --region "us-east-1"

# Or API
```python
from huggingface_hub import create_inference_endpoint

endpoint = create_inference_endpoint(
    "my-endpoint",
    repository="gpt2",
    framework="pytorch",
    accelerator="gpu",
    instance_type="g4dn.xlarge",
    vendor="aws",
    region="us-east-1"
)
```

---

## Pricing

### Compute Costs Overview

| Service | Free Tier | Paid Options | Cost |
|---------|-----------|--------------|------|
| **Hub** (Model Storage) | Unlimited public repos | Private repos: $9/mo | $9/mo/seat |
| **Inference API** | 30k input tokens/day | Pro: More tokens + priority | $9/mo |
| **Spaces** | 2GB RAM, CPU, sleeps | GPU/CPU upgrades | $0.05-0.60/hour |
| **Inference Endpoints** | — | Dedicated GPU instances | $0.06-4.50/hour |
| **Fine-tuning** | — | Compute time | $0.10-4.50/hour |
| **Datasets** | Unlimited public | Private datasets | Included with Pro |

---

### Detailed Compute Pricing

#### Spaces (Hosted Demos)

| Hardware | VRAM | Price | Best For |
|----------|------|-------|----------|
| **CPU Basic** | — | Free | Prototypes, simple UIs |
| **CPU Upgrade** | — | $0.05/hr | Reliable CPU apps |
| **T4 (GPU Small)** | 16GB | $0.40/hr | Small models, inference |
| **L4 (GPU Medium)** | 24GB | $0.60/hr | Medium models |
| **A10G (GPU Large)** | 24GB | $0.75/hr | Training, larger models |
| **A100 (GPU XL)** | 40/80GB | $2.00-4.00/hr | Large models, training |

#### Inference Endpoints (Production API)

| Instance Type | GPU | Price/Hour | Best For |
|---------------|-----|------------|----------|
| **CPU** | — | $0.06 | Simple tasks, embeddings |
| **GPU Small** | NVIDIA T4 | $0.50 | 7B models, inference |
| **GPU Medium** | NVIDIA L4 | $0.75 | 13B-30B models |
| **GPU Large** | NVIDIA A10G | $0.90 | 70B models, batch inference |
| **GPU XL** | NVIDIA A100 | $3.00-4.50 | Large models, training |

**Autoscaling available** — pay only for active compute time.

---

### Local/On-Premise Costs (Self-Hosting)

Running Hugging Face models locally means **no API costs**, but you pay for hardware:

| Setup | Hardware Cost | VRAM | Can Run |
|-------|---------------|------|---------|
| **Consumer GPU** | $500-1000 | 8-12GB | 7B-13B models |
| **Mid-range** | $1500-2500 | 24GB | 30B-70B models (quantized) |
| **High-end** | $4000-8000 | 48GB | 70B models, fine-tuning |
| **Server GPU** | $10,000+ | 80GB | 405B models (quantized), training |

**Operational costs:**
- Electricity: ~$50-200/mo for 24/7 operation
- Cloud GPU rental: $0.50-4.50/hr if not owning hardware

---

### Cost Comparison: API vs Local

#### Scenario: 100K requests/day, 1000 tokens each

| Option | Cost | Pros | Cons |
|--------|------|------|------|
| **Inference API Free** | $0 | $0 | Limited to 30k tokens/day |
| **Inference API Pro** | $9/mo | More quota | Still rate limited |
| **Inference Endpoints** | ~$300-600/mo | Reliable, auto-scale | Requires setup |
| **Local GPU (T4)** | $300 (one-time) | Unlimited, private | Maintenance |
| **Cloud GPU (rent)** | ~$300-500/mo | Flexible | Recurring cost |

#### Scenario: Fine-tuning a 7B model

| Option | Cost | Time |
|--------|------|------|
| **Free T4 (Spaces)** | $0 | 6-12 hours |
| **Paid A10G** | ~$5-10 | 2-4 hours |
| **Local RTX 4090** | Hardware cost | 2-4 hours |

---

### Hidden Costs

**Free tier limitations:**
- Inference API: Cold starts (2-10s)
- Spaces: Sleep after inactivity (cold start on wake)
- Bandwidth: Charges for large outgoing transfers

**Paid considerations:**
- Storage: Models cached count toward storage limits
- Egress: Data transfer out can add up
- Idle time: Endpoints still bill when idle unless auto-scaled to zero

---

## Code Examples

### RAG with Embeddings

```python
from transformers import AutoTokenizer, AutoModel
import torch

# Load embedding model
tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-small-en")
model = AutoModel.from_pretrained("BAAI/bge-small-en")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Mean pooling
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings

# Use for similarity search
doc_embeddings = [get_embedding(doc) for doc in documents]
query_embedding = get_embedding("query text")
# Compute similarities...
```

### Image Classification

```python
from transformers import pipeline

classifier = pipeline("image-classification")
result = classifier("image.jpg")
# [{'label': 'tiger', 'score': 0.98}, ...]
```

### Speech Recognition

```python
from transformers import pipeline

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base")
result = transcriber("audio.mp3")
# {'text': 'transcribed text'}
```

---

## Comparison with Alternatives

| vs | Hugging Face | Advantage |
|----|--------------|-----------|
| **OpenAI** | Open models | No vendor lock-in |
| **GitHub** | ML-specific | Model versioning, inference |
| **AWS SageMaker** | Community focus | Free tier, open source |

---

## Resources

- **Website**: https://huggingface.co
- **Docs**: https://huggingface.co/docs
- **Models**: https://huggingface.co/models
- **Datasets**: https://huggingface.co/datasets
- **Spaces**: https://huggingface.co/spaces
- **Transformers Docs**: https://huggingface.co/docs/transformers
- **Course**: https://huggingface.co/course

---

## Related

- [[20-knowledge/ai/providers/openai|OpenAI]] — Closed alternative
- [[20-knowledge/ai/models/llama-3-1|Llama 3.1]] — Popular HF model
- [[20-knowledge/ai/tools/llama-cpp|llama.cpp]] — Run HF models locally

---

*Last updated: 2026-04-05*
