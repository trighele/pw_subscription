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
        \\"cursor_id\\":60941,\
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
        __dyn=7AzHK4HwkEng5KbxG4VuC0BVU98nwgU7SbgS3q2ibwNw9G2S7o762S1DwUx609vCxS320om782Cwwwqo465o-cw5MKdwGwQw9m8wsU9kbxS2218wc61axe3S68f85qfK6E7e58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUws9ovUaU3VBwJCwLyESE2KwwwOhE25wMwhF8-4UdU&\
        __csr=giiOjMDcIG25OH2bQy8OtPjYO9FuBt9bqWEZbRijfimykDgCnB4tG_BGh29t7h24jAJCGleUCi8CWz945ox29KHy-9Gi2mUKV-aJ5z8Kq5e8zkqqinyu48fqxG48KEGdzmbwwxG4UcoclHxW4U5m3O2Ku9xu2p5wAwiUaE8EO0w88awcu1yxWU-UcE1dU4u1ew4mw4FwmE6OEtxubwpE0K-016hym00F9E8E3SDzFFU0atE04Sa2F00NCo1KAC0cOw&\
        __req=1c&\
        __hs=19121.HYP%3Acomet_pkg.2.1.0.2.&\
        dpr=1&\
        __ccg=EXCELLENT&\
        __rev=1005475387&\
        __s=fjyqn7%3Amnvtx6%3Awn9ifi&\
        __hsi=7095719461830738164-0&\
        __comet_req=1&\
        fb_dtsg=AQHB9URQb7JhwqY%3A18%3A1652100926&\
        jazoest=21974&\
        lsd=__WJTRPdYMZ4DRXG-aUDDO&\
        __spin_r=1005475387&\
        __spin_b=trunk&\
        __spin_t=1652100929&\
        fb_api_caller_class=RelayModern&\
        fb_api_req_friendly_name=CometMarketplaceSearchContentPaginationQuery&\
        variables={variable_string_formatted}&\
        server_timestamps=true&\
        doc_id=4900245856749252'

    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'{os.environ.get("fb_cookie")}',
        'origin': 'https://www.facebook.com',
        'referer': f'https://www.facebook.com/marketplace/103675689671038/search/?query={item_formatted}',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'viewport-width': '749',
        'x-fb-friendly-name': 'CometMarketplaceSearchContentPaginationQuery',
        'x-fb-lsd': '__WJTRPdYMZ4DRXG-aUDDO'
    }    

    return url, payload, headers

if __name__ == "__main__":
    import httpx

    from func_preloader_req_details import preloader_req_details
    from func_preloader_resp_list import preloader_resp_list

    item = 'playstation'

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
     
    print(postloader_api_response.text)