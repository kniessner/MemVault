---
title: Prompt Engineering
created: 2026-04-05
tags: [ai, concept, prompting]
---

# Prompt Engineering

> Systematic techniques for effectively communicating with LLMs to get desired outputs.

---

## Core Principles

1. **Be specific** — Vague prompts → vague outputs
2. **Provide context** — Model can't read your mind
3. **Show examples** — Few-shot beats instructions
4. **Break it down** — Complex tasks in steps
5. **Iterate** — Rarely perfect on first try

---

## Pattern 1: Zero-Shot

Direct instruction without examples.

```
Classify this review as positive, neutral, or negative.

Review: "The product arrived broken and customer service was useless."
```

**Best for:** Simple, well-defined tasks

---

## Pattern 2: Few-Shot

Provide examples of desired input/output.

```
Classify sentiment:

Review: "Best purchase ever!" → Positive
Review: "It's okay, nothing special" → Neutral
Review: "Total waste of money" → Negative
Review: "Works fine but shipping was slow" →
```

**Best for:** Defining output format, teaching style

---

## Pattern 3: Chain-of-Thought (CoT)

Prompt model to show reasoning.

```
Q: A farmer has 10 sheep. All but 3 die. How many remain?
A: Let's think step by step.
The question says "all but 3 die".
This means 3 sheep did NOT die.
So 3 sheep remain.

Q: Roger has 5 balls. He buys 2 more cans, each with 3 balls.
How many balls does he have?
A: Let's think step by step.
```

**Trigger phrases:**
- "Let's think step by step"
- "Explain your reasoning"
- "Work through this systematically"

**Best for:** Math, logic, multi-step problems

---

## Pattern 4: System Prompt Design

Set global behavior and constraints.

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": """You are a senior Python code reviewer.
            
Rules:
- Be concise, focus on critical issues
- Suggest specific code improvements
- Explain WHY, not just WHAT
- Use type hints in suggestions
- Flag security issues with [SECURITY]"""
        },
        {
            "role": "user",
            "content": code_to_review
        }
    ]
)
```

**System prompt components:**
- Role definition
- Tone/style
- Constraints/don'ts
- Output format
- Examples (if needed)

---

## Pattern 5: Role Prompting

Assign specific persona.

```
You are an expert cybersecurity consultant with 20 years experience.

Review this system architecture for vulnerabilities:
[architecture]

Provide:
1. Critical risks (CVSS score)
2. Recommended mitigations
3. Priority order
```

**Best for:** Shaping expertise, tone, perspective

---

## Pattern 6: Structured Output

Enforce consistent format.

```python
from pydantic import BaseModel

class Analysis(BaseModel):
    sentiment: str  # "positive", "negative", "neutral"
    confidence: float  # 0-1
    key_phrases: list[str]
    suggestions: list[str]

response = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[{
        "role": "user",
        "content": "Analyze this feedback: Great product but slow shipping"
    }],
    response_format=Analysis
)

result = response.choices[0].message.parsed
```

**Best for:** APIs, parsing, downstream processing

---

## Pattern 7: Template Filling

Pre-defined structure with variables.

```
Extract information from this article:

Article: {article_text}

Format:
TITLE: [article title]
AUTHOR: [author name or "Unknown"]
KEY_POINTS:
- [point 1]
- [point 2]
- [point 3]
SUMMARY: [2 sentence summary]
SENTIMENT: [positive/neutral/negative]
```

**Best for:** Consistent extraction, automated processing

---

## Pattern 8: Self-Consistency

Generate multiple answers, take most common.

```python
answers = []
for _ in range(5):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": question}],
        temperature=0.7  # Higher for diversity
    )
    answers.append(response.choices[0].message.content)

# Take majority answer (for classification)
from collections import Counter
final_answer = Counter(answers).most_common(1)[0][0]
```

**Best for:** Reducing random errors, critical decisions

---

## Pattern 9: Tree of Thoughts

Explore multiple reasoning paths.

```
Solve this problem. Consider multiple approaches:

Problem: {problem}

Generate 3 different approaches:

Approach 1: [first method]
- Pros: 
- Cons:

Approach 2: [second method]
- Pros:
- Cons:

Approach 3: [third method]
- Pros:
- Cons:

Now evaluate all approaches and choose the best one.
Execute the best approach step by step.
```

**Best for:** Complex problem solving, planning

---

## Pattern 10: Iterative Refinement

Generate → Critique → Improve.

```python
# Step 1: Generate
v1 = generate("Write a blog post about AI")

# Step 2: Critique
critique = generate(f"""
Review this blog post and identify weaknesses:
{v1}

Critique:
""")

# Step 3: Improve
v2 = generate(f"""
Original:
{v1}

Critique:
{critique}

Rewrite addressing all critique points:
""")
```

**Best for:** High-quality creative/content tasks

---

## Temperature Guide

| Temperature | Use Case |
|-------------|----------|
| **0.0** | Deterministic, extraction, code |
| **0.3** | Reliable, balanced |
| **0.7** | Creative, diverse |
| **1.0** | Maximum creativity |

---

## Common Pitfalls

❌ **Too vague** — "Write something good"
❌ **Conflicting instructions** — "Be brief but comprehensive"
❌ **Assuming knowledge** — Not providing context
❌ **No examples** — When format matters
❌ **All in one prompt** — Not breaking down complex tasks
❌ **Ignoring edge cases** — Not specifying what NOT to do

---

## Resources

- **OpenAI Best Practices**: https://platform.openai.com/docs/guides/prompt-engineering
- **Anthropic Prompting**: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
- **Prompt Engineering Guide**: https://www.promptingguide.ai/

---

## Related

- [[20-knowledge/ai/concepts/chain-of-thought|Chain-of-Thought]]
- [[20-knowledge/ai/concepts/rag-patterns|RAG Patterns]]
- [[20-knowledge/ai/models/gpt-4o|GPT-4o]] — Best for prompt engineering

---

*Last updated: 2026-04-05*
