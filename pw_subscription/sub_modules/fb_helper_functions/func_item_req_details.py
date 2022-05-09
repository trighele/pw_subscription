import os, urllib.parse

from dotenv import load_dotenv
load_dotenv()

def item_req_details(item: str, src_id: str, target_id: str):

    item_formatted = item.replace(' ', '%2520')

    url = 'https://www.facebook.com/api/graphql/'

    variable_string = '{"UFI2CommentsProvider_commentsKey":"MarketplacePDP",\
        "canViewCustomizedProfile":true,\
        "disableDoublePDPFieldFetchFix":false,\
        "feedbackSource":56,\
        "feedLocation":"MARKETPLACE_MEGAMALL",\
        "location_latitude":40.9147,\
        "location_longitude":-74.3842,\
        "location_radius":65,\
        "location_vanity_page_id":"' + src_id + '",\
        "pdpContext_isHoisted":false,\
        "pdpContext_trackingData":"browse_serp:16e8b16e-56f3-40a6-8237-fa8cfee01f74",\
        "referralCode":"marketplace_search",\
        "relay_flight_marketplace_enabled":false,\
        "scale":1,\
        "targetId":"' + target_id + '",\
        "useDefaultActor":false,\
        "__relay_internal__pv__GKMarketplacePdpUfiPerfH12022relayprovider":false}'

    variable_string_formatted = urllib.parse.quote(variable_string)

    payload=f'av=100077957444098&\
        __user=100077957444098&\
        __a=1&\
        __dyn=7AzHK4HwkEng5KbxG4VuC0BVU98nwgU7SbgS3q2ibwNw9G2S7o762S1DwUx60gu0luq7oc81xoswaq221FwgolzUO0n2US2G3i0Boy1PwBgK7o884y0Mo4G4UfoowYwlE-UqwsUkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W3y1MBx_wHwfCm2Sq2-azqwaW22396w8m3216AzUjwTw&\
        __csr=giiOjMDcIG25OH2iQy8OtPjYO9FuBt9bqWEZbRijfimykDgCnB4tG_BGh29t7h24jAJCGleUCi8CWz945ox29KHy-9Gi2mUKV-aJ5z8Kq5e8zkqqinyu48fqxG48KEGdzmbwwxG4UcoclHxW4U5m3O2Ku9xu2p5wAwiUaE8EO0w88awcu1yxWU-UcE1dU4u1ew4mw4FwmE6OEtxubwpE0K-016hym00F9E8E3SDzFFU0atE04Sa2F00NCo1KAC0cOw&\
        __req=1y&\
        __hs=19121.HYP%3Acomet_pkg.2.1.0.2.&\
        dpr=1&\
        __ccg=EXCELLENT&\
        __rev=1005475387&\
        __s=ebby2i%3Amnvtx6%3Awn9ifi&\
        __hsi=7095719461830738164-0&\
        __comet_req=1&\
        fb_dtsg=AQHB9URQb7JhwqY%3A18%3A1652100926&\
        jazoest=21974&\
        lsd=__WJTRPdYMZ4DRXG-aUDDO&\
        __spin_r=1005475387&\
        __spin_b=trunk&\
        __spin_t=1652100929&\
        fb_api_caller_class=RelayModern&\
        fb_api_req_friendly_name=MarketplacePDPContainerQuery&\
        variables={variable_string_formatted}&\
        server_timestamps=true&\
        doc_id=5122276097848826'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-FB-Friendly-Name': 'MarketplacePDPContainerQuery',
        'X-FB-LSD': 'ffUNZgbzj9EEqu5l7MrpzM',
        'Origin': 'https://www.facebook.com',
        'Connection': 'keep-alive',
        'Referer': f'https://www.facebook.com/marketplace/103675689671038/search/?query={item_formatted}',
        'Cookie': f'{os.environ.get("fb_cookie")}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers'
        }

    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=FA95YrUmz3xX4OJrHt5O1Ymt; wd=929x797; datr=FA95YmGcdpuiFz4BGFko-yst; c_user=100077957444098; xs=18%3A9M_ZxyVVcGCJXA%3A2%3A1652100926%3A-1%3A7312; fr=0cKqbswd6hOOiFLYa.AWWgRf6q8jRTDPXNgz1JI-NKS20.BieQ8U.kB.AAA.0.0.BieQ8-.AWU3_UFS1Ok; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1652100937039%2C%22v%22%3A1%7D; c_user=100077957444098; fr=00bFhrbMGJuPDyRWn.AWXSDiub_L2miYzegZ7SjIiQ6L8.BieRAb.kB.AAA.0.0.BieRAb.AWVQeHXZBaI; xs=18%3A9M_ZxyVVcGCJXA%3A2%3A1652100926%3A-1%3A7312%3A%3AAcWigZn_C38etc1IK7tAONLxUw0WInoiLk2ygshdmw',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/marketplace/103675689671038/search/?query=iphone%2013',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'viewport-width': '749',
        'x-fb-friendly-name': 'MarketplacePDPContainerQuery',
        'x-fb-lsd': '__WJTRPdYMZ4DRXG-aUDDO'
    }        
    
    return url, payload, headers

if __name__ == "__main__":
    import httpx

    item='iphone 13'
    src_id='532966698195748'
    target_id='5551101601584454'

    item_req_details = item_req_details(item, src_id, target_id)

    item_api_response = httpx.post(
        url=item_req_details[0], 
        data=item_req_details[1], 
        headers=item_req_details[2], 
        follow_redirects=False
        )       

    print(item_api_response.text)