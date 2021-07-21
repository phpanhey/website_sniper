# website sniper - i will watch state changes on your sites
this script watches if a specific snippet on a website changes and sends a notifiction via telegram.
e.g. stock of a ps5 in a online-store could be checked.


## usage
```sh
python3 website_sniper custom_config.json
```

## config
the script depends on a `config.json` where you specify the sites to be watched. you can specify your own configname. then configname has to be an argument of the script.

`title`, `url`,`search_snippet` must be specified. the script searches `search_snippet` on a website if it's not found you will be notifed. notification requires telegrams `bot_token` and `user_id`.

```json
{
    "watched_sites": [
        {
            "title": "ps5 mueller",
            "url": "https://www.mueller.de/multi-media/playstation-5/",
            "search_snippet": "nicht erhältlich"
        },
        {
            "title": "ps5 expert",
            "url": "https://ps5.expert.de/themenwelten/sony-ps5.html",
            "search_snippet": "bereits vergriffen"
        }
    ],
    "telegram": {
        "bot_token": "bot_token",
        "user_id": "user_id"
    }
}
```
## crontab
in order to watch periodically use crontab:
i.e. every 15 min:

```sh
*/15 * * * * cd ~/scripts/website_sniper; python3 website_sniper.py;cd 
```