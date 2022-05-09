import os

from dotenv import load_dotenv
load_dotenv()

def preloader_req_details(item: str):

    item_formatted = item.replace(' ', '%2520')

    url = 'https://www.facebook.com/ajax/route-definition/'

    payload=f'client_previous_actor_id=100077957444098&\
        route_url=%2Fmarketplace%2F103675689671038%2Fsearch%2F%3Fquery%3D{item_formatted}&\
        routing_namespace=fb_comet&\
        __user=100077957444098&\
        __a=1&\
        __dyn=7AzHK4HwkEng5KbxG4VuC0BVU98nwgU7SbgS3q2ibwNw9G2S7o762S1DwUx609vCxS320om782Cwwwqo465o-cw5MKdwGwQw9m8wsU9kbxS2218wc61axe3S68f85qfK6E7e58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUws9ovUaU3VBwJCwLyESE2KwwwOhE25wMwhF8-4UdU&\
        __csr=giiOjMDcIG25OH2bQy8OtPjYO9FuBt9bqWEZbRijfimykDgCnB4tG_BGh29t7h24jAJCGleUCi8CWz945ox29KHy-9Gi2mUKV-aJ5z8Kq5e8zkqqinyu48fqxG48KEGdzmbwwxG4UcoclHxW4U5m3O2Ku9xu2p5wAwiUaE8EO0w88awcu1yxWU-UcE1dU4u1ew4mw4FwmE6OEtxubwpE0K-016hym00F9E8E3SDzFFU0atE04Sa2F00NCo1KAC0cOw&\
        __req=u&\
        __hs=19121.HYP%3Acomet_pkg.2.1.0.2.&\
        dpr=1&\
        __ccg=EXCELLENT&\
        __rev=1005475387&\
        __s=tce1dw%3Amnvtx6%3Awn9ifi&\
        __hsi=7095719461830738164-0&\
        __comet_req=1&\
        fb_dtsg=AQHB9URQb7JhwqY%3A18%3A1652100926&\
        jazoest=21974&\
        lsd=__WJTRPdYMZ4DRXG-aUDDO&\
        __spin_r=1005475387&\
        __spin_b=trunk&\
        __spin_t=1652100929'

    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'{os.environ.get("fb_cookie")}',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/marketplace/103675689671038',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'viewport-width': '749',
        'x-fb-lsd': '__WJTRPdYMZ4DRXG-aUDDO',
        'x-fb-qpl-active-flows': '30605361'
    }

    return url, payload, headers


if __name__ == "__main__":
    import httpx

    preloader_req_details = preloader_req_details('iphone 13')

    preloader_api_response = httpx.post(
        url=preloader_req_details[0], 
        data=preloader_req_details[1], 
        headers=preloader_req_details[2], 
        follow_redirects=False
        )
    
    print(preloader_api_response.text)