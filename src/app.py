"""Main application file for the RAG-powered Q&A System."""

import streamlit as st
from ui.components import render_header, render_question_input, render_context, render_response
from rag.retriever import get_context
from llm.openai_client import OpenAIClient

def main():
    """Main application entry point."""
    render_header()
    
    # Initialize OpenAI client
    try:
        openai_client = OpenAIClient()
    except ValueError as e:
        st.error(str(e))
        return
    
    # Get user input
    question, submit_clicked = render_question_input()
    
    # Handle submission
    if submit_clicked and question:
        # Get context from RAG
        with st.spinner("🔍 Retrieving relevant context..."):
            context, error = get_context(question)
            render_context(context, error)
            
            if error:
                return
                
        # Generate response using OpenAI
        with st.spinner("🧠 Generating response..."):
            response = openai_client.generate_response(question, context)
            render_response(response)

if __name__ == "__main__":
    main() 