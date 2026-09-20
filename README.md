# LinkedInGenAI

## RAG-Powered Multi-Agent LinkedIn Content Generator

LinkedInGenAI is a Generative AI application that creates personalized
LinkedIn posts using Retrieval-Augmented Generation (RAG) and a
multi-agent refinement workflow.

## Features

- Semantic search using Sentence Transformers
- FAISS vector similarity search
- Retrieval-Augmented Generation (RAG)
- Gemini-based content generation
- AI-powered content evaluation
- Critic agent
- Optimizer agent
- Streamlit interface
- Multiple tones and languages

## Architecture

User
↓
Streamlit UI
↓
User Requirements
↓
Sentence Transformer
↓
FAISS Vector Search
↓
Relevant LinkedIn Posts
↓
Gemini Generator
↓
Critic Agent
↓
Final LinkedIn Post

Optional:

Critic Feedback
↓
Optimizer Agent
↓
Improved Post
↓
Final Evaluation

## Technology Stack

- Python
- Streamlit
- Google Gemini API
- Sentence Transformers
- FAISS
- Pandas
- NumPy
- LangChain
- LangGraph

## Dataset

The project uses a LinkedIn post dataset containing post text and
metadata such as engagement, language, tone, tags, and line count.

The dataset is used as a retrieval and reference corpus rather than
for LLM fine-tuning.

## Running Locally

### Install dependencies

```bash
pip install -r requirements.txt