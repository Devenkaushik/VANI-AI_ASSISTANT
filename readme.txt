####                                                             iiii
####                                                            i::::i
####                                                             iiii
####
#### vvvvvvv           vvvvvvvaaaaaaaaaaaaa  nnnn  nnnnnnnn    iiiiiii
####  v:::::v         v:::::v a::::::::::::a n:::nn::::::::nn  i:::::i
####   v:::::v       v:::::v  aaaaaaaaa:::::an::::::::::::::nn  i::::i
####    v:::::v     v:::::v            a::::ann:::::::::::::::n i::::i
####     v:::::v   v:::::v      aaaaaaa:::::a  n:::::nnnn:::::n i::::i
####      v:::::v v:::::v     aa::::::::::::a  n::::n    n::::n i::::i
####       v:::::v:::::v     a::::aaaa::::::a  n::::n    n::::n i::::i
####        v:::::::::v     a::::a    a:::::a  n::::n    n::::n i::::i
####         v:::::::v      a::::a    a:::::a  n::::n    n::::ni::::::i
####          v:::::v       a:::::aaaa::::::a  n::::n    n::::ni::::::i
####           v:::v         a::::::::::aa:::a n::::n    n::::ni::::::i
####            vvv           aaaaaaaaaa  aaaa nnnnnn    nnnnnniiiiiiii
####
####                                         -Your own personal Assistant


#### Video Demo:  https://youtu.be/Jw4GI6R_o-o?si=GgZhNYenJ36uPOSm

## **Overview**
Vani is a virtual AI assistant capable of responding to user commands, performing tasks like opening websites, searching content, generating AI responses, and interacting via text or speech.

---

## **How It Works**
The assistant operates in two modes:
1. **"say"**: Voice-based interaction (requires microphone input).
2. **"type"**: Text-based interaction.

The user can give commands by prefixing their input with **`vani`**.

---

## **Main Features**
- **Voice/Text Interaction**: Users can interact with Vani using speech or text input.
- **Web Handling**:
  - Open pre-saved or user-defined websites.
  - Add new websites to Vani's dictionary.
- **YouTube Search**: Generate a YouTube search link based on queries.
- **AI-Powered Responses**: Leverages Gemini AI for generating contextual replies.
- **Custom Writing**: Handles content generation tasks upon request.
- **Dynamic Mode Switching**: Switch between "say" (speech) and "type" (text) modes during interaction.
- **Threaded Initialization**: Ensures smooth startup without blocking the main program.

---

## **Dependencies**
- `pyttsx3` (Text-to-Speech)
- `colorama` (Terminal text styling)
- `speech recognition` (Voice input)
- Threading (Async Initialization)
- Custom Functions:
  - `mode()`: Sets communication mode.
  - `initialise_gemini()`: Initializes Gemini AI.
  - `ai()`: Processes user input and generates responses.
  - `open_webs()`: Opens user-requested websites.
  - `gen_yt_vdo()`: Generates YouTube search links.
  - `write()`: writing functionality.
  - `add_website()`: Adds websites to Vani's dictionary.
  - `speech_r()`: Captures voice input.

---

## **How to Run**
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Script**:
   ```bash
   python project.py
   ```
3. **Follow Prompts**:
   - Choose the communication mode (**say/type**).
   - Start commands with **`vani`**.

---

## **Commands**
| Command                         | Description                                           |
|---------------------------------|-------------------------------------------------------|
| `vani can you exit`             | Exits the program.                                    |
| `vani open [website]`           | Opens a specific website.                             |
| `vani search [query]`           | Searches for the query on YouTube.                    |
| `vani can you write`            | Handles content writing tasks.                        |
| `vani can you change mode`      | Switches between **say** and **type** modes.          |
| `vani can you add website`      | Adds a new website to Vani's saved dictionary.        |

---

#### **Files and Their Functionality**
1. *Core Script* : project.py
- # Code Walkthrough of `project.py`:

The main logic resides in the `main()` function, which works as follows:

1. **Mode Selection**:
   - Calls `mode()` to decide between "say" or "type" modes.
2. **AI Initialization**:
   - Starts a separate thread for Gemini AI initialization using `threading.Thread()`.
3. **Input Handling**:
   - **"say" mode**: Captures voice input using `speech_r()`.
   - **"type" mode**: Takes user input from the terminal.
4. **Command Execution**:
   - Opens websites, searches on YouTube, handles writing tasks, or switches modes.
5. **AI Response**:
   - Processes user input via `ai()` and responds through text or speech (`pyttsx3`).
6. **Graceful Exit**: Program ends when the user says **`vani can you exit`**.

2. *Data File* : websites.csv

**Purpose**:
- Stores website names and their corresponding URLs.
**Functions**:
- Read and update website entries dynamically.
- Interacts with the core script to ensure seamless website management.

3. *Environment File*: .env

**Purpose**:
- Securely stores API keys for the Google Generative AI integration.
**Functionality**:
- Externalizes sensitive information for better security and maintainability.

---

## **Error Handling**
- Handles missing or invalid inputs gracefully.
- Catches exceptions during text-to-speech processing.
- Reminds users to prefix inputs with **`vani`** for valid commands.

---

## **Example Usage**
```text
> Vani: Hello! How can I assist you today?
> User: vani open Google
> Vani: Opening Google...
> User: vani can you search Python tutorials on youtube
> Vani: Searching YouTube for 'Python tutorials'.
> User: vani can you exit
> Vani: Goodbye!
```

---

## **Known Limitations**
- Voice recognition may fail in noisy environments.
- AI responses depend on the quality of the Gemini AI API.
- Requires a stable internet connection.
---