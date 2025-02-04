VANI - YOUR AI ASSISTANT

Welcome to Vani, your personalized AI assistant! Use voice or text to interact seamlessly, get tasks done quickly, and make your daily life easier.
KEY FEATURES

    Dual Modes: Communicate through voice or text.

    Web Actions: Open saved websites or add new ones to your directory.

    YouTube Searches: Generate direct search links for any topic.

    AI Responses: Smart and contextual replies with Gemini AI.

    Custom Writing: Generate personalized content with ease.

    Easy Switching: Change between voice and text modes anytime.

    Smooth Operation: Multi-threaded setup for quick, uninterrupted tasks.

HOW TO SET UP
PREREQUISITES

    Python 3.6 or higher

    pip (Python package installer)

INSTALL AND RUN

    Clone this repository:
    Copy

    git clone https://github.com/Devenkaushik/VANI-AI_ASSISTANT.git  
    cd VANI-AI_ASSISTANT  

    Install required libraries:
    Copy

    pip install -r requirements.txt  

    Launch Vani:
    Copy

    python project.py  

Follow on-screen instructions to choose a mode: voice (say) or text (type).
HOW TO USE

All commands start with the prefix vani. Choose between voice or text to interact.

COMMAND EXAMPLES:

    Command: vani open [website]
    Action: Opens the specified website.

    Command: vani search [query]
    Action: Searches YouTube for the query.

    Command: vani can you add website
    Action: Adds a website to Vani's saved list.

    Command: vani can you write
    Action: Helps with custom writing tasks.

    Command: vani can you change mode
    Action: Switches between voice and text modes.

    Command: vani can you exit
    Action: Exits the assistant.

FILES IN THIS PROJECT

CORE FILES:

    project.py: Main file with all logic.

    websites.csv: Stores website names and URLs.

    .env: Secures sensitive data like API keys.

MAIN FUNCTIONS:

    mode(): Lets you choose input mode (text/voice).

    initialise_gemini(): Sets up AI response capabilities.

    ai(): Processes input and generates responses.

    open_webs(): Opens specified websites.

    gen_yt_vdo(): Creates YouTube search links.

    add_website(): Adds new websites to the list.

    speech_r(): Captures voice commands.

HOW VANI WORKS

    Choose voice or text mode.

    Start commands with vani.

    Vani performs tasks like opening websites, generating search results, or providing AI responses.

    Exit anytime with vani can you exit.

ERROR HANDLING

    Friendly prompts for invalid input.

    Smooth recovery from network/API issues.

    Reminders to use the vani prefix.

EXAMPLE CONVERSATION

Vani: Hello! How can I help you today?
User: vani open Google
Vani: Opening Google...
User: vani search "Python tutorials on YouTube"
Vani: Searching YouTube for 'Python tutorials'...
User: vani can you exit
Vani: Goodbye! Have a great day!
KNOWN LIMITATIONS

    Voice recognition may struggle in noisy environments.

    AI responses require an internet connection.

    Commands may need refinement for specific use cases.

START EXPLORING VANI TODAY

Vani simplifies daily tasks. Download, set up, and start using your intelligent assistant!