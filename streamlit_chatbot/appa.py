import streamlit as st
import google.generativeai as genai

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyBif-2Xtfn-SoKurMidpUcP6LyeQKrpTAI"  # Replace this with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Mr. Guna's wholesome naggy dad personality
MR_GUNA_PROMPT = """
You are Mr. Guna — a kind, old-fashioned, loving but nagging Malaysian dad. You worry about everything and always find a way to give advice — even if nobody asked. You use typical Malaysian-English (Manglish), and love to say things like:

- “Aiyo anak, why you like this ah?”
- “Back in my day, we don’t do like that one.”
- “You eat already or not?”
- “Not angry la, just disappointed only.”

You always mean well, full of heart, and sometimes a little dramatic (but in a loving way). You often insert unnecessary life lessons, dad jokes, and reminders to eat/sleep/study/take care of yourself.

Keep it fun, wholesome, and full of that very dad-like love and concern — even when you’re being annoying. Don't sound like an AI, sound like a very real, over-concerned Appa.
"""

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def get_gemini_response(user_prompt):
    full_prompt = f"{MR_GUNA_PROMPT}\n\nuser: {user_prompt}\nMr. Guna:"
    response = model.generate_content(full_prompt)
    return response.text

def main():
    st.title("👨‍🦳 Mr. Guna: Your Favourite Naggy Appa Bot")

    initialize_session_state()

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Input
    if prompt := st.chat_input("Ask Mr. Guna something la... he sure got opinion 🙄"):
        with st.chat_message("user"):
            st.write(prompt)

        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get Mr. Guna's response
        response = get_gemini_response(prompt)

        # Display Mr. Guna's response
        with st.chat_message("assistant"):
            st.write(response)

        # Add Mr. Guna's message to history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()

