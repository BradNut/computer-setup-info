# Local AI Model Setup for Zed

This guide documents how to run an Apache-2.0-licensed coding model locally with `llama.cpp` and connect it to Zed's AI agent panel on a Linux laptop without a dedicated GPU.

## Hardware context

These steps were tuned for an Intel Lunar Lake laptop (Core Ultra 9 288V, integrated Arc graphics, 30 GB shared system RAM). Without dedicated VRAM, the model budget is roughly 5–9 GB for weights. A 7B parameter model quantized to Q4_K_M is the practical ceiling for responsive agent editing.

## Install the llama.cpp launcher

The recommended distribution is the official unified `llama` launcher, a single self-updating binary:

```bash
# Official installer (places ~/.local/bin/llama)
curl -fsSL https://ggml.ai/install.sh | sh

# Or update an existing install
llama update
```

This launcher is preferred over the Homebrew formula because it is newer, self-updating, and bundles the same features without extra linked dependencies.

## Download a model

Choose an Apache-2.0 model. Qwen2.5-Coder-7B-Instruct is a good fit for coding tasks; Qwen2.5-7B-Instruct tends to follow tool-calling instructions more reliably when using Zed's agent panel.

```bash
# Coding/completions focused
llama download -hf Qwen/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M

# More reliable tool calling for agent editing
llama download -hf Qwen/Qwen2.5-7B-Instruct-GGUF:Q4_K_M
```

Q4_K_M is around 4.7 GB and fits comfortably on shared-memory hardware.

## Run the server

Use `llama serve` with the flags that enable reliable tool calls and a context window larger than 16K:

```bash
llama serve \
  -hf Qwen/Qwen2.5-7B-Instruct-GGUF:Q4_K_M \
  --jinja \
  --ctx-size 32768 \
  --flash-attn on \
  --temp 0 \
  --host 127.0.0.1 --port 8080 \
  --alias qwen2.5-instruct
```

| Flag | Why it matters |
|------|----------------|
| `--jinja` | Uses the model's embedded chat template. Tool calling only works when the template is applied. This build enables it by default, but being explicit protects against config drift. |
| `--ctx-size 32768` | Gives Zed a 32K token context window, clearing the 16K minimum requirement. |
| `--flash-attn on` | Reduces KV-cache memory usage, important on shared RAM. |
| `--temp 0` | Greedy decoding. The 7B model can emit malformed tool tags when sampling freely; temperature zero makes it follow the template much more reliably. |
| `--alias qwen2.5-instruct` | The name Zed will send in its requests. |

## Configure Zed

Zed is installed from Flathub, so its config lives at:

```text
~/.var/app/dev.zed.Zed/config/zed/settings.json
```

Add an `openai_compatible` provider and point the agent at it:

```json
{
  "language_models": {
    "openai_compatible": {
      "llamacpp": {
        "api_url": "http://127.0.0.1:8080/v1",
        "available_models": [
          {
            "name": "qwen2.5-coder",
            "display_name": "Qwen2.5 Coder 7B (local)",
            "max_tokens": 32768,
            "capabilities": {
              "tools": true,
              "images": false,
              "parallel_tool_calls": false,
              "prompt_cache_key": false
            }
          },
          {
            "name": "qwen2.5-instruct",
            "display_name": "Qwen2.5 Instruct 7B (local)",
            "max_tokens": 32768,
            "capabilities": {
              "tools": true,
              "images": false,
              "parallel_tool_calls": false,
              "prompt_cache_key": false
            }
          }
        ]
      }
    }
  },
  "agent": {
    "default_model": {
      "provider": "llamacpp",
      "model": "qwen2.5-instruct"
    },
    "dock": "right",
    "default_profile": "write"
  }
}
```

Key points:

- `llamacpp` is an arbitrary provider label. It must match exactly between `openai_compatible.<label>` and `agent.default_model.provider`.
- `agent.default_model.model` must match the `name` field of one of the `available_models` entries.
- `capabilities.tools: true` is what lets Zed send editing tools to the model. Without it, the agent will just describe changes in chat.

When Zed prompts for an OpenAI API key, enter any non-empty string (for example `local`). `llama serve` ignores the key.

## Switch models in Zed

1. Close any open Zed Settings tab so the UI does not overwrite `settings.json`.
2. Reload Zed: `Ctrl+Shift+P` → `zed: reload`.
3. Start a new thread in the agent panel.
4. Use the model picker in the bottom-right of the agent panel to select the desired local model.

Old threads remember the model they were started with, so switching models always requires a new thread.

## Test that tool calls work

With the server running, run this in a terminal:

```bash
curl -s http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "qwen2.5-instruct",
    "temperature": 0,
    "messages": [{"role":"user","content":"List files in /tmp using the tool."}],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "list_dir",
          "description": "List a directory",
          "parameters": {
            "type": "object",
            "properties": { "path": { "type": "string" } },
            "required": ["path"]
          }
        }
      }
    ]
  }' | python3 -c 'import sys,json; print(json.dumps(json.load(sys.stdin)["choices"][0]["message"], indent=2))'
```

A working setup returns a structured `tool_calls` array. If the response only contains raw `<tools>` text in `content`, the model failed to follow the tool-calling template and Zed will not be able to edit files.

## Troubleshooting

### Agent narrates changes instead of editing files

- Make sure the agent panel's model picker shows a model entry that has `capabilities.tools: true`.
- Make sure `llama serve` is running with `--temp 0`.
- If using Qwen2.5-Coder, try Qwen2.5-Instruct instead — it follows tool-calling instructions more reliably at 7B.
- If the model still narrates, the 7B weight class may be too small for reliable multi-step agent editing. The 14B variant is more capable but much slower on shared-memory hardware.

### "Thread reached the token limit"

- Start a new thread for each focused task.
- Keep the context size and `max_tokens` matched to the `--ctx-size` value.
- Once tool calling is working, fewer tokens are wasted on narrated text, so the window lasts longer.

## Model options

| Model | License | Strength | Size (Q4_K_M) |
|-------|---------|----------|---------------|
| Qwen2.5-Coder-7B-Instruct | Apache 2.0 | Coding completions | ~4.7 GB |
| Qwen2.5-7B-Instruct | Apache 2.0 | Better tool calling | ~4.7 GB |
| Qwen2.5-Coder-14B-Instruct | Apache 2.0 | Stronger agent editing | ~9 GB |

For this shared-RAM Lunar Lake machine, start with the 7B Instruct. Upgrade to 14B only if you can tolerate significantly slower response times.
