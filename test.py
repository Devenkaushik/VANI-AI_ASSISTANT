import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from unittest.mock import patch
from project import get_website, gen_yt_vdo, write, is_key,get_website, add_website, open_webs, is_valid_url, gen_yt_vdo


websites = {
    "Google": "https://www.google.com",
    "YouTube": "https://www.youtube.com",
    "facebook" : "https://www.facebook.com"
}

@patch('pyautogui.write', return_value=None)
def test_write(mock_write):
    result = write("can you write Hello World")
    assert result == "You would write anything, even it is non-sence and you have written Hello World successfully as well"
    mock_write.assert_called_with("Hello World", interval=0.01)

    result = write("can you write")
    assert result == "user just said 'can you write' but what to write?"

def test_is_key():
    assert is_key("API_KEY=abcdefghijklmno1234567890pqrstuvwxyzABC") is True
    assert is_key("API_KEY=invalidkey123") is False
    assert is_key("INVALID_FORMAT") is False



def test_get_website():
    assert get_website("Google", websites) == "https://www.google.com"
    assert get_website("YouTube", websites) == "https://www.youtube.com"
    assert get_website("Bing", websites) == "'Bing' is not in the website list"
    assert get_website("nonexistent", websites) == "'nonexistent' is not in the website list"

def test_add_website():
    add_website("reddit","https://www.reddit.com",websites)
    assert "reddit" in websites
    assert websites["reddit"] == "https://www.reddit.com"
    assert add_website("somthing","https://www.ujbsehuiehuisn.com",websites) == "Error: 'https://www.ujbsehuiehuisn.com' is not accessible, Try to add another any url."
    assert add_website("reddit","https://www.reddit.com",websites) == "user tried to add 'reddit' to website list with link 'https://www.reddit.com' but it already exists"
    assert add_website("invalid","invalid.url",websites) == "Error: invalid URL, it must be in the format 'https:// [website domain name] / [if somthing else]'"


def test_is_valid_url():
    assert is_valid_url("https://www.google.com") is True
    assert is_valid_url("htp://invalid-url") is False
    assert is_valid_url("www.missing-scheme.com") is False

def test_gen_yt_vdo():
    assert gen_yt_vdo("search Python tutorials on youtube") == "https://www.youtube.com/results?search_query=Python+tutorials"
    assert gen_yt_vdo("search CS50p final project on youtube") == "https://www.youtube.com/results?search_query=CS50p+final+project"
    assert gen_yt_vdo("search python tutorials on youtube") == "https://www.youtube.com/results?search_query=python+tutorials"
    assert gen_yt_vdo("search on youtube") is False