# LinkedInGenAI

## RAG-Powered Multi-Agent LinkedIn Content Generator

LinkedInGenAI is a Generative AI application that creates personalized LinkedIn posts using **Retrieval-Augmented Generation (RAG)** and a **multi-agent refinement workflow**.

The system retrieves semantically similar LinkedIn posts from a reference dataset using **Sentence Transformers and FAISS**, provides the retrieved examples as context to a **Gemini-based Generator Agent**, and evaluates the generated content using a **Critic Agent**. Users can optionally improve the generated post using an **Optimizer Agent** based on the critic's feedback.

---

## Features

- Retrieval-Augmented Generation (RAG)
- Semantic search using Sentence Transformers
- FAISS vector similarity search
- Gemini-based LinkedIn post generation
- Generator Agent
- Critic Agent
- Optimizer Agent
- LLM-based content evaluation
- Multiple tones and languages
- Configurable target audience
- Configurable post length
- Interactive Streamlit interface
- Optional post refinement workflow

---

## Architecture

### Main Generation Workflow

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
                  │  Generated Post │
                  └─────────────────┘
```

### Optional Refinement Workflow

```text
                  Generated Post
                         │
                         ▼
                User clicks
                "Improve Post"
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
                ┌─────────────────┐
                │   Critic Agent  │
                │ Final Evaluation│
                └────────┬────────┘
                         │
                         ▼
                  Final Improved
                       Post
```

### Overall System Flow

```text
User Requirements
       │
       ▼
Semantic Retrieval
       │
       ▼
Relevant Reference Posts
       │
       ▼
Gemini Generator
       │
       ▼
Critic Agent
       │
       ├──────────────► Generated Post
       │
       ▼
 Optional Refinement
       │
       ▼
Optimizer Agent
       │
       ▼
Improved Post
       │
       ▼
Final Critic Evaluation
```

---

## How It Works

### 1. User Input

The user provides the following requirements through the Streamlit interface:

- **Topic**
- **Tone**
- **Target audience**
- **Language**
- **Desired length**

These requirements are used to perform semantic retrieval and guide content generation.

### 2. Semantic Retrieval

The LinkedIn reference posts are converted into vector embeddings using the **Sentence Transformer `all-MiniLM-L6-v2`** model.

The embeddings are stored in a **FAISS IndexFlatIP** vector index.

When the user submits their requirements, the system creates an embedding for the query and retrieves the most semantically similar posts from the dataset.

### 3. Retrieval-Augmented Generation

The retrieved posts are passed to the **Gemini Generator Agent** as contextual references.

The generator uses these examples to understand:

- Writing patterns
- Structure
- Tone
- Content style

The generator is instructed to create an original LinkedIn post and not directly copy the retrieved examples.

### 4. Critic Agent

The generated post is evaluated by the **Critic Agent**.

The critic evaluates seven dimensions:

- Relevance
- Clarity
- Tone consistency
- Hook quality
- Readability
- Originality
- LinkedIn suitability

The Critic Agent also provides concise improvement feedback.

### 5. Optimizer Agent

The user can optionally select **Improve Post**.

The Optimizer Agent receives:

- The generated post
- Critic feedback
- Original user requirements

It then improves the post by addressing the identified weaknesses while preserving the core topic and requested tone.

The improved post is evaluated again by the Critic Agent.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Interactive web interface |
| Google Gemini API | Generative AI |
| Sentence Transformers | Text embeddings |
| FAISS | Vector similarity search |
| Pandas | Data processing |
| NumPy | Numerical operations |
| python-dotenv | Environment variable management |

---

## Dataset

This project uses the **LinkedIn Post Generator Dataset** from Kaggle as a reference corpus for the RAG pipeline.

The dataset contains LinkedIn-style posts with associated metadata such as:

- Text
- Engagement
- Line count
- Language
- Tags
- Tone

The dataset is used primarily for **semantic retrieval and contextual reference** during generation.

### Dataset License

The dataset is licensed under **CC BY-SA 4.0**.

### Dataset Source

**Kaggle:**  
(https://www.kaggle.com/datasets/prishatank/post-generator-dataset)]

The original dataset attribution and license should be preserved when redistributing the dataset.

---

## RAG Pipeline

The RAG pipeline consists of the following steps:

```text
                   LinkedIn Dataset
                          │
                          ▼
                    Text Extraction
                          │
                          ▼
                Sentence Transformer
                          │
                          ▼
                     Embeddings
                          │
                          ▼
                  FAISS Vector Index
                          │
                          │
                          │
User Requirements ────────┘
       │
       ▼
Query Embedding
       │
       ▼
Similarity Search
       │
       ▼
Top-K Relevant Posts
       │
       ▼
Gemini Generator
       │
       ▼
Generated LinkedIn Post
```

### Embedding Model

The project uses:

```text
all-MiniLM-L6-v2
```

The generated embeddings are normalized before being added to the FAISS index.

### Retrieval

The system uses FAISS **inner-product similarity search** to retrieve the most relevant reference posts.

By default, the application retrieves the top **3** similar posts.

---

## Multi-Agent Workflow

### Generator Agent

The Generator Agent creates a LinkedIn post using:

- User requirements
- Retrieved reference posts
- Requested tone
- Target audience
- Language
- Desired length

The agent is instructed to produce original content rather than copying the retrieved examples.

### Critic Agent

The Critic Agent evaluates the generated post using seven dimensions:

```text
1. Relevance
2. Clarity
3. Tone Consistency
4. Hook Quality
5. Readability
6. Originality
7. LinkedIn Suitability
```

It returns structured JSON containing the evaluation scores and improvement feedback.

### Optimizer Agent

The Optimizer Agent uses the critic's feedback to improve the generated post.

It focuses on:

- Strengthening the opening hook
- Increasing specificity
- Improving originality
- Addressing critic feedback
- Preserving the requested tone
- Maintaining the original topic
- Improving readability

---

## Evaluation

The Critic Agent provides an LLM-based evaluation of generated posts.

| Metric | Description |
|---|---|
| Relevance | Alignment with the requested topic |
| Clarity | How clearly the message is communicated |
| Tone Consistency | Consistency with the requested tone |
| Hook Quality | Effectiveness of the opening |
| Readability | Ease of reading and organization |
| Originality | Originality of the generated expression |
| LinkedIn Suitability | Suitability for LinkedIn content |

The evaluation is intended as a **heuristic LLM-based assessment** and should not be interpreted as a statistically validated human evaluation.

---

## Project Structure

```text
LinkedInGenAI/
│
├── agents/
│   ├── __init__.py
│   ├── generator.py
│   ├── critic.py
│   └── optimizer.py
│
├── data/
│   └── posts.json
│
├── rag/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── test_rag.py
│
├── app.py
├── data_test.py
├── test_critic.py
├── test_gemini.py
├── test_generation.py
├── test_optimizer.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Khyathiyadav/LinkedInGenAI.git
cd LinkedInGenAI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API Key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Do not commit the `.env` file to GitHub.

The `.gitignore` file is configured to exclude the `.env` file.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Environment Variables

The application requires the following environment variable:

```text
GEMINI_API_KEY
```

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

Keep API keys private and never hard-code them into the application source code.

---

## Testing

The project contains separate test scripts for individual components:

```text
data_test.py
test_gemini.py
test_generation.py
test_critic.py
test_optimizer.py
```

### Test the RAG Pipeline

```bash
python rag/test_rag.py
```

The test verifies:

- Dataset loading
- Embedding generation
- FAISS index creation
- Semantic retrieval

---

## Security

Sensitive configuration is excluded from version control.

The `.gitignore` file prevents the following from being committed:

```text
.env
venv/
__pycache__/
*.pyc
```

The Gemini API key is loaded through an environment variable rather than being stored directly in the source code.

---

## Limitations

- The reference dataset is relatively small and is primarily used for contextual retrieval.
- LLM-based evaluation can vary between generations.
- Critic scores are heuristic and are not a substitute for human evaluation.
- Generated content should be reviewed before publishing.
- The application currently relies on the availability and quota of the Gemini API.

---

## Future Improvements

Potential extensions include:

- Persistent vector databases
- Conversation memory
- User-specific writing style adaptation
- Human feedback collection
- Automated evaluation benchmarks
- Cloud deployment
- Authentication and user profiles
- Improved observability and logging
- Additional social media content generation
- More advanced agent orchestration

---

## Disclaimer

The generated content is AI-generated and should be reviewed and edited by the user before publishing.
