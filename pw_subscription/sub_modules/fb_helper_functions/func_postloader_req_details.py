import os, urllib.parse

from dotenv import load_dotenv
load_dotenv()

def postloader_req_details(item: str, end_cursor_br: str):

    item_formatted = item.replace(' ', '%2520')

    url = 'https://www.facebook.com/api/graphql/'

    variable_string = '{"count":24,\
        "cursor":"{\\"pg\\":0,\
        \\"b2c\\":{\\"br\\":\\"\\",\
        \\"it\\":0,\
        \\"hmsr\\":false,\
        \\"tbi\\":0},\
        \\"c2c\\":{\\"br\\":\\"'+ end_cursor_br +'\\",\
        \\"it\\":24,\
        \\"rpbr\\":\\"\\",\
        \\"rphr\\":false},\
        \\"ads\\":{\\"items_since_last_ad\\":20,\
        \\"items_retrieved\\":25,\
        \\"ad_index\\":1,\
        \\"ad_slot\\":1,\
        \\"dynamic_gap_rule\\":0,\
        \\"counted_organic_items\\":0,\
        \\"average_organic_score\\":0,\
        \\"is_dynamic_gap_rule_set\\":false,\
        \\"first_organic_score\\":0,\
        \\"is_dynamic_initial_gap_set\\":false,\
        \\"iterated_organic_items\\":0,\
        \\"top_organic_score\\":0,\
        \\"feed_slice_number\\":0,\
        \\"feed_retrieved_items\\":0,\
        \\"ad_req_id\\":0,\
        \\"refresh_ts\\":0,\
        \\"cursor_id\\":38177,\
        \\"mc_id\\":0,\
        \\"ad_index_e2e\\":0,\
        \\"seen_ads\\":[]},\
        \\"irr\\":false,\
        \\"rui\\":[]}",\
        "params":{"bqf":{"callsite":"COMMERCE_MKTPLACE_WWW",\
        "query":"'+ item +'"},\
        "browse_request_params":{"commerce_enable_local_pickup":true,\
        "commerce_enable_shipping":true,\
        "commerce_search_and_rp_available":true,\
        "commerce_search_and_rp_category_id":[],\
        "commerce_search_and_rp_condition":null,\
        "commerce_search_and_rp_ctime_days":null,\
        "filter_location_latitude":40.9147,\
        "filter_location_longitude":-74.3842,\
        "filter_price_lower_bound":0,\
        "filter_price_upper_bound":214748364700,\
        "filter_radius_km":65},\
        "custom_request_params":{"browse_context":null,\
        "contextual_filters":[],\
        "referral_code":null,\
        "saved_search_strid":null,\
        "search_vertical":"C2C",\
        "seo_url":null,\
        "surface":"SEARCH",\
        "virtual_contextual_filters":[]}},\
        "scale":1}'

    variable_string_formatted = urllib.parse.quote(variable_string)

    payload=f'av=100077957444098&\
        __user=100077957444098&\
        __a=1&\
        __dyn=7AzHK4HwkEng5KbxG4VuC0BVU98nwgU7SbgS3q2ibwNw9G2S7o762S1DwUx609vCxS320om782Cwwwqo465o-cw5MKdwGwQw9m8wsU9kbxS1Fwc61axe3S68f85qfK6E7e58jwGzE7W7oqBwJK2W5olwUwgojUlDw-wUws9ovUaU3VBwJCwLyESE2KwkQq0xoc84K2e&\
        __csr=gF6Fn9mzgx8BQW6FPOk-Bt8kAzkmDjQgxd4hvETR_iZTlBrgxaBnAhbQKCaBAWmdKcGmcKlbKiaBoCSWDx92QfAxWfAyVEG4A9iggz-gwGA3i48hmuiXyGwhUuHzUkwFgbEWq1JxK9xu9AG0R98pwh89-i5po7K3C2K0Eof82Zwm84GcwkUeE66321YwAK18w8S0gu0GU2bw2fU0nCg03cSxi46micw0Gbw0l0ES039q6EdU1sUdqx-1Mg0_20lK&\
        __req=17&\
        __hs=19115.HYP%3Acomet_pkg.2.1.0.2.&\
        dpr=1&\
        __ccg=EXCELLENT&\
        __rev=1005444505&\
        __s=866btt%3A8txo3e%3Am5ql8a&\
        __hsi=7093652700381737707-0&\
        __comet_req=1&\
        fb_dtsg=AQGjnBHuZPJ-YJQ%3A48%3A1649072784&\
        jazoest=21973&\
        lsd=ffUNZgbzj9EEqu5l7MrpzM&\
        __spin_r=1005444505&\
        __spin_b=trunk&\
        __spin_t=1651619724&\
        fb_api_caller_class=RelayModern&\
        fb_api_req_friendly_name=CometMarketplaceSearchContentPaginationQuery&\
        variables={variable_string_formatted}&\
        server_timestamps=true&\
        doc_id=4900245856749252'

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-Friendly-Name': 'CometMarketplaceSearchContentPaginationQuery',
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

    from func_preloader_req_details import preloader_req_details
    from func_preloader_resp_list import preloader_resp_list

    item = 'iphone 13'

    preloader_req_details = preloader_req_details(item)

    preloader_api_response = httpx.post(
        url=preloader_req_details[0], 
        data=preloader_req_details[1], 
        headers=preloader_req_details[2], 
        follow_redirects=False
        )

    preloader_results = preloader_resp_list(item, preloader_api_response)

    end_cursor_br = preloader_results[0]

    postloader_req_details = postloader_req_details(item, end_cursor_br=end_cursor_br)
    
    postloader_api_response = httpx.post(
        url=postloader_req_details[0], 
        data=postloader_req_details[1], 
        headers=postloader_req_details[2], 
        follow_redirects=False
        )
     
    print(postloader_api_response.status_code)