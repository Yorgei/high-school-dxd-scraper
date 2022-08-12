# high-school-dxd-scraper

## Things to remember

1. They will occasionally upload the /C/ cards up to 3 days before an event starts. Whenever they upload the event main image /C/ assets will be uploaded too.
2. They will NEVER release cards early in the gacha lineup page, it's all server side stuff so it's gg
3. Don't be a cunt and practically ddos them by spamming requests, there's no rate limit on the CDN but don't be a cunt.
4. Use sessions if you're going to use python, look at my examples.

## **Getting Card IDs the dumb way**

Every card's first evolution has a small image like this, so you can just bruteforce until you get working results. If you really want you can just try every combo from 1000-531000000 lol. I never got rate limited while scraping these so have fun

`http://cdn-prod.highschooldd.net/sp/image/cards/C/{card_number}.png`


## **Getting the card name and url**

Each card, including all evolutions can be viewed in the gacha details page but you need to remove the "gacha_details" param. You need to be logged in for this though so you'll need someway to get your mbga cookie. Mobage used to limit you to 1 request at a time, not sure if it still does or if gree/d do the same thing.

`https://g12014827.sp.pf.mbga.jp/?url=http%3A%2F%2Fmg.highschooldd.net%2Fsp%2Fgacha_card_detail%3Fcard_id%3D{card_number}%26lineup%3Dnormal`

I just got the url from using the xpath "'/html/body/div[2]/img/@src'"

## **How Card IDs work**

The way the card IDs work since event 200 seem to be the same so this should still work, but anything before 200 is a bit of a mess.

Example ID: 530201121

This gets broken down in to;

` 530 2 01 12 1`
- Event ID: 530 - Self explanatory. Last number in the ID indicates the type of event.
- Card Type: 2 - This indicates how the card is obtained, e.g Monthly W card, daily login reward or gacha
- Card Number: 01 - Number in the set, but doesn't always increment by 1. 
- Rarity: 12 - Self explanatory, 1-12
- Evolution: 1 - Self explanatory, 1-5?6?

Knowing how the Card IDs work should help limit the amount of bruteforcing you need to do. 

You CAN predict all of the card IDs since they don't usually change between variants of the events, but sometimes they will add more cards so I just decided to always scrape all the cards. Doing it this way from event 200~ to the 530 (latest) will take a LONG time (around 500k+ iterations). They very rarely add cards under rarity 5 which cuts it down by a lot. Events ending in 4/8 usually NEVER have new cards so you can decide if you want to scrape those.

If a card ends in _mobage.jpg or whatever that means it's been "updated" or "censored" but removing the _mobage in the url should still direct to the original version.


## Example

1. http://cdn-prod.highschooldd.net/sp/image/cards/C/530201121.png

1. https://g12014827.sp.pf.mbga.jp/?url=http%3A%2F%2Fmg.highschooldd.net%2Fsp%2Fgacha_card_detail%3Fcard_id%3D530201121%26lineup%3Dnormal

1. http://cdn-prod.highschooldd.net/sp/image/cards/L3/530201121_W4Q8hjqBX6.jpg
