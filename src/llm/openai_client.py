"""OpenAI client for generating responses based on context."""

import os
from pathlib import Path
from typing import Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from project root
env_path = Path(__file__).parents[2] / '.env'
load_dotenv(env_path)

class OpenAIClient:
    """Client for interacting with OpenAI's API."""
    
    def __init__(self):
        """Initialize the OpenAI client with API key and model configuration."""
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
            
        self.model = os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview")
        self.client = OpenAI(api_key=self.api_key)
        
    def generate_response(self, question: str, context: Optional[str] = None) -> str:
        """Generate a response to a question using optional context.
        
        Args:
            question: The user's question
            context: Optional context from RAG retrieval
            
        Returns:
            str: The generated response
        """
        messages = []
        
        if context:
            messages.append({
                "role": "system",
                "content": f"Use the following context to answer the question:\n\n{context}"
            })
            
        messages.append({
            "role": "user",
            "content": question
        })
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error generating response: {str(e)}" 