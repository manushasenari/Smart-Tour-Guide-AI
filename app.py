import streamlit as st
from generator import get_reply


# Streamlit page configuration
st.set_page_config(
    page_title="Smart Tour Guide",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* General styling */
    .main {
        background: linear-gradient(135deg, #E6F0FA 0%, #F8E9E9 100%);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background: linear-gradient(90deg, #2E86C1, #1B5E91);
        color: white;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        border: none;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        background: linear-gradient(90deg, #1B5E91, #2E86C1);
    }
    .stTextArea>label, .stSelectbox>label {
        font-size: 18px;
        font-weight: 600;
        color: #1B263B;
        margin-bottom: 8px;
    }
    .stTextArea>div>textarea, .stSelectbox>div>select {
        border-radius: 10px;
        border: 2px solid #D1E8F4;
        background-color: #FFFFFF;
        padding: 10px;
        font-size: 16px;
    }
    /* Header styling */
    .title {
        color: #1B263B;
        font-size: 42px;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
    .subtitle {
        color: #415A77;
        font-size: 20px;
        text-align: center;
        margin-bottom: 30px;
        font-style: italic;
    }
    /* Card for response */
    .response-card {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #2E86C1;
    }
    /* Example questions */
    .example {
        color: #778DA9;
        font-size: 15px;
        font-style: italic;
        margin-top: 15px;
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
    }
    /* Footer */
    .footer {
        text-align: center;
        color: #778DA9;
        font-size: 14px;
        margin-top: 40px;
    }
    /* Responsive design */
    @media (max-width: 600px) {
        .title { font-size: 32px; }
        .subtitle { font-size: 16px; }
        .stButton>button { padding: 10px 18px; }
    }
    </style>
""", unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown('<h1 class="title">🌍 Smart Tour Guide</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Your ultimate companion for personalized travel advice!</p>', unsafe_allow_html=True)

    # Layout with columns for a clean look
    col1, col2 = st.columns([2, 1])

    with col1:
        # Optional topic selector
        topic = st.selectbox(
            "📌 Select a travel topic (optional)",
            options=["General Travel", "Trip Planning", "Cultural Experiences", "Adventure Activities", "Food & Dining", "Budget Travel", "Family Travel"],
            help="Choose a topic to focus your question, or select 'General Travel' for any question.",
            key="topic_select"
        )

        # Free-form question input
        user_question = st.text_area(
            "✈️ What's your travel question?",
            placeholder="e.g., What's the best time to visit Japan? or Recommend budget hotels in Paris.",
            height=120,
            help="Type any travel-related question, and I'll provide a detailed answer!"
        )

        # Example questions for inspiration
        st.markdown("""
            <p class="example">Example questions:
            <ul class="example">
                <li>What are the top cultural sites in Rome?</li>
                <li>How can I plan a 5-day trip to Iceland on a budget?</li>
                <li>What are the best hiking trails in New Zealand?</li>
                <li>Is it safe to travel to Morocco in December?</li>
            </ul></p>
        """, unsafe_allow_html=True)

    with col2:
        # Add a travel-themed image (placeholder URL, replace with your own)
        st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Explore the World!", use_column_width=True)

    # Submit button
    if st.button("Get Your Answer 🚀"):
        if user_question.strip():
            with st.spinner("Exploring the best travel advice..."):
                # Get response from Gemini (assuming get_reply is defined)
                try:
                    from generator import get_reply
                    reply = get_reply(user_question, topic)
                    with st.container():
                        st.markdown('<div class="response-card">', unsafe_allow_html=True)
                        st.subheader("🌟 Your Travel Answer")
                        st.markdown(reply, unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Oops! Something went wrong: {str(e)}")
        else:
            st.error("Please enter a question to get started!")

# Footer
st.markdown('<p class="footer">Powered by xAI • Explore the world with Smart Tour Guide 🌎</p>', unsafe_allow_html=True)