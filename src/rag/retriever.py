"""RAG retriever integration module."""

import subprocess
from typing import Optional, Tuple

def get_context(query: str) -> Tuple[Optional[str], Optional[str]]:
    """Get relevant context for a query using the rag-retriever CLI tool.
    
    Args:
        query: The user's question to find context for
        
    Returns:
        Tuple[Optional[str], Optional[str]]: A tuple containing:
            - The retrieved context if successful, None if failed
            - An error message if failed, None if successful
    """
    try:
        # Run the rag-retriever command
        result = subprocess.run(
            ["rag-retriever", "--query", query],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Return the output if successful
        return result.stdout.strip(), None
        
    except FileNotFoundError:
        return None, "RAG retriever tool not found. Please ensure it is installed and in your PATH."
        
    except subprocess.CalledProcessError as e:
        # Handle command execution errors
        error_msg = e.stderr.strip() if e.stderr else "An error occurred while retrieving context."
        return None, f"Failed to get context: {error_msg}"
        
    except Exception as e:
        # Handle any other unexpected errors
        return None, f"An unexpected error occurred: {str(e)}" 