import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import io
from deep_translator import GoogleTranslator

# Load environment variables from .env file
load_dotenv()

# Initialize Gemini client with API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern dark theme with gradient and glassmorphism
st.markdown("""
    <style>
    /* Main background with gradient */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Sidebar text color - blue */
    [data-testid="stSidebar"] * {
        color: #667eea !important;
    }

    /* Sidebar headers */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #667eea !important;
    }

    /* Sidebar info box */
    [data-testid="stSidebar"] .stAlert {
        background: rgba(102, 126, 234, 0.1) !important;
        color: #667eea !important;
    }

    /* Chat message containers */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 15px;
        margin: 10px 0;
    }

    /* Input field styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.95) !important;
        border: 2px solid rgba(102, 126, 234, 0.5) !important;
        border-radius: 25px !important;
        color: #667eea !important;
        padding: 12px 20px !important;
        font-weight: 500 !important;
        font-size: 16px !important;
    }

    .stTextInput > div > div > input:focus {
        border: 2px solid #667eea !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3) !important;
        background: white !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(102, 126, 234, 0.5) !important;
        font-weight: 400 !important;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }

    /* Title and headers */
    h1 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        font-weight: 700;
    }

    h2, h3 {
        color: rgba(255, 255, 255, 0.95);
    }

    /* Info box styling */
    .element-container div[data-testid="stMarkdownContainer"] p {
        color: rgba(255, 255, 255, 0.9);
    }

    /* Chat input */
    .stChatInput > div {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .stChatInput input {
        color: white;
    }

    /* Divider */
    hr {
        border-color: rgba(255, 255, 255, 0.2);
    }

    /* Audio recorder component - remove white background */
    .st-emotion-cache-1v0mbdj > div {
        background: transparent !important;
    }

    /* Audio recorder styling */
    iframe[title="streamlit_audio_recorder.audio_recorder"] {
        background: transparent !important;
    }

    /* Remove white background from audio recorder container */
    [data-testid="stVerticalBlock"] > div:has(iframe[title*="audio_recorder"]) {
        background: transparent !important;
    }

    /* Target all potential audio recorder containers */
    div[data-testid="column"] > div {
        background: transparent !important;
    }

    /* Remove background from all divs containing iframe */
    div:has(> iframe) {
        background: transparent !important;
    }

    /* Specific targeting for the component wrapper */
    .element-container:has(iframe[title*="audio_recorder"]) {
        background: transparent !important;
    }

    /* Override any default backgrounds in columns */
    [data-testid="column"] {
        background: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Add some spacing at the top
st.markdown("<br>" * 2, unsafe_allow_html=True)

# Robot icon/image centered at the top
st.markdown("""
<div style='text-align: center; margin-bottom: 30px;'>
    <div style='font-size: 80px; animation: float 3s ease-in-out infinite;'>
        🤖
    </div>
</div>

<style>
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}
</style>
""", unsafe_allow_html=True)

# App title and description with modern look (moved down)
st.title("✨ AI Chatbot")
st.markdown("""
<div style='background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 20px; border-radius: 15px; border: 1px solid rgba(255, 255, 255, 0.2); margin-bottom: 20px;'>
    <h3 style='margin: 0; color: white;'>👋 Welcome!</h3>
    <p style='margin: 10px 0 0 0; color: rgba(255, 255, 255, 0.9);'>
        I'm your AI assistant powered by Google Gemini. Ask me anything - from creative writing to technical questions!
    </p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "personality" not in st.session_state:
    st.session_state.personality = "General Assistant"
if "voice_text" not in st.session_state:
    st.session_state.voice_text = ""
if "voice_language" not in st.session_state:
    st.session_state.voice_language = "en-US"
if "translate_to" not in st.session_state:
    st.session_state.translate_to = "english"
if "show_translation" not in st.session_state:
    st.session_state.show_translation = False

# Function to transcribe audio with language support
def transcribe_audio(audio_bytes, language="en-US"):
    """Convert audio bytes to text using speech recognition"""
    recognizer = sr.Recognizer()
    try:
        # Save audio to temporary wav file for processing
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            temp_audio.write(audio_bytes)
            temp_audio_path = temp_audio.name

        # Load audio file and transcribe with specified language
        with sr.AudioFile(temp_audio_path) as source:
            audio_data = recognizer.record(source)
            # Recognize speech in the specified language
            text = recognizer.recognize_google(audio_data, language=language)

        # Clean up temp file
        import os
        os.unlink(temp_audio_path)

        return text
    except sr.UnknownValueError:
        return "Could not understand audio. Please speak clearly."
    except sr.RequestError as e:
        return f"Speech recognition service error: {e}"
    except Exception as e:
        return f"Error: {str(e)}"

# Voice input section with microphone and text input
st.markdown("""
<div style='background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 20px; border-radius: 15px; border: 1px solid rgba(255, 255, 255, 0.2); margin-bottom: 20px;'>
    <p style='margin: 0 0 15px 0; color: white; text-align: center; font-size: 1.1em;'>
        🎤 <strong>Voice Input</strong> or 💬 <strong>Type Below</strong>
    </p>
""", unsafe_allow_html=True)

# Audio recorder centered
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    audio_bytes = audio_recorder(
        text="",
        recording_color="#e74c3c",
        neutral_color="#667eea",
        icon_name="microphone",
        icon_size="2x",
    )

# Text input box below microphone
user_input = st.text_input(
    "Message Input",
    placeholder="Type your message here...",
    key="text_input",
    label_visibility="collapsed"
)

st.markdown("</div>", unsafe_allow_html=True)

# Process audio if recorded
if audio_bytes:
    # Transcribe audio using selected language
    with st.spinner("🎧 Transcribing audio..."):
        transcribed_text = transcribe_audio(audio_bytes, st.session_state.voice_language)

    # Handle transcription result
    if transcribed_text and not any(transcribed_text.startswith(prefix) for prefix in ["Error", "Could not", "Speech recognition"]):
        # Show original transcription
        st.success(f"✅ **Transcribed:** {transcribed_text}")

        # Translate if translation is enabled and target language is different
        # Map speech recognition language codes to Google Translator language codes
        lang_code_map = {
            "en": "english",
            "zh": "chinese (simplified)",
            "yue": "chinese (traditional)",
            "fr": "french"
        }

        source_lang_code = st.session_state.voice_language.split('-')[0]
        source_lang = lang_code_map.get(source_lang_code, "auto")

        if st.session_state.show_translation and source_lang != st.session_state.translate_to:
            with st.spinner("🌐 Translating..."):
                try:
                    translated_text = GoogleTranslator(source=source_lang, target=st.session_state.translate_to).translate(transcribed_text)
                    st.session_state.voice_text = translated_text
                    # Don't show the info message - just translate silently
                except Exception as e:
                    # Silently use original text if translation fails
                    st.session_state.voice_text = transcribed_text
        else:
            st.session_state.voice_text = transcribed_text
    else:
        st.error(f"❌ {transcribed_text}")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Determine prompt from voice or text
prompt = None
if st.session_state.voice_text:
    prompt = st.session_state.voice_text
    st.session_state.voice_text = ""  # Clear after using
elif user_input:
    prompt = user_input

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Create messages for API call including system prompt with personality
        personality_prompts = {
            "General Assistant": "You are a helpful and knowledgeable AI assistant. Provide clear, accurate, and useful information. Be friendly and professional in your responses."
        }

        system_prompt = personality_prompts[st.session_state.personality]

        # Build conversation history for Gemini including system prompt
        conversation_history = []

        # Add system prompt as first user message if history is empty
        if len(st.session_state.messages) == 1:  # Only current message
            conversation_history.append({"role": "user", "parts": [system_prompt]})
            conversation_history.append({"role": "model", "parts": ["Understood! I'm ready to assist you. How can I help you today?"]})

        for msg in st.session_state.messages[:-1]:  # Exclude the current user message
            if msg["role"] == "user":
                conversation_history.append({"role": "user", "parts": [msg["content"]]})
            else:
                conversation_history.append({"role": "model", "parts": [msg["content"]]})

        # Stream response from Gemini API
        try:
            # Initialize the model
            model = genai.GenerativeModel("gemini-2.5-flash")

            # Start chat with history
            chat = model.start_chat(history=conversation_history)

            # Send message and stream response
            response = chat.send_message(prompt, stream=True)

            # Display streaming response
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")

            # Display final response
            message_placeholder.markdown(full_response)

        except Exception as e:
            full_response = f"❌ Error: {str(e)}\n\nPlease check your GEMINI_API_KEY in the .env file."
            message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with info
with st.sidebar:
    # Large animated robot icon at top
    st.markdown("""
    <div style='text-align: center; padding: 40px 0 20px 0;'>
        <div style='font-size: 120px; animation: float 3s ease-in-out infinite;'>
            🤖
        </div>
        <h2 style='margin: 10px 0 0 0; color: #667eea;'>AI Assistant</h2>
    </div>

    <style>
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    </style>
    """, unsafe_allow_html=True)

    st.divider()

    # Message count
    if len(st.session_state.messages) > 0:
        st.metric("💬 Messages", len(st.session_state.messages))
        st.divider()

    # Language selection for voice input
    st.markdown("### 🎤 Speak In")

    input_language_options = {
        "🇺🇸 English": "en-US",
        "🇨🇳 Chinese (Mandarin)": "zh-CN",
        "🇭🇰 Cantonese": "yue-Hant-HK",
        "🇫🇷 French": "fr-FR"
    }

    selected_input_language = st.selectbox(
        "Select language to speak:",
        options=list(input_language_options.keys()),
        index=0,
        label_visibility="collapsed",
        key="input_lang"
    )

    st.session_state.voice_language = input_language_options[selected_input_language]

    # Toggle button for translation
    if st.button("🌐 Enable Translation" if not st.session_state.show_translation else "✅ Translation Enabled",
                 use_container_width=True,
                 type="primary" if st.session_state.show_translation else "secondary"):
        st.session_state.show_translation = not st.session_state.show_translation
        st.rerun()

    # Show translation options only if enabled
    if st.session_state.show_translation:
        st.markdown("### 🌐 Translate To")

        output_language_options = {
            "🇺🇸 English": "english",
            "🇨🇳 Chinese (Simplified)": "chinese (simplified)",
            "🇹🇼 Chinese (Traditional)": "chinese (traditional)",
            "🇫🇷 French": "french",
            "🇪🇸 Spanish": "spanish",
            "🇩🇪 German": "german",
            "🇯🇵 Japanese": "japanese",
            "🇰🇷 Korean": "korean",
            "🇮🇹 Italian": "italian",
            "🇵🇹 Portuguese": "portuguese",
            "🇷🇺 Russian": "russian",
            "🇸🇦 Arabic": "arabic",
            "🇮🇳 Hindi": "hindi"
        }

        selected_output_language = st.selectbox(
            "Select language to translate to:",
            options=list(output_language_options.keys()),
            index=0,
            label_visibility="collapsed",
            key="output_lang"
        )

        st.session_state.translate_to = output_language_options[selected_output_language]

        st.markdown("""
        <p style='font-size: 0.85em; color: #667eea; margin-top: 10px;'>
            💡 Your voice will be translated automatically!
        </p>
        """, unsafe_allow_html=True)

    st.divider()

    # Add space before bottom section
    st.markdown("<br>" * 3, unsafe_allow_html=True)

    st.markdown("### 💡 About")

    st.info("""
    This is an AI chatbot powered by:
    - **Google Gemini API** (gemini-2.5-flash)
    - **Streamlit** for the interface

    Ask me anything and I'll do my best to help!
    """)

    st.divider()

    # Clear chat button at bottom
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
