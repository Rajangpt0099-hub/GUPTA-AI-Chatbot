# 🤖 GUPTA AI Chatbot

An interactive AI-powered chatbot built using **Python, Streamlit, and Google Gemini API**. GUPTA AI Chatbot provides an easy-to-use conversational interface where users can interact with AI, ask questions, and upload different types of files for AI-powered analysis.

## 🚀 Project Overview

GUPTA AI Chatbot is a Generative AI application designed to make AI interaction simple, accessible, and user-friendly. It integrates Google's Gemini API with Streamlit to deliver intelligent responses through a clean and interactive interface.

The application supports text-based conversations along with file uploads, allowing users to interact with AI using different types of content.

## ✨ Key Features

- 💬 **AI-Powered Conversations:** Get intelligent responses using Google Gemini API.
- 🖼️ **Image Upload:** Upload images and ask questions about their content.
- 🎙️ **Audio Support:** Upload audio files for AI-based interaction and analysis.
- 📄 **Document Upload:** Upload supported documents and extract information.
- 📊 **CSV Support:** Work with CSV data and ask questions about its contents.
- 🧠 **Chat History:** Maintain conversation context during interactions.
- 🎨 **Interactive UI:** User-friendly Streamlit interface with a customized design.
- ⚡ **Real-Time Responses:** Get AI-generated answers to your prompts.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Google Gemini API | AI-powered response generation |
| Pandas | Data handling and CSV processing |
| Pillow (PIL) | Image processing |
| PyPDF2 | PDF text extraction |
| Python-docx | Word document processing |

## 📂 Project Structure

```text
GUPTA-AI-Chatbot/
│
├── KumarChatbot.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml
```

*Adjust the filenames above if your actual repository uses different names.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rajangpt0099-hub/GUPTA-AI-Chatbot.git
```

### 2. Open the Project Folder

```bash
cd GUPTA-AI-Chatbot
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Create a `.streamlit/secrets.toml` file and add your Google Gemini API key:

```toml
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"
```

Keep your API key private. Never upload `secrets.toml` to GitHub.

### 5. Run the Application

```bash
streamlit run KumarChatbot.py
```

The application will open in your browser.

## 🔑 API Configuration

This project uses the Google Gemini API to generate AI responses.

Get your API key from:

https://aistudio.google.com/apikey

Add the key to your Streamlit secrets before running the application.

## 🎯 Project Objectives

- Build an interactive chatbot using Generative AI.
- Integrate Google Gemini API with Python.
- Enable users to interact with AI through multiple input formats.
- Develop a simple and user-friendly web interface.
- Explore practical applications of multimodal AI.

## 🔮 Future Improvements

- Add voice-based conversations.
- Improve document understanding and summarization.
- Introduce chat export functionality.
- Add support for additional file formats.
- Deploy the application for public access.
<img width="1882" height="977" alt="image" src="https://github.com/user-attachments/assets/5ee11380-8afd-4d02-b44e-319c1031c279" />

## 👨‍💻 Author

**Rajan Gupta**

GitHub: https://github.com/Rajangpt0099-hub

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback!

**Built with Python, Streamlit, and Google Gemini AI.**
