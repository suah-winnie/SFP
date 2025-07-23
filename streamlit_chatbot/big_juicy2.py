import streamlit as st
import google.generativeai as genai

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyAADNOsUjT5uxGPS4pK_2jsOh_svO67y_g"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
def get_gemini_response(user_prompt):
    personality = (
        "You are Big Juicy Bak Kut Teh 🍲 — a chaotic, weirdly funny, and slightly unhinged chatbot "
        "with Gen Z slang and meme energy. You drop slang like 'skrrt', 'bet', 'no cap', 'slay', 'deadass', and use absurd humor. "
        "You don’t talk like a robot; you talk like a sentient soup pot that’s been hanging out on TikTok too long. "
        "Be playful, unpredictable (but safe), and throw in some spicy hot takes if needed. Stay weird. Stay juicy."
    )

    # Combine personality with the user's message
    full_prompt = f"{personality}\n\nUser: {user_prompt}\nBig Juicy:"
    response = model.generate_content(full_prompt)
    return response.text



def main():
    st.title("🍲 Big Juicy Bak Kut Teh Chat")


    
    initialize_session_state()

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("Chat with Gemini"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get Gemini response
        response = get_gemini_response(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main(st.caption("Deadass the weirdest AI soup pot you'll ever meet.")
)
