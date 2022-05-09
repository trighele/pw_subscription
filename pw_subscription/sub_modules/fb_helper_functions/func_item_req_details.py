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
        "pdpContext_trackingData":"browse_serp:d47bf3a8-73bf-4fff-a2ee-7fb37a90c051",\
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
        __dyn=7AzHK4HwkEng5KbxG4VuC0BVU98nwgU7SbgS3q2ibwNw9G2S7o762S1DwUx609vCxS320om782Cwwwqo465o-cw5MKdwGwQw9m8wsU9kbxS1Fwc61axe3S68f85qfK6E7e58jwGzE7W7oqBwJK2W5olwUwgojUlDw-wUws9ovUaU3VBwJCwLyESE2KwkQq0xoc84K2e&\
        __csr=gF6Fn9mzgx8BQW6FPOk-Bt8kAzkmDjQgxd4hvETR_iZTlBrgxaBnAhbQKCaBAWmdKcGmcKlbKiaBoCSWDx92QfJ1WfAyVEG4A9iggz-gwGA3i48hmuiXyGwhUuHzUkwFgbEWq1JxK9xu9AG1ew8mi6o4i2vAxmm1XwVwHwa63O0Lo5y1az85e3G1xwMwv89bwi82dw47waK0yU0z-05VA00PdEkx1BAz80ayU05gadw0OmxG3u0ne3mEvws40fMw5rw&\
        __req=1s&\
        __hs=19115.HYP%3Acomet_pkg.2.1.0.2.&\
        dpr=1&\
        __ccg=EXCELLENT&\
        __rev=1005444505&\
        __s=t3zlb4%3A8txo3e%3Am5ql8a&\
        __hsi=7093652700381737707-0&\
        __comet_req=1&\
        fb_dtsg=AQGjnBHuZPJ-YJQ%3A48%3A1649072784&\
        jazoest=21973&\
        lsd=ffUNZgbzj9EEqu5l7MrpzM&\
        __spin_r=1005444505&\
        __spin_b=trunk&\
        __spin_t=1651619724&\
        fb_api_caller_class=RelayModern&\
        fb_api_req_friendly_name=MarketplacePDPContainerQuery&\
        variables={variable_string_formatted}&\
        server_timestamps=true&\
        doc_id=5081507548628867'

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
    
    return url, payload, headers

if __name__ == "__main__":
    import httpx

    item='iphone 13'
    src_id='725492411932215'
    target_id='4944658752311726'

    item_req_details = item_req_details(item, src_id, target_id)

    item_api_response = httpx.post(
        url=item_req_details[0], 
        data=item_req_details[1], 
        headers=item_req_details[2], 
        follow_redirects=False
        )       

    print(item_api_response.status_code)