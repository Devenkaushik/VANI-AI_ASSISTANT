# VANI - Your AI Assistant

Welcome to **Vani**, your personalized AI assistant! Use **voice** or **text** to interact seamlessly, get tasks done quickly, and make your daily life easier.

## 🚀 Key Features

- **Dual Modes**: Communicate through voice or text.
- **Web Actions**: Open saved websites or add new ones to your directory.
- **YouTube Searches**: Generate direct search links for any topic.
- **AI Responses**: Smart and contextual replies with Gemini AI.
- **Custom Writing**: Generate personalized content with ease.
- **Easy Switching**: Change between voice and text modes anytime.
- **Smooth Operation**: Multi-threaded setup for quick, uninterrupted tasks.

---

## 🛠️ How to Set Up

### 1️⃣ Prerequisites

- **Python 3.6 or higher**
- **pip** (Python package installer)

### 2️⃣ Install and Run

Clone this repository:

```bash
git clone https://github.com/Devenkaushik/VANI-AI_ASSISTANT.git
cd VANI-AI_ASSISTANT
```

Install all required libraries:

```bash
pip install -r requirements.txt
```

Launch Vani:

```bash
python project.py
```

Follow the on-screen instructions to choose a mode: **voice (say)** or **text (type)**.

---

## 💬 How to Use

All commands start with the prefix **vani**.
Choose between **voice or text** to interact.

| Command | What It Does |
|---------|-------------|
| `vani open [website]` | Opens the specified website. |
| `vani search [query]` | Searches YouTube for the given query. |
| `vani can you add website` | Adds a website to Vani's saved list. |
| `vani can you write` | Helps with custom writing tasks. |
| `vani can you change mode` | Switches between voice and text input modes. |
| `vani can you exit` | Exits the assistant. |

---

## 📂 Files in This Project

### **Core Files:**

- `project.py`: The main file where all the logic is implemented.
- `websites.csv`: Stores website names and URLs for dynamic access.
- `.env`: Keeps sensitive information like API keys secure.

### **Main Functions:**

- `mode()`: Lets you choose between text or voice input.
- `initialise_gemini()`: Sets up AI response capabilities.
- `ai()`: Processes your input and generates helpful responses.
- `open_webs()`: Opens user-specified websites.
- `gen_yt_vdo()`: Creates YouTube search links for your queries.
- `add_website()`: Adds new websites to the list.
- `speech_r()`: Captures and interprets voice commands.

---

## ⚙️ How Vani Works

1. Choose the mode: **say (voice)** or **type (keyboard)**.
2. Use the **vani** prefix to start your commands.
3. Vani performs tasks such as **opening websites, generating search results, or responding with AI-generated text**.
4. Exit anytime by saying or typing **vani can you exit**.

---

## 🛡️ Error Handling

- Friendly prompts for invalid input.
- Recovers smoothly from **network or API issues**.
- Reminders to start commands with the **vani prefix** for accurate results.

---

## 🌟 Example Conversation

```
Vani: Hello! How can I help you today?
User: vani open Google
Vani: Opening Google...
User: vani search "Python tutorials on YouTube"
Vani: Searching YouTube for 'Python tutorials'...
User: vani can you exit
Vani: Goodbye! Have a great day!
```

---

## 🚧 Known Limitations

- **Voice recognition** might not work perfectly in noisy areas.
- **AI responses** depend on your internet connection.
- You may need to refine your commands for specific use cases.

---

## 🎉 Start Exploring Vani Today

Vani is here to simplify your daily tasks. **Download, set up, and start using your own intelligent assistant!**

