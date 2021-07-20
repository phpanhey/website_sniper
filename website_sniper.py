import requests
import argparse
import json


def get_credentials(fieldname):
    return json.loads(open(get_config_name(), "r").read())[fieldname]


def get_config_name():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_name", nargs="?")
    config_name = parser.parse_args().config_name
    if not config_name:
        config_name = "config.json"
    return config_name


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5",
    }
    return requests.get(url, headers=headers).text


def send_telegram(message):
    request_string = (
        "https://api.telegram.org/bot"
        + get_credentials("telegram")["bot_token"]
        + "/sendMessage?chat_id="
        + get_credentials("telegram")["user_id"]
        + "&parse_mode=Markdown&text="
        + message
    )
    response = requests.get(request_string)
    return response.json()


sites = get_credentials("sites")
for site in sites:
    html = get_html(site["url"])
    if site["search_snippet"] not in html:
        message = f"👁  state {site['title']} changed: {site['url']}"
        send_telegram(message)