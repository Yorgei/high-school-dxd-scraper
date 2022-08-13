# Scraping Cards

## How To

First set the params in `get_base_ids.py` to scrape the IDs you want. This is a lot faster than doing it in game so it's recommended if you're going to go this route.

After running it should output a `dump.json` file with a list of the URLs it found. These are NOT all the cards, only the first evolution of them. Configure `cookies.json` and then run `get_gacha.py`. You are only allowed one requst at a time in the game from what I've tested, so async/multithreading is useless here. It's going to be slow.




### Cookies
There are only two required cookies:
1. sp_mbga_sid_12014827
2. x-mbga-check-cookie

Accounts will usually have a `PRE` cookie but it is not required. Same with a `G` cookie.

In `cookies.json` set the `cookie` field to whatever your cookie is.

### 