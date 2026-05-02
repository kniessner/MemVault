# OpenCode + Ollama Integration

## Setup

- **opencode version**: 1.4.3
- **config file**: `~/.config/opencode/opencode.json`
- **config dir**: `~/.config/opencode/`
- **binary**: `/opt/homebrew/bin/opencode`

## Config Format for Ollama

Ollama is added as an OpenAI-compatible custom provider. Requires installing `@ai-sdk/openai-compatible` in `~/.config/opencode/`:

```bash
cd ~/.config/opencode && npm install @ai-sdk/openai-compatible
```

### opencode.json schema

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "model-id": {
          "name": "Display Name"
        }
      }
    }
  }
}
```

## Key Notes

- No API key needed for local Ollama
- For Ollama Cloud: export `OLLAMA_API_KEY` env var and use `https://ollama.com/v1` as baseURL
- Embedding models (e.g., `mxbai-embed-large`) should NOT be added to the config
- Default context is 4096 tokens; increase `num_ctx` in Ollama modelfile if tool calls fail
- To select a model: `opencode -m ollama/llama3.2:3b`
- To list available models: `opencode models ollama`

## Installed Local Models (as of 2026-04-10)

| Model | Size | Notes |
|-------|------|-------|
| gemma4:e4b | 9.6 GB | Large model |
| llama3.2:3b | 2.0 GB | Fast, small |
| llama3.1:latest | 4.9 GB | General purpose |
| minimax-m2:cloud | - | Cloud connector |
| mxbai-embed-large | 669 MB | Embedding only, not in config |

## Sources

- https://opencode.ai/docs/providers/
- https://docs.ollama.com/integrations/opencode
