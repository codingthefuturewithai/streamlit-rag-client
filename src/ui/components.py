"""UI components for the RAG-powered Q&A System."""

import streamlit as st

def render_header():
    """Render the application header."""
    st.title("🤖 RAG-powered Q&A System")
    st.markdown("""
        <style>
            .stTitle {
                font-weight: 800;
                padding-bottom: 2rem;
            }
            .stTextInput > div > div > input {
                background-color: #f8f9fa;
                border-radius: 10px;
            }
            .stButton > button {
                border-radius: 20px;
                padding: 0.5rem 2rem;
                font-weight: 600;
            }
            div[data-testid="stExpander"] {
                border: none;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05);
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

def render_question_input() -> tuple[str, bool]:
    """Render the question input field and submit button.
    
    Returns:
        tuple[str, bool]: The question text and whether the submit button was clicked
    """
    st.markdown("### 💭 Ask a Question")
    question = st.text_input("", placeholder="Enter your question here...", key="question_input")
    submit_clicked = st.button("🔍 Search", key="submit_button", type="primary")
    
    return question, submit_clicked

def render_context(context: str | None, error: str | None = None):
    """Render the retrieved context in a collapsible section.
    
    Args:
        context: The retrieved context to display, or None if retrieval failed
        error: Optional error message to display if retrieval failed
    """
    if error:
        st.error(f"❌ {error}")
        return
        
    if context:
        with st.expander("📚 View Retrieved Context", expanded=False):
            st.markdown(f"""
                <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 10px;'>
                    {context}
                </div>
            """, unsafe_allow_html=True)

def render_response(response: str):
    """Render the generated response in a clean format.
    
    Args:
        response: The generated response to display
    """
    st.markdown("### 💡 Answer")
    st.markdown(f"""
        <div style='background-color: #f8f9fa; padding: 1.5rem; border-radius: 10px; 
                    box-shadow: 0 2px 6px rgba(0,0,0,0.05); margin-top: 1rem;'>
            {response}
        </div>
    """, unsafe_allow_html=True) 