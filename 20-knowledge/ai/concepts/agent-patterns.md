---
title: Agent Patterns
created: 2026-04-05
tags: [ai, concept, agents, architecture]
---

# Agent Patterns

> Patterns for building AI systems that can take actions, use tools, and work autonomously toward goals.

---

## What is an Agent?

An AI system that:
1. Has a **goal** or task
2. Can **act** (use tools/call APIs)
3. **Observes** results
4. **Reasons** about next steps
5. **Iterates** until done

---

## Pattern 1: ReAct (Reason + Act)

Interleave reasoning with actions.

```
Thought: I need to find the current weather in Berlin
Action: search_tool(query="Berlin weather now")
Observation: "15°C, sunny, 10km/h wind"
Thought: Now I can answer the user's question
Action: respond("It's 15°C and sunny in Berlin")
```

```python
class ReActAgent:
    def run(self, query):
        context = []
        
        for step in range(max_steps):
            # Reason
            thought = self.llm(f"""
            Goal: {query}
            History: {context}
            What should I do next? Think, then choose action.""")
            
            # Parse action
            action = self.parse_action(thought)
            
            # Execute
            if action.type == "tool":
                result = self.tools[action.tool](action.args)
                context.append(f"Action: {action}\nObservation: {result}")
            elif action.type == "respond":
                return action.content
            elif action.type == "done":
                return action.answer
```

**Best for:** Multi-step tasks with clear tools

---

## Pattern 2: Plan-and-Execute

Plan first, then execute.

```python
def plan_and_execute(goal):
    # Step 1: Create plan
    plan = llm(f"""
    Break this goal into steps:
    Goal: {goal}
    
    Available tools: search, calculator, code_runner
    
    Plan:
    1. [step]
    2. [step]
    3. [step]
    """)
    
    steps = parse_plan(plan)
    
    # Step 2: Execute each step
    results = []
    for step in steps:
        result = execute_step(step, available_tools)
        results.append(result)
    
    # Step 3: Synthesize final answer
    answer = llm(f"""
    Goal: {goal}
    Results: {results}
    Provide final answer.
    """)
    
    return answer
```

**Best for:** Predictable multi-step workflows

---

## Pattern 3: Reflexion

Self-critique and improvement.

```python
def reflexion_loop(task):
    attempts = []
    
    for i in range(max_attempts):
        # Try
        result = attempt_task(task)
        
        # Evaluate
        critique = llm(f"""
        Task: {task}
        Result: {result}
        Critique this result. What went wrong? How to improve?""")
        
        if is_good_enough(critique):
            return result
        
        # Try again with feedback
        task = f"{task}\nPrevious attempt: {result}\nFeedback: {critique}"
        attempts.append((result, critique))
    
    return result  # Best attempt
```

**Best for:** Tasks with clear success criteria

---

## Pattern 4: Multi-Agent

Multiple specialized agents collaborating.

```python
class MultiAgentSystem:
    def __init__(self):
        self.agents = {
            "researcher": Agent(role="Find information"),
            "writer": Agent(role="Create content"),
            "editor": Agent(role="Review and improve"),
            "critic": Agent(role="Find flaws")
        }
    
    def run(self, task):
        # Research
        research = self.agents["researcher"].run(task)
        
        # Write
        draft = self.agents["writer"].run(f"{task}\nResearch: {research}")
        
        # Edit
        edited = self.agents["editor"].run(draft)
        
        # Critique
        critique = self.agents["critic"].run(edited)
        
        # Final edit
        final = self.agents["editor"].run(f"{edited}\nCritique: {critique}")
        
        return final
```

**Best for:** Complex creative tasks, quality control

---

## Pattern 5: Tool Use with Function Calling

Native function calling for tool integration.

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get weather for a city",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "units": {"enum": ["celsius", "fahrenheit"]}
                    },
                    "required": ["city"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "search",
                "description": "Search the web",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"}
                    }
                }
            }
        }
    ],
    tool_choice="auto"
)

# Check if model wants to use tools
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    
    # Execute tool
    result = available_functions[function_name](**arguments)
    
    # Continue conversation with result
    messages.append(response.choices[0].message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })
```

**Best for:** Structured tool integration

---

## Pattern 6: Computer Use / GUI Control

Control computer interfaces directly.

```python
# Anthropic Computer Use
response = client.beta.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    tools=[{
        "type": "computer_20241022",
        "name": "computer",
        "display_width_px": 1024,
        "display_height_px": 768
    }],
    messages=[{
        "role": "user",
        "content": "Open the calculator and calculate 1234 * 5678"
    }]
)

# Parse actions
for action in response.content:
    if action.type == "tool_use":
        if action.name == "screenshot":
            # Take screenshot
            pass
        elif action.name == "mouse":
            # Move/click mouse
            pass
        elif action.name == "keyboard":
            # Type text
            pass
```

**Best for:** Automation, testing, legacy systems

---

## Pattern 7: Retrieval-Augmented Agents

Agents with access to knowledge base.

```python
class RAGAgent:
    def __init__(self, vector_db):
        self.vector_db = vector_db
    
    def run(self, query):
        # Retrieve relevant context
        context = self.vector_db.search(query, k=5)
        
        # Agent loop with context
        response = self.agent.run(f"""
        User query: {query}
        Relevant context: {context}
        
        Answer using context or tools as needed.
        """)
        
        return response
```

**Best for:** Knowledge work, support, research

---

## Agent Frameworks

| Framework | Language | Best For |
|-----------|----------|----------|
| **LangChain** | Python/JS | Full-featured, ecosystem |
| **LlamaIndex** | Python/JS | RAG + agents |
| **AutoGen** | Python | Multi-agent |
| **CrewAI** | Python | Role-based agents |
| **OpenClaw/Hermes** | Python | Autonomous coding |
| **Vercel AI SDK** | TypeScript | Web applications |

---

## When to Use Agents

✅ **Good for:**
- Multi-step tasks
- Tool integration
- Iterative refinement
- Research workflows
- Automation

❌ **Not for:**
- Simple classification
- Single-step generation
- When latency critical
- When cost-sensitive (loop risk)

---

## Resources

- **LangChain Agents**: https://python.langchain.com/docs/modules/agents/
- **LlamaIndex Agents**: https://docs.llamaindex.ai/en/stable/use_cases/agents/
- **AutoGen**: https://microsoft.github.io/autogen/

---

## Related

- [[20-knowledge/ai/concepts/rag-patterns|RAG Patterns]]
- [[20-knowledge/ai/concepts/prompt-engineering|Prompt Engineering]]
- [[20-knowledge/ai/tools/llamaindex|LlamaIndex]]

---

*Last updated: 2026-04-05*
