---
name: langgraph-docs
description: Use official LangGraph docs for implementation, API, state, orchestration, and human-in-the-loop guidance.
---

# langgraph-docs

## Workflow

1. Fetch index with `fetch_url`:
	 https://docs.langchain.com/llms.txt

2. Pick 2-3 relevant pages:
- how-to pages for implementation questions
- concept pages for architecture questions
- API reference for exact method behavior

3. Fetch selected pages and answer using doc-grounded guidance.

## Constraints

- Prefer official docs over external sources for LangGraph claims.
- Keep extracted details brief and implementation-focused.
- If a fetch fails, retry once; then report failure and point to:
	https://langchain-ai.github.io/langgraph/
