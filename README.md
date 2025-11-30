---
title: AI Chatbot - Multilingual Voice Assistant
emoji: 🤖
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: "1.31.0"
app_file: app.py
pinned: false
license: mit
---

# 🤖 AI Chatbot - Multilingual Voice-Enabled Assistant

Your personal AI-powered assistant with voice input, text-to-speech output, and multilingual translation capabilities!

---

## 📖 About

The **AI Chatbot** is an intelligent conversational assistant powered by Google's Gemini 2.5 Flash model. It features voice input with speech recognition, text-to-speech output powered by AWS Polly, real-time translation across 13+ languages, and a beautiful modern purple gradient interface. Whether you need help with questions, creative tasks, or just want to chat in your native language, this AI assistant has you covered!

---

## ✨ Features

- 🤖 **AI-Powered Conversations** - Leverages Google Gemini 2.5 Flash for intelligent, context-aware discussions
- 🎤 **Voice Input** - Speak your questions instead of typing
  - Click the microphone button to record
  - Supports English, Chinese (Mandarin), Cantonese, and French
  - Automatic speech-to-text transcription
- 🔊 **Text-to-Speech Output** - Hear AI responses spoken aloud
  - Powered by AWS Polly with high-quality voices
  - Choose from multiple voices (Joanna, Matthew, Ivy, Salli, Joey, Kendra, Justin)
  - Audio player for each AI response
- 🌐 **Multilingual Translation** - Translate between 13+ languages
  - Speak in one language, translate to another
  - Supported languages: English, Chinese (Simplified/Traditional), French, Spanish, German, Japanese, Korean, Italian, Portuguese, Russian, Arabic, Hindi
  - Toggle translation on/off with a button
- 💬 **Text & Voice Input** - Choose between typing or speaking
- ⚡ **Real-Time Streaming** - Watch responses appear in real-time
- 💬 **Chat History** - Maintains conversation context throughout your session
- 🎨 **Modern UI** - Beautiful purple gradient theme with glassmorphism effects
  - Animated robot mascot
  - Smooth transitions and floating animations
  - Clean, intuitive interface
- 📊 **Message Counter** - Track your conversation length
- 🔄 **Easy Reset** - Clear chat history anytime to start fresh

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_Polly-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)

- **Python 3.12+** - Programming language
- **Streamlit** - Web application framework for rapid UI development
- **Google Gemini API** - Advanced AI model (gemini-2.5-flash)
- **AWS Polly** - Text-to-speech synthesis with natural voices
- **boto3** - AWS SDK for Python
- **SpeechRecognition** - Voice input processing
- **deep-translator** - Multilingual translation
- **audio-recorder-streamlit** - Audio recording component
- **python-dotenv** - Environment variable management

---

## 🌐 Live Deployments

This AI Chatbot is deployed on multiple platforms for easy access:

- **Hugging Face Spaces**: [https://huggingface.co/spaces/mollycodecub/voice-ai-assistant](https://huggingface.co/spaces/mollycodecub/voice-ai-assistant)
  - Easy one-click deployment
  - Free hosting for AI/ML applications
  - Integrated with Streamlit

- **Render**: Coming soon!
  - Production-ready deployment
  - Custom domain support
  - Automatic HTTPS

Try the live demo on Hugging Face Spaces - no installation required!

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.12 or higher
- Google Gemini API key (free tier available)
- AWS account with Polly access (for text-to-speech)
- Git installed on your computer
- Microphone (for voice input feature)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/CodeCubCA/ai-chatbox-Molly-codecub.git
   cd ai-chatbox-Molly-codecub
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```bash
   touch .env
   ```

   Add your API keys to the `.env` file:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   AWS_ACCESS_KEY_ID=your_aws_access_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret_key
   AWS_REGION=ca-central-1
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in your terminal

---

## 🎤 Using Voice Input

1. **Select your speaking language** in the sidebar (English, Chinese, Cantonese, or French)
2. **Optional: Enable translation**
   - Click the "🌐 Enable Translation" button
   - Choose your target language from the dropdown
3. **Click the microphone button** in the main area
4. **Speak your message** clearly
5. **Click again to stop recording**
6. Your speech will be transcribed and (if enabled) translated automatically!

**Browser Permissions:** Make sure to allow microphone access when prompted by your browser.

---

## 🌐 Translation Features

- **Speak in:** English, Chinese (Mandarin), Cantonese, French
- **Translate to:** English, Chinese (Simplified/Traditional), French, Spanish, German, Japanese, Korean, Italian, Portuguese, Russian, Arabic, Hindi

**Example Use Case:**
- Speak in Chinese → Translate to Spanish → AI responds in Spanish
- Speak in French → Translate to English → AI responds in English

---

## 🔑 API Key Setup

### How to Get Your Google Gemini API Key

1. **Visit Google AI Studio**
   - Go to [aistudio.google.com](https://aistudio.google.com)

2. **Create an account or sign in**
   - Use your Google account

3. **Generate API Key**
   - Click "Get API Key"
   - Create a new API key
   - Copy your key (save it securely!)

4. **Add to your project**
   - Paste the key in your `.env` file:
     ```env
     GEMINI_API_KEY=your_api_key_here
     ```

### How to Get Your AWS Credentials (for Text-to-Speech)

1. **Create an AWS Account**
   - Go to [aws.amazon.com](https://aws.amazon.com) and sign up

2. **Create IAM User with Polly Access**
   - Go to IAM Console → Users → Create User
   - Attach the `AmazonPollyReadOnlyAccess` policy
   - Create access keys for the user

3. **Add AWS credentials to your `.env` file**
   ```env
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   AWS_REGION=ca-central-1
   ```

**Note:** Keep your API keys secret! Never commit them to GitHub.

---

## 📦 Project Structure

```
ai-chatbox/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API key)
├── .env.example               # Template for .env file
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
└── .streamlit/
    └── config.toml            # Streamlit configuration
```

---

## 🎨 Features Showcase

### Voice Input
- 🎤 Click-to-record microphone button
- 🔊 Real-time audio transcription
- 🌐 Multi-language speech recognition

### Translation
- 🌍 13+ supported languages
- ⚡ Real-time translation
- 🔄 Toggle on/off as needed

### Modern UI
- 💜 Purple gradient background
- ✨ Glassmorphism effects
- 🤖 Animated robot mascot
- 📱 Responsive design

---

## 🚧 Future Improvements

- [x] 🔊 Text-to-speech for AI responses (AWS Polly)
- [ ] 🎨 Additional theme options (light mode, custom colors)
- [ ] 📱 Mobile app version
- [ ] 💾 Save and export chat history
- [ ] 🎯 Specialized AI personalities
- [ ] 📊 Conversation analytics
- [ ] 🔒 User authentication
- [ ] 🌍 Expanded language support (50+ languages)
- [ ] 🔊 Multi-language TTS support

---

## 👩‍💻 Author

**Molly**

Student & Developer passionate about AI and creating interactive applications.

- 🤖 **AI Enthusiast** - Exploring LLMs and creative AI applications
- 💡 **Tech Stack:** Python, Streamlit, AI/ML, Web Development
- 🌟 **GitHub:** [CodeCubCA](https://github.com/CodeCubCA)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

- **Google** - For the powerful Gemini API
- **Streamlit** - For the amazing web framework
- **Open Source Community** - For the excellent libraries and tools

---

## 💡 Tips for Best Experience

1. **Use a good microphone** - Clear audio = better transcription
2. **Speak clearly** - Especially when using non-English languages
3. **Choose the right language** - Match your speaking language in the dropdown
4. **Try translation** - Experience multilingual conversations
5. **Refresh chat** - Use "Clear Chat History" for fresh conversations

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with 💙 and 🤖 by Molly

*Talk to AI in any language!*

</div>
