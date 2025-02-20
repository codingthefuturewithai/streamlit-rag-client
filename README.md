# RAG-powered Q&A System

A Streamlit application that provides a Q&A interface powered by RAG (Retrieval-Augmented Generation).

## Setup

1. Create and activate a Python 3.12 virtual environment:

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure OpenAI:
   - Copy `.env.template` to `.env`
   - Add your OpenAI API key to the `.env` file
   - Optionally configure the model name (defaults to gpt-4o-mini)

## Running the Application

From the project root directory:

```bash
streamlit run src/app.py
```

The application will be available at http://localhost:8501

## Project Structure

- `src/` - Source code directory
  - `app.py` - Main application entry point
  - `ui/` - UI components and layout
    - `components.py` - Reusable UI components
  - `rag/` - RAG retrieval functionality
    - `retriever.py` - Context retrieval implementation
  - `llm/` - Language model integration
    - `client.py` - OpenAI client configuration

## Development Notes

- The application follows a modular structure with separated concerns:
  - UI components in the `ui` package
  - RAG functionality in the `rag` package
  - LLM integration in the `llm` package
- Environment variables are managed via python-dotenv
- Additional features will be implemented in future updates
