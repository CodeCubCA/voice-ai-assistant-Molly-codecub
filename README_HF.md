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

## ✨ Features

- 🤖 **AI-Powered Conversations** - Leverages Google Gemini 2.5 Flash for intelligent discussions
- 🎤 **Voice Input** - Speak your questions instead of typing
  - Supports English, Chinese (Mandarin), Cantonese, and French
  - Automatic speech-to-text transcription
- 🔊 **Text-to-Speech Output** - Hear AI responses spoken aloud
  - Powered by AWS Polly with high-quality voices
  - Choose from multiple voices (Joanna, Matthew, Ivy, Salli, Joey, Kendra, Justin)
- 🌐 **Multilingual Translation** - Translate between 13+ languages
  - English, Chinese (Simplified/Traditional), Cantonese, French, Spanish, German, Japanese, Korean, Italian, Portuguese, Russian, Arabic, Hindi
- ⚡ **Real-Time Streaming** - Watch responses appear in real-time
- 🎨 **Modern UI** - Beautiful purple gradient theme with glassmorphism effects

## 🚀 Quick Start

1. **Configure Environment Variables** in the Hugging Face Space Settings:
   - `GEMINI_API_KEY` - Your Google Gemini API key ([Get it here](https://aistudio.google.com))
   - `AWS_ACCESS_KEY_ID` - AWS access key for Polly
   - `AWS_SECRET_ACCESS_KEY` - AWS secret key
   - `AWS_REGION` - Set to `ca-central-1`

2. **Start Using**:
   - Type or speak your questions
   - Enable translation to chat in multiple languages
   - Listen to AI responses with text-to-speech

## 🔑 Getting API Keys

### Google Gemini API
1. Visit [Google AI Studio](https://aistudio.google.com)
2. Sign in with your Google account
3. Generate an API key
4. Add to Space settings as `GEMINI_API_KEY`

### AWS Credentials (for Text-to-Speech)
1. Create an AWS account at [aws.amazon.com](https://aws.amazon.com)
2. Go to IAM Console → Create User
3. Attach the `AmazonPollyReadOnlyAccess` policy
4. Create access keys
5. Add to Space settings as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

## 🛠️ Technologies

- **Python 3.12+** - Programming language
- **Streamlit** - Web application framework
- **Google Gemini API** - AI model (gemini-2.5-flash)
- **AWS Polly** - Text-to-speech synthesis
- **SpeechRecognition** - Voice input processing
- **deep-translator** - Multilingual translation

## 📝 License

MIT License - See [LICENSE](LICENSE) for details

## 👩‍💻 Author

**Molly** - Student & Developer passionate about AI and creating interactive applications.

- GitHub: [CodeCubCA](https://github.com/CodeCubCA)
- Project Repository: [voice-ai-assistant-Molly-codecub](https://github.com/CodeCubCA/voice-ai-assistant-Molly-codecub)

---

**⭐ Star this Space if you find it helpful!**

Made with 💙 and 🤖 by Molly

*Talk to AI in any language!*