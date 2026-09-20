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
Sentence Transformer Embeddings
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

Optional Refinement:

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

## Dataset

This project uses the LinkedIn Post Generator Dataset from Kaggle,
licensed under **CC BY-SA 4.0**.

The dataset is used as a reference corpus for semantic retrieval
in the RAG pipeline.

**Dataset source:** [Add your original Kaggle dataset URL here]

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Khyathiyadav/LinkedInGenAI.git
cd LinkedInGenAI
