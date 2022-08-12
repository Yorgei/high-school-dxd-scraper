import asyncio
import aiohttp
import json

# Change this to how ever many requests you want to send at a time, don't be a cunt and send a bajillion
sem = asyncio.Semaphore(64)
urls = []

# Change the event_id range to what ever you'd like, this is just an example of scraping one event.
for event_id in range(199,540):
    for card_type in range(0, 10):
        for card_id in range(1, 19):
            for rarity in range(5, 13):
                for evolution in range(1, 2):
                    urls.append('http://cdn-prod.highschooldd.net/sp/image/cards/C/{}{}{:02d}{:02d}{}.png'\
                        .format(event_id, card_type, card_id, rarity, evolution))


async def get_status(url, session):
    async with session.get(url) as response:
        # The server will give a 403 if the file doesn't exist so you could just check against that.
        if response.status == 200:
            return url
        elif response.status not in [403, 200]:
            print(url, response.status, 'something happened?')


async def fetch(url, session):
    async with sem:
        return await get_status(url, session)
    
async def run():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        # Lazy fix for None
        responses = [x for x in responses if x]
        
    # Do whatever you want here, this will dump the URLs to a json file
    print(f'there were {len(responses)} responses')
    with open('dump.json', 'w') as f:
        json.dump(responses, f, indent=4)


# async fun woooo love async wooooooooo yayyyyyyyyyyyyyyyyyyyyyyyy
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)