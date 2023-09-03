import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.RequestException:
        pass

target_input = "google.com"
with open("wordlist.txt", "r") as word_list:
    for word in word_list:
        word = word.strip()
        url = "https://" + word + "." + target_input
        response = make_request(url)
        if response:
            print("Found sundomain ---> " + url)

