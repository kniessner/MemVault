---
name: session-summary
description: Display a comprehensive summary of the current session including token usage, provider/model, tools used, and skills invoked
allowed-tools: session_status, sessions_history
---

# Session Summary Skill

Provide a detailed summary of the current conversation session when the user asks for it.

## When to Use

Use this skill when the user asks for:
- "session summary"
- "token usage"
- "what tools did you use"
- "session stats"
- "cost report"
- Or similar requests for session analytics

## Information to Provide

### 1. Session Metadata
- Session key/ID
- Start time and duration
- Model and provider used
- Thinking/reasoning mode (if enabled)

### 2. Token Usage
- Input tokens consumed
- Output tokens generated
- Total tokens
- Cache read/write stats (if available)

### 3. Cost Estimation
- Estimated cost in USD (if pricing data available)
- Breakdown by input/output

### 4. Tools Used
List all tools invoked during the session:
- `read` - File reading
- `write` - File creation
- `edit` - File modifications
- `bash` - Shell command execution
- `glob` - File pattern search
- `grep` - Content search
- `web_fetch` - URL content fetching
- etc.

### 5. Skills Used
List any skills that were:
- Detected and loaded from SKILL.md
- Followed during the conversation

### 6. Notable Actions
Highlight significant operations:
- Files created/modified
- Commands executed
- Web resources accessed

## Output Format

```
SESSION SUMMARY
════════════════════════════════════════════

MODEL & PROVIDER
   Provider: [provider]
   Model: [model]
   Session Duration: [duration]

TOKEN USAGE
   Input: [X] tokens
   Output: [Y] tokens
   Total: [Z] tokens
   Est. Cost: $[amount]

TOOLS USED ([N] total)
   * tool1 (X invocations)
   * tool2 (Y invocations)

SKILLS REFERENCED
   * skill1
   * skill2

NOTABLE ACTIONS
   * Created: [files]
   * Modified: [files]
   * Executed: [commands]

════════════════════════════════════════════
```

## Implementation Notes

1. Use `session_status` to get current session info
2. Use `sessions_history` to get detailed turn-by-turn info
3. Parse tool calls from the session history
4. Identify skills by checking which SKILL.md files were loaded
5. Calculate duration from first to last message timestamp

## Example Usage

User: "Give me a session summary"
-> Run session_status
-> Run sessions_history (limit=1000)
-> Parse and summarize the data
-> Present formatted output