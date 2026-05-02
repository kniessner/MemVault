---
title: AI Image Generation Options
created: 2026-04-05
tags: [ai, concept, image-generation, multimodal]
---

# AI Image Generation Options

> Complete guide to generating images with AI — APIs, local models, and web services.

---

## Option 1: API-Based Services

### 1.1 OpenAI DALL-E 3

**Best for:** High quality, reliable, text-accurate images

```python
from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="A serene Japanese garden with cherry blossoms, watercolor style",
    size="1024x1024",
    quality="standard",  # or "hd"
    n=1
)

image_url = response.data[0].url
```

| Attribute | Value |
|-----------|-------|
| **Quality** | ⭐⭐⭐⭐⭐ |
| **Text Accuracy** | ⭐⭐⭐⭐⭐ (best for text in images) |
| **Speed** | ⭐⭐⭐⭐ |
| **Price** | $0.04-0.08 per image |
| **API** | Simple REST |
| **Rate Limits** | 5-50 images/min depending on tier |

**Pros:**
- Excellent at following complex prompts
- Best for text rendering in images
- Consistent quality
- Simple API

**Cons:**
- More expensive than alternatives
- Content policy restrictions
- No fine-tuning

---

### 1.2 Replicate (Multiple Models)

**Best for:** Flexibility, latest open-source models

```python
import replicate

# Flux.1 (open weights, high quality)
output = replicate.run(
    "black-forest-labs/flux-1.1-pro",
    input={
        "prompt": "A futuristic city at sunset, cyberpunk style",
        "width": 1024,
        "height": 1024
    }
)

# Stable Diffusion XL
output = replicate.run(
    "stability-ai/stable-diffusion-xl-base-1.0",
    input={"prompt": "A cat playing piano, oil painting"}
)
```

| Model | Best For | Price |
|-------|----------|-------|
| Flux 1.1 Pro | Highest quality | ~$0.03-0.055 |
| SDXL | Balanced | ~$0.008 |
| SD 1.5 | Fast, cheap | ~$0.002 |

**Pros:**
- Access to latest open-source models
- Pay-per-use
- Many models available (4000+)

**Cons:**
- Cold start latency
- Variable pricing
- Requires separate account

---

### 1.3 Stability AI API

**Best for:** Production apps, mass generation

```python
import requests

response = requests.post(
    "https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={"authorization": f"Bearer {api_key}"},
    files={"none": ''},
    data={
        "prompt": "A magical forest with glowing mushrooms",
        "output_format": "png"
    }
)
```

| Plan | Price | Best For |
|------|-------|----------|
| Free | 25 credits/day | Testing |
| Basic | $9/mo | Personal |
| Standard | $27/mo | Small business |
| Premium | $147/mo | Heavy usage |

**Pros:**
- SD3 (best open model quality)
- Credits system
- Commercial license

**Cons:**
- Credit system complexity
- Pricing tiers

---

### 1.4 HuggingFace Inference API

**Best for:** Free tier, open models

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {api_key}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

image_bytes = query({
    "inputs": "Astronaut riding a horse",
})
```

**Pros:**
- Generous free tier
- Many open models
- Easy to try

**Cons:**
- Rate limits on free tier
- Cold start times
- Model availability varies

---

## Option 2: Local/On-Premise

### 2.1 Stable Diffusion (SD WebUI / AUTOMATIC1111)

**Best for:** Privacy, unlimited generation, full control

```bash
# Install
pip install stable-diffusion-webui

# Or use pre-built
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui
./webui.sh

# Access at http://localhost:7860
```

**Requirements:**
| Hardware | VRAM | Speed |
|----------|------|-------|
| NVIDIA GPU | 8GB+ for SDXL | 512-1024px in seconds |
| Apple Silicon | 16GB+ unified | Slower but works |
| CPU | N/A | Minutes per image |

**Features:**
- LoRA fine-tuning support
- ControlNet for precise control
- Inpainting, outpainting
- Batch processing
- Extensions ecosystem

**Pros:**
- One-time cost (hardware)
- Complete privacy
- No rate limits
- Full customization

**Cons:**
- Requires GPU
- Setup complexity
- Maintenance burden

---

### 2.2 ComfyUI

**Best for:** Power users, complex workflows, node-based editing

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
pip install -r requirements.txt
python main.py
```

**Workflow example:**
```
Load Checkpoint → CLIP Text Encode (Prompt) → KSampler → VAE Decode → Save Image
                     ↓
              Empty Latent Image
```

**Pros:**
- Visual workflow builder
- Maximum flexibility
- Share workflows as JSON
- Active community

**Cons:**
- Steep learning curve
- Complex UI
- Overkill for simple tasks

---

### 2.3 Diffusers (Python Library)

**Best for:** Python developers, custom pipelines

```python
from diffusers import StableDiffusionXLPipeline
import torch

pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16
)
pipe.to("cuda")

image = pipe(
    "A beautiful landscape painting",
    num_inference_steps=30
).images[0]
```

**Pros:**
- Programmatic control
- Easy fine-tuning
- Batch processing
- Great for apps

**Cons:**
- Requires GPU
- Python knowledge needed

---

## Option 3: Web-Based Services

### 3.1 Midjourney

**Best for:** Artistic, atmospheric images

| Plan | Price | Fast Hours |
|------|-------|------------|
| Basic | $10/mo | 3.3 hrs |
| Standard | $30/mo | 15 hrs |
| Pro | $60/mo | 30 hrs |

**Pros:**
- Unique aesthetic quality
- Great community
- Upscaling excellent
- Style consistency

**Cons:**
- Discord-only interface
- Subscription required
- Public generations by default
- Limited control

---

### 3.2 Leonardo.AI

**Best for:** Game assets, stylized art

**Features:**
- 150-300 tokens/day free
- Fine-tuned models
- Real-time canvas
- Motion generation

| Plan | Price | Tokens |
|------|-------|--------|
| Free | $0 | 150/day |
| Apprentice | $12/mo | 8500/mo |
| Artisan | $30/mo | 25000/mo |

---

### 3.3 Ideogram

**Best for:** Text in images (logo, typography)

- Free tier: 25 prompts/day
- Plus: $8/mo for 400 prompts
- Best-in-class text rendering

---

### 3.4 Adobe Firefly

**Best for:** Commercial-safe content, Adobe integration

- Commercially safe training data
- Integrated with Photoshop
- Generative fill feature

---

## Option 4: Free/No-API Alternatives

### 4.1 Pollinations AI (When Available)

```
https://image.pollinations.ai/prompt/{your+prompt}?width=1024&height=1024
```

- Completely free
- No API key
- Often overloaded

### 4.2 Bing Image Creator (DALL-E 3)

- Free with Microsoft account
- Powered by DALL-E 3
- Limited boosts (credits)
- Web interface only

### 4.3 Craiyon (Formerly DALL-E Mini)

- Completely free
- Lower quality
- Good for experimentation

---

## Comparison Matrix

| Service | Quality | Cost | Speed | Privacy | API | Best For |
|---------|---------|------|-------|---------|-----|----------|
| **DALL-E 3** | ⭐⭐⭐⭐⭐ | $$ | Fast | ❌ | ✅ | Text accuracy |
| **Midjourney** | ⭐⭐⭐⭐⭐ | $$ | Medium | ❌ | ❌ | Art/Atmosphere |
| **Flux** | ⭐⭐⭐⭐⭐ | $ | Fast | ❌ | ✅ | Open-source quality |
| **SDXL** | ⭐⭐⭐⭐⭐ | $ | Fast | Local only | ✅ | Control/Custom |
| **Leonardo** | ⭐⭐⭐⭐ | $ | Fast | ❌ | ✅ | Game assets |
| **Ideogram** | ⭐⭐⭐⭐ | Free/$ | Medium | ❌ | ✅ | Text in images |
| **Local SD** | ⭐⭐⭐⭐⭐ | Hardware | Varies | ✅ | Custom | Privacy/Scale |

---

## Decision Guide

**Choose DALL-E 3 if:**
- You need text in images
- Simple API integration
- Budget allows

**Choose Midjourney if:**
- Artistic quality matters most
- You're doing concept art
- Discord workflow works for you

**Choose Local SD if:**
- Privacy is critical
- High volume generation
- Technical expertise available

**Choose Replicate if:**
- Flexibility needed
- Pay-per-use preferred
- Want latest models

**Choose Leonardo if:**
- Game development
- Need fine-tuning
- Want free tier

---

## Environment Setup for Hermes

### Option A: Replicate (Recommended)

```bash
# Get key from https://replicate.com/account/api-tokens
export REPLICATE_API_TOKEN="r8_xxxxxxxx"
```

### Option B: OpenAI

```bash
# Get key from https://platform.openai.com/api-keys
export OPENAI_API_KEY="sk-xxxxxxxx"
```

### Option C: Stability AI

```bash
# Get key from https://platform.stability.ai/
export STABILITY_API_KEY="sk-xxxxxxxx"
```

### Option D: Local (GPU Required)

```bash
# Install dependencies
pip install diffusers transformers accelerate torch

# Run with local GPU
```

---

## Resources

- **DALL-E 3**: https://platform.openai.com/docs/guides/images
- **Replicate**: https://replicate.com/docs
- **Stability AI**: https://platform.stability.ai/
- **Midjourney**: https://docs.midjourney.com/
- **ComfyUI**: https://github.com/comfyanonymous/ComfyUI
- **AUTOMATIC1111**: https://github.com/AUTOMATIC1111/stable-diffusion-webui

---

## Related

- [[20-knowledge/ai/models/stable-diffusion|Stable Diffusion]] — Local generation skill
- [[20-knowledge/ai/providers/openai|OpenAI]] — DALL-E provider

---

*Last updated: 2026-04-05*
