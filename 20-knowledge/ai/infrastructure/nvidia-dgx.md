---
title: "NVIDIA DGX Platform"
description: NVIDIA's unified platform for enterprise AI development at scale
url: https://www.nvidia.com/en-us/data-center/dgx-systems/
category: AI Infrastructure
subcategory: Enterprise Hardware
type: product-platform
status: active
founded: 2016 (DGX-1)
last_updated: 2026-04-24
tags:
  - nvidia
  - dgx
  - gpu-cluster
  - enterprise-ai
  - supercomputer
  - infrastructure
  - blackwell
  - h100
  - h200
  -推理
products:
  - DGX B200
  - DGX H100
  - DGX H200
  - DGX GB200 NVL72
  - DGX SuperPOD
  - DGX BasePOD
  - DGX Cloud
pricing:
  - "Contact sales for pricing"
  - "DGX Cloud: Usage-based"
  - "Financing options available"
competitors:
  - Lambda Labs
  - CoreWeave
  - Crusoe Cloud
  - Together AI
  - Lambda
  - RunPod
  - Vast.ai
---

# NVIDIA DGX Platform

> "The world's leading solution for enterprise AI development at scale"

## Overview

NVIDIA DGX Systems provide the world's leading solutions for enterprise AI development at scale. The platform includes both on-premises hardware and cloud-based solutions, offering a full-stack AI infrastructure for organizations building and deploying large-scale AI models.

## Product Lineup

### Current Generation (Blackwell/Rubin)

#### Vera Rubin NVL72
- **Architecture**: Blackwell/Rubin
- **Form Factor**: Rack-scale system
- **Target Use**: Agentic AI, reasoning models
- **Key Feature**: Agent-based AI supercomputer at rack scale
- **Inference**: Fast inference with comprehensive intelligence at scale

#### DGX GB200 NVL72
- **Architecture**: Blackwell
- **Form Factor**: 72-GPU rack-scale system
- **Target Use**: Scalable LLM inference and advanced enterprise AI
- **Platform**: Full-stack system for enterprise AI

#### DGX GB300 NVL72
- **Architecture**: Next-gen after GB200
- **Form Factor**: Rack-scale
- **Target Use**: Era of AI reasoning
- **Status**: Announced/Upcoming

### Previous Generation (Hopper)

#### DGX H100
- **Architecture**: Hopper
- **GPU**: 8x H100 Tensor Core GPUs
- **AI Performance**: Up to 32 petaflops FP8
- **GPU Memory**: 640 GB total HBM3
- **NVSwitches**: 4x 3rd gen NVSwitch
- **CPU**: 2x Intel Xeon Platinum
- **Networking**: 10x NVIDIA ConnectX-7

#### DGX H200
- **Architecture**: Hopper
- **Upgrade**: Enhanced H100 with HBM3e memory
- **GPU Memory**: Increased capacity vs H100
- **Target Use**: Larger model inference

### Entry/Mid Range

#### DGX B200
- **Architecture**: Blackwell
- **Position**: Mainstream enterprise AI
- **Use Cases**: Training and inference for enterprise workloads

### Modular and Cloud

#### DGX SuperPOD
- **Scale**: Multi-rack supercomputer
- **Architecture**: Reference design for large-scale AI
- **Full-Stack Blueprint**: For gigascale AI infrastructure
- **Components**: Compute, networking, storage, software

#### DGX BasePOD
- **Type**: Reference architecture
- **Purpose**: Building and scaling AI infrastructure
- **Flexible**: Customer-configurable

#### DGX Cloud
- **Model**: AI factory in the cloud
- **Access**: Immediate, no hardware procurement
- **Software**: Full NVIDIA AI stack
- **Partners**: AWS, Azure, Google Cloud, OCI

## Key Specifications Comparison

| System | Architecture | GPUs | GPU Memory | Use Case |
|--------|-------------|------|------------|----------|
| Vera Rubin NVL72 | Rubin | 72 | Massive | Agentic AI, Reasoning |
| GB300 NVL72 | Next-gen | 72 | Large | AI Reasoning |
| GB200 NVL72 | Blackwell | 72 | 1.4TB HBM3e | LLM Inference |
| DGX H100 | Hopper | 8 | 640GB HBM3 | Training, Inference |
| DGX H200 | Hopper | 8 | Increased | Large Model Inference |
| DGX B200 | Blackwell | 8 | HBM3e | Enterprise AI |
| SuperPOD | Varies | 32+ | Scalable | Large-scale training |

## Software Stack

### NVIDIA AI Enterprise
- **NVIDIA NeMo**: End-to-end model training and customization
- **NVIDIA Triton**: Inference serving
- **NVIDIA Base Command**: AI job scheduling and orchestration
- **NVIDIA Fleet Command**: Edge deployment management

### System Software
- **NVIDIA BaseOS**: Optimized Linux distribution
- **CUDA**: GPU computing platform
- **NCCL**: Multi-GPU communication
- **NVLink/NVSwitch**: High-speed interconnect

## Networking

### InfiniBand
- Up to 400 Gb/s per port
- RDMA support
- NVIDIA ConnectX adapters

### NVLink/NVSwitch
- GPU-to-GPU interconnect
- Up to 900 GB/s bandwidth
- Enables large effective memory pools

## Use Cases

### Large Language Models
- Training from scratch
- Fine-tuning
- Inference at scale

### Generative AI
- Text-to-image (Stable Diffusion)
- Text-to-video
- Code generation

### Scientific Computing
- Climate modeling
- Drug discovery
- Physics simulations

### Enterprise AI
- Recommendation systems
- Computer vision
- Natural language processing

## Deployment Options

### On-Premises
- Purchase hardware
- Deploy in data center
- Full control and customization

### DGX Cloud
- Instant access
- Pay-as-you-go
- No hardware procurement

### Colocation
- Third-party data center
- NVIDIA certified partners

## Key Features

### Full-Stack Integration
- Hardware + Software + Networking
- Optimized end-to-end
- Single vendor support

### Scalability
- Start with single DGX system
- Scale to SuperPOD
- Connect to DGX Cloud

### Enterprise Support
- NVIDIA Enterprise Services
- Proactive monitoring
- Optimized software updates

## Alternatives and Competitors

### Cloud GPU Providers
- **Lambda Labs**: GPU cloud, on-demand instances
- **CoreWeave**: Kubernetes-native GPU cloud
- **Crusoe Cloud**: Clean energy GPU cloud

### Hardware Alternatives
- **AMD MI300X**: Competitive GPU offering
- **Google TPUs**: Google Cloud only
- **Amazon Trainium/Inferentia**: AWS only

### Software-Only
- **Kubernetes + GPU Operators**: Build your own
- **Ray**: Distributed AI framework

## Market Position

### Strengths
- Dominant GPU ecosystem (CUDA)
- Full-stack optimization
- Proven at scale (OpenAI, Anthropic, etc.)
- Enterprise support and services

### Considerations
- Premium pricing
- Vendor lock-in (CUDA ecosystem)
- High power requirements
- Long procurement cycles

## Pricing

- **DGX H100**: ~$300,000+ per system
- **DGX H200**: Premium over H100
- **DGX SuperPOD**: Multi-million dollar deployments
- **DGX Cloud**: Usage-based, competitive with cloud providers

*Note: Pricing varies by configuration and requires quotes from NVIDIA sales*

## Recent Developments (2024-2025)

### Blackwell Generation
- B200, GB200 announced
- Significant performance improvements
- Enhanced inference capabilities

### DGX Cloud Expansion
- More cloud provider partnerships
- Increased availability regions

### Software Enhancements
- NVIDIA AI Enterprise updates
- Inference optimization tools
- Multi-modal model support

## Resources

- [Official DGX Page](https://www.nvidia.com/en-us/data-center/dgx-systems/)
- [DGX Solutions](https://www.nvidia.com/en-us/data-center/solutions/)
- [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/)
- [DGX Cloud](https://www.nvidia.com/en-us/data-center/dgx-cloud/)

---

*Source: [NVIDIA DGX Systems](https://www.nvidia.com/en-us/data-center/dgx-systems/)*
*Last updated: April 2026*
