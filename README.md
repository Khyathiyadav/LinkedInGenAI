# LinkedInGenAI

## RAG-Powered Multi-Agent LinkedIn Content Generator

LinkedInGenAI is a Generative AI application that creates personalized LinkedIn posts using **Retrieval-Augmented Generation (RAG)** and a **multi-agent refinement workflow**.

The application retrieves semantically similar LinkedIn posts from a reference dataset and provides them as contextual examples to a Gemini-based generator. A Critic Agent evaluates the generated content, while an Optimizer Agent can refine the post based on the critic's feedback.

---

## Features

- Semantic search using Sentence Transformers
- FAISS vector similarity search
- Retrieval-Augmented Generation (RAG)
- Gemini-based content generation
- AI-powered content evaluation
- Critic Agent
- Optimizer Agent
- Streamlit interactive interface
- Multiple tones and languages
- Configurable target audience and post length
- LLM-based quality evaluation

---

## Architecture

```text
                         User
                           │
                           ▼
                  ┌─────────────────┐
                  │  Streamlit UI   │
                  └────────┬────────┘
                           │
                           ▼
                  User Requirements
                           │
                           ▼
              ┌────────────────────────┐
              │ Sentence Transformer   │
              │      Embeddings        │
              └────────────┬───────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    FAISS    │
                    │Vector Search│
                    └──────┬──────┘
                           │
                           ▼
                 Retrieved LinkedIn
                       Examples
                           │
                           ▼
                  ┌─────────────────┐
                  │ Gemini Generator│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   Critic Agent  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Final Post     │
                  └─────────────────┘


              Optional Refinement Workflow

                  Critic Feedback
                           │
                           ▼
                  ┌─────────────────┐
                  │ Optimizer Agent │
                  └────────┬────────┘
                           │
                           ▼
                    Improved Post
                           │
                           ▼
                   Final Evaluation
