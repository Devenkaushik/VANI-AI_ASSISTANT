from colorama import Fore, Back, Style
import google.generativeai as genai
import speech_recognition as sr
from dotenv import load_dotenv
import pyautogui as auto
import google.api_core
import webbrowser
import threading
import requests
import pyttsx3
import time
import csv
import re
import os


def main():
    Vani_mode = mode()
    gemini = initialise_gemini()
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "\n# Wait for a while... Initializing Vani...\n Till then you can read 'Some basic Instructions and Usage' above"
        + Style.RESET_ALL
    )
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    extra_info = None
    global websites
    websites = get_website_DICT()
    args = (
        "initializing VANI...",
        gemini,
        "this is for initializing purposes, take as much time you wanna take here... but from now respond quickly",
    )
    thread = threading.Thread(target=ai, args=args)
    thread.start()
    while thread.is_alive():
        print("...V.A.N.I... is getting ready...")
        time.sleep(1)
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "\nVani is Now Initialized and Ready for help...\n"
        + Fore.GREEN
        + "###############################################\n"
        + Style.RESET_ALL
    )
    while True:
        print(
            Fore.CYAN
            + Style.NORMAL
            + "Vani is listing... (Only if you call her.)"
            + Style.RESET_ALL
        )
        if Vani_mode == "say":
            user_said = speech_r().lower()
        else:
            user_said = (
                input(Fore.GREEN + Style.BRIGHT + "type here: " + Style.RESET_ALL)
                .strip()
                .lower()
            )

        if user_said.startswith("vani "):
            print(
                Fore.BLUE
                + Style.BRIGHT
                + Back.WHITE
                + f"you: {user_said}"
                + Style.RESET_ALL
            )
            if "vani can you exit" in user_said:
                break
            elif "opening" in user_said or "open" in user_said:
                extra_info = open_webs(user_said)
            elif "search" in user_said in user_said:
                if link := gen_yt_vdo(user_said):
                    webbrowser.open(link)
                    extra_info = f"we have searched successfully on youtube."
                else:
                    extra_info = f"just say yes and tell them to {Vani_mode} 'search 'thing they want to seach' on youtube', if user asked, can you search on youtube? because you can... but not other website yet. on the other and if they ask for totaly different so tell them that..."
            elif "vani can you write" in user_said:
                extra_info = write(user_said)
            elif "vani can you change mode" in user_said:
                Vani_mode = mode()
                extra_info = f"Vani mode has been changed to {Vani_mode}, 'type' means chat interface where you don't speak and type your desired thing, Vani also repiles in chat and 'say' means where you speak and tell Vani what do you want to say and Vavi will also speak here."
            elif "vani can you add website" in user_said:
                print(
                    Fore.RED
                    + Style.BRIGHT
                    + "Note: If you don't want to add a website, enter 'exit' to exit anytime."
                    + Style.RESET_ALL
                )
                while True:
                    url = (
                        input(Fore.GREEN + "Input the URL: " + Style.RESET_ALL)
                        .strip()
                        .lower()
                    )
                    webs_name = (
                        input(Fore.GREEN + "Input website's name: " + Style.RESET_ALL)
                        .strip()
                        .lower()
                    )
                    if url == exit or webs_name == exit:
                        extra_info = "user wanted to add a website to list but exit in between and did't add any website to list."
                        break
                    extra_info = add_website(webs_name, url)
                    if extra_info.startswith("Error"):
                        print(Fore.RED + extra_info + Style.RESET_ALL)
                    else:
                        break

            print(Fore.CYAN + Style.BRIGHT + "Vani is Thinking..." + Style.RESET_ALL)
            if Vani_mode == "say":
                what_to_speak = ai(user_said, gemini, extra_info)
                try:
                    speak(engine, what_to_speak, Vani_mode)
                except Exception as e:
                    print(
                        Fore.RED
                        + f"\nSomething went wrong, Can't speak at the moment: for devs: error: {e}\n"
                        + Style.RESET_ALL
                    )
                print(
                    Fore.CYAN
                    + Style.BRIGHT
                    + Back.WHITE
                    + f"Vani: {what_to_speak}"
                    + Style.RESET_ALL
                )
            else:
                print(
                    Fore.CYAN
                    + Style.BRIGHT
                    + Back.WHITE
                    + f"Vani: {ai(user_said,gemini,extra_info)}"
                    + Style.RESET_ALL
                )
        else:
            print(
                Fore.CYAN
                + Style.DIM
                + f"\nDon't fotgot to {Vani_mode} 'Vani' at the start of your sentence\n"
                + Style.RESET_ALL
            )


def get_website(webs_name, websites):
    try:
        return websites[webs_name]

    except KeyError as e:
        return f"{e} is not in the website list"


def get_website_DICT():
    try:
        with open("websites.csv", newline="") as csvfile:
            websites = {row["Website"]: row["URL"] for row in csv.DictReader(csvfile)}
            if websites == {}:
                raise ValueError("The dictionary is empty!")
            else:
                pass
    except (FileNotFoundError, ValueError):
        with open("websites.csv", "w", newline="") as csvfile:
            fieldnames = ["Website", "URL"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"Website": "google", "URL": "https://www.google.com/"})
        with open("websites.csv", newline="") as csvfile:
            websites = {row["Website"]: row["URL"] for row in csv.DictReader(csvfile)}
    return websites


def open_webs(user_said):

    if searched := re.search(r"(?:open|opening) (\w+) ?", user_said):
        webapp = searched.group(1).lower()
    else:
        return "user just said 'open' or something... what to open?"
    get_webs = get_website(webapp, websites)
    if get_webs.endswith("is not in the website list"):
        return f"if user asked for a website to open name,{webapp} but {get_webs}, so tell them that you can't open this website for now but if user did't ask for any website then answer them what they have asked for."
    else:
        webbrowser.open(get_webs)
        return (
            f"User asked for a website to open {webapp}, and It is opening successfully"
        )


def is_valid_url(url):
    pattern = re.compile(
        r"^(https?:\/\/)"
        r"(www\.)?"
        r"[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}"
        r"(\/[a-zA-Z0-9\-._~:\/?#[\]@!$&\'()*+,;%=]*)?$",
        re.IGNORECASE,
    )
    return re.match(pattern, url) is not None


def is_website_accessible(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False


def add_website(name, url, websites):
    if not is_valid_url(url):
        return "Error: invalid URL, it must be in the format 'https:// [website domain name] / [if somthing else]'"
    if not is_website_accessible(url):
        return f"Error: '{url}' is not accessible, Try to add another any url."
    if name in websites:
        return f"user tried to add '{name}' to website list with link '{url}' but it already exists"
    with open("websites.csv", "a", newline="") as csvfile:
        fieldnames = ["Website", "URL"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Website": name, "URL": url})
        websites[name] = url
    return f"user tried to add '{name}' to website list with link '{url}' and it added successfully"


def gen_yt_vdo(yt_search):
    if searched := re.search(r"search (.+) on youtube", yt_search):
        yt_search = searched.group(1)
        yt_search = yt_search.strip().replace(" ", "+")
        return f"https://www.youtube.com/results?search_query={yt_search}"
    else:
        return False


def write(user_said):
    if searched := re.search(r"can you write (.+)", user_said):
        write = searched.group(1)
        auto.write(write, interval=0.01)
        return f"You would write anything, even it is non-sence and you have written {write} successfully as well"
    else:
        return "user just said 'can you write' but what to write?"


def check_key():
    try:
        with open(".env", "r") as k:  # Open the .env file in read mode
            keys = k.read().strip()  # Read and remove extra spaces or lines
    except FileNotFoundError:
        print("\n.env file not found! Don't worry, just making one for you :)")
        setup_key()  # Call setup_key to create and configure the file
    else:
        if is_key(keys):  # Validate the content of the .env file
            pass  # Valid key, do nothing
        else:
            print("You have an invalid key!!! or You don't have a key in .env")
            setup_key()  # Prompt the user for a valid key



def is_key(key):
    return True if re.match("^API_KEY=[a-zA-Z0-9]{39}$", key) else False


def setup_key():
    with open(".env", "w") as k:
        print(
            Fore.BLACK
            + Back.GREEN
            + "\nGet an API key From here: https://ai.google.dev/"
            + Style.RESET_ALL
        )
        while True:
            # Prompt user for the key
            key = input(
                Fore.GREEN + "\nPaste your Gemini API key here: " + Style.RESET_ALL
            ).strip()
            if not is_key(f"API_KEY={key}"):  # Validate the input
                print(Fore.RED + "\nError: Invalid key, try again." + Style.RESET_ALL)
            else:
                break  # Break the loop if the key is valid
        # Save the valid key to the .env file
        k.write(f"API_KEY={key}")


def initialise_gemini():
    check_key()
    load_dotenv()
    genai.configure(api_key=os.getenv("API_KEY"))

    model = genai.GenerativeModel("gemini-1.5-flash-8b")

    gemini = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": """you are a 'Vani' a personal assistance, don't give too long response until asked or specified by the user but you should give if user asked for, and There are some functions that I have implimented in your code.
                you will be provied with 'user_said: [what user realy said], 'extra_info': [if any function ran if would give you some info that might be helpfull while reponding to user]
                you have two mode fisrt 'TYPE' mode other one is 'SAY' mode, more on this later when we choose one of the mode but modes can be change if user said exactly 'vani can you change mode' then it will trigger change mode function.
                you have move function like :-
                Add a Website , you have a website list, so can only access them, this function will add website to that list:
                usage: "vani can you add website" and it will trigger the function and will proved vani some extra_info too.
                Open Website, this will open website from website list:
                eg: "Open YouTube"
                usage: "Open [name of website]" and it will trigger the function and will proved vani some extra_info too.
                Search on YouTube, it will search on youtube:
                usage: "Search [keywords] on YouTube" and it will trigger the function and will proved vani some extra_info too.
                Write Text, it will write anything what user said on screen:
                usage: "vani can you write [specific text]?" and it will trigger the function and will proved vani some extra_info too.
                and vani can be quit if user said 'vani can you exit' """,
            },
            {
                "role": "model",
                "parts": "Great to meet you, I will resond like 'Vani' from now. What would you like to know?",
            },
        ]
    )
    return gemini


def add_new_line(text, words_in_line=15):
    n = 0
    resp = []
    words = ""
    for word in text.split(" "):
        words += word + " "
        n += 1
        if n == words_in_line:
            resp.append(words + "\n")
            n = 0
            words = ""
    resp.append(words + "\n")
    final_text = ""
    for line in resp:
        final_text += "      " + line
    return final_text.strip()


def ai(here, gemini, extra_info="nothing for now"):
    try:
        response = gemini.send_message(
            f"user_said: {here}, additional data: {extra_info}"
        )
        return add_new_line(response.text, 20)
    except google.api_core.exceptions.InvalidArgument:
        print("API key is not valid. Please pass a valid API key")
        setup_key()


def speak(engine, what_to_speak, Vani_mode):
    if Vani_mode == "say":
        engine.say(what_to_speak)
        engine.runAndWait()
    else:
        pass


def speech_r():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                audio = r.listen(source, phrase_time_limit=20)
                return r.recognize_google(audio)
            except Exception:
                pass


def mode():
    while True:
        print(
            Fore.GREEN
            + """\nIf you preffer to speak and listen, enter '1'
If you preffer to type and read, enter '2'
(You can change it later by asking "Vani can change mode")"""
        )
        try:
            set_mode = int(input("What do you preffer? (1/2): " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Error: Invalid Value Try Again" + Style.RESET_ALL)
        else:
            if set_mode == 1:
                return "say"
            elif set_mode == 2:
                return "type"
            else:
                print(Fore.RED + "Error: Invalid Value Try Again" + Style.RESET_ALL)


if __name__ == "__main__":
    print(
        Fore.CYAN
        + Style.BRIGHT
        + """
                                                            iiii
                                                           i::::i
                                                            iiii

vvvvvvv           vvvvvvvaaaaaaaaaaaaa  nnnn  nnnnnnnn    iiiiiii
 v:::::v         v:::::v a::::::::::::a n:::nn::::::::nn  i:::::i
  v:::::v       v:::::v  aaaaaaaaa:::::an::::::::::::::nn  i::::i
   v:::::v     v:::::v            a::::ann:::::::::::::::n i::::i
    v:::::v   v:::::v      aaaaaaa:::::a  n:::::nnnn:::::n i::::i
     v:::::v v:::::v     aa::::::::::::a  n::::n    n::::n i::::i
      v:::::v:::::v     a::::aaaa::::::a  n::::n    n::::n i::::i
       v:::::::::v     a::::a    a:::::a  n::::n    n::::n i::::i
        v:::::::v      a::::a    a:::::a  n::::n    n::::ni::::::i
         v:::::v       a:::::aaaa::::::a  n::::n    n::::ni::::::i
          v:::v         a::::::::::aa:::a n::::n    n::::ni::::::i
           vvv           aaaaaaaaaa  aaaa nnnnnn    nnnnnniiiiiiii

                                        -Your own personal Assistant
"""
        + Style.RESET_ALL
    )

    print(
        Fore.CYAN
        + Style.NORMAL
        + """
# Some basic Instructions and Usage(type or say):

# 1.  Vani is your personal assistant designed to make your tasks easier.
# 2.  You can ask Vani to open popular websites (Usage: "vani open Google", "vani open YouTube").
# 3.  Vani can add new websites to its database for future use (Usage: "vani can you add website").
# 4.  Vani supports typing and speech-based interactions; you can choose your preferred mode during initialization.
      and you can change mode later by (Usage: "vani can you change mode")
# 5.  Vani is integrated with the Gemini AI model for enhanced responses.
# 6.  Vani can interact with and respond to your voice commands using speech recognition.
# 7.  Note: Ensure your .env file contains a valid API key for the AI to function correctly.
# 8.  Use Vani to perform actions writing text seamlessly (Usage: "vani can you write [what to write]").
# 9.  You can search directly to Youtube (Usage: "Vani search [what to search] on Youtube")
# 10. you can exit anytime from vani (usage: "vani can you exit" )
# 11. Last but not the least Don't fotgot to type or say 'Vani' at the start of your sentence else she will not respond
# 12. If Some kind of unexpected error occurred, please share this to the developer.
"""
        + Style.RESET_ALL
    )
    try:
        main()
    except EOFError:
        print("exited vani")
   
    except Exception as e:
        print(
        Back.BLACK
        + "Some kind of unexpected error occurred, please share this to the developer, log:\n"
        + str(e)
    )

