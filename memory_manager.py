import streamlit as st
import json
from datetime import datetime

class MemoryManager:
    """Manage user session memory for context-aware interactions."""
    
    def __init__(self):
        if "user_history" not in st.session_state:
            st.session_state.user_history = []
    
    def save_interaction(self, user_inputs, response):
        """Save user inputs and response to session history."""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "inputs": user_inputs,
            "response": response
        }
        st.session_state.user_history.append(interaction)
    
    def get_context(self):
        """Retrieve relevant context from history."""
        if not st.session_state.user_history:
            return None
        # Return the most recent interaction as context
        last_interaction = st.session_state.user_history[-1]
        return f"Previous Inputs: {json.dumps(last_interaction['inputs'], indent=2)}\nPrevious Response: {last_interaction['response'][:200]}..."
    
    def clear_history(self):
        """Clear session history."""
        st.session_state.user_history = []