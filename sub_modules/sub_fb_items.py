import httpx, json, asyncio, platform, urllib.parse, os
from dotenv import load_dotenv
from datetime import datetime
from geopy.distance import geodesic
from parso import split_lines
import re

async def run_initial_items(item_dict: dict):
    
    item = item_dict['item']
    item_formatted = item.replace(' ', '%2520')

    preloader_url = "https://www.facebook.com/ajax/route-definition/"

    preloader_payload=f'client_previous_actor_id=&\
    route_url=%2Fmarketplace%2F103675689671038%2Fsearch%2F%3Fquery%3D{item_formatted}&\
    routing_namespace=fb_comet&\
    __user=0&\
    __a=1&\
    __dyn=7xeUmwlE7ibwKBWo2vwAxu13wvoKewSwMwNw9G2S0im3y4o0B-q1ew65xO0FE2awt81sbzoaEd82ly87e2l0Fwqo31wnEfo5m1mxe6E7e58jwGzEao4236222SUbElxm0zK5o4q0GpovU1aUbodEGdwko2QwbS1bw&\
    __csr=hIIg-ySHYAR9qGGhml9HQqivGAuypWgF7CBl7Gl6KFonLgK8G9KayGUPJ5zAFQ79oCqfyoO5oiVVVVV4qVayorG4U4m4EsxKaxr-6polxF7UC8z9E88981jKU0mUw1SS0sOE099y00V7w0Czw0nPU0G-0zeh4ACwj86quqp2pe09UDypk5UB0by0E89o0swg5W2l2E27w2To0DC4E0i9w1h96wFw_w0yQxm9wiZm1JGm9giOwcm059U0bZ81do1l81cEmw1CWawioLwXCwfi&\
    __req=y&\
    __hs=19072.HYP%3Acomet_loggedout_pkg.2.0.0.0.&\
    dpr=1&\
    __ccg=EXCELLENT&\
    __rev=1005218752&\
    __s=v7uzhb%3Awrp5dt%3Ar9ja1q&\
    __hsi=7077666656081570639-0&\
    __comet_req=1&\
    lsd=AVp4CUdbFLA&\
    jazoest=2876&\
    __spin_r=1005218752&\
    __spin_b=trunk&\
    __spin_t=1647897683'
    preloader_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-LSD': 'AVp4CUdbFLA',
    'Origin': 'https://www.facebook.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.facebook.com/marketplace/103675689671038',
    'Cookie': f'{os.environ.get("fb_cookie")}',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'trailers'
    }    

    preloader_api_response = await httpx.AsyncClient().post(preloader_url, headers=preloader_headers, data=preloader_payload)
    preloader_response = preloader_api_response.text

    preloader_response_split = split_lines(preloader_response)

    for i in preloader_response_split:
        if 'marketplace_search' in i:
            preloader_response_filtered = json.loads(i.replace('for (;;);', ''))

    ## Obtain end cursor br for post preload call
    end_cursor = preloader_response_filtered['result']['result']['data']['marketplace_search']['feed_units']['page_info']['end_cursor']
    end_cursor_json = json.loads(end_cursor)
    end_cursor_br = end_cursor_json['c2c']['br']

    preloader_results = preloader_response_filtered['result']['result']['data']['marketplace_search']['feed_units']['edges']

    ## Compile initial results
    results_list = []
    for i in preloader_results:
        result_dict = {}
        fb_id = i['node']['listing']['id']
        title = i['node']['listing']['marketplace_listing_title']
        delivery_types = i['node']['listing']['delivery_types']
        price = i['node']['listing']['listing_price']['formatted_amount']
        url = f'https://www.facebook.com/marketplace/item/{fb_id}'

        tracking_info = json.loads(i['node']['tracking'])
        commerce_rank_obj = json.loads(tracking_info['commerce_rank_obj'])
        target_id = str(commerce_rank_obj['target_id'])

        result_dict['src_id'] = fb_id
        result_dict['source'] = 'fb_marketplace'
        result_dict['title'] = title
        result_dict['query'] = item
        result_dict['post_type'] = delivery_types
        result_dict['price'] = price
        result_dict['target_id'] = target_id
        result_dict['url'] = url
        results_list.append(result_dict) 

    ## Postloader Call
    postloader_url = "https://www.facebook.com/api/graphql/"

    postloader_variable_string = '{"count":24,\
    "cursor":"{\\"pg\\":0,\
    \\"b2c\\":{\\"br\\":\\"\\",\
    \\"it\\":0,\
    \\"hmsr\\":false,\
    \\"tbi\\":0},\
    \\"c2c\\":{\\"br\\":\\"' + end_cursor_br + '\\",\
    \\"it\\":0,\
    \\"rpbr\\":\\"\\",\
    \\"rphr\\":false},\
    \\"irr\\":false,\
    \\"rui\\":[]}",\
    "params":{"bqf":{"callsite":"COMMERCE_MKTPLACE_WWW",\
    "query":"' + item +  '"},\
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

    postload_payload=f'av=0&\
    __user=0&\
    __a=1&\
    __dyn=7xeUmwlE7ibwKBWo2vwAxu13wvoKewSwMwNw9G2S0im3y4o0B-q1ew65xO0FE2awt81sbzoaEd82ly87e2l0Fwqo31wnEfo5m1mxe6E7e58jwGzEao4236222SUbElxm0zK5o4q0GpovU1aUbodEGdwko2QwbS1bw&\
    __csr=hIIg-ySHYAR9qGGhml9HQqivGAuypWgF7CBl7Gl6KFonLgK8G9KayGUPJ5zAFQ79oCqfyoO5oiVVVVV4qVayorG4U4m4EsxKaxr-6polxF7UC8z9E88981jKU0mUw1SS0sOE099y00V7w0Czw0nPU0G-0zeh4ACwj86quqp2pe09UDypk5UB0by0E89o0swg5W2l2E27w2To0DC4E0i9w1h96wFw_w0yQxm9wiZm1JGm9giOwcm059U0bZ81do1l81cEmw1CWawioLwXCwfi&\
    __req=1f&\
    __hs=19072.HYP%3Acomet_loggedout_pkg.2.0.0.0.&\
    dpr=1&\
    __ccg=EXCELLENT&\
    __rev=1005218752&\
    __s=v7uzhb%3Awrp5dt%3Ar9ja1q&\
    __hsi=7077666656081570639-0&\
    __comet_req=1&\
    lsd=AVp4CUdbFLA&\
    jazoest=2876&\
    __spin_r=1005218752&\
    __spin_b=trunk&\
    __spin_t=1647897683&\
    fb_api_caller_class=RelayModern&\
    fb_api_req_friendly_name=CometMarketplaceSearchContentPaginationQuery&\
    variables={urllib.parse.quote(postloader_variable_string)}&\
    server_timestamps=true&\
    doc_id=7111939778879383'
    postload_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-Friendly-Name': 'CometMarketplaceSearchContentPaginationQuery',
    'X-FB-LSD': 'AVp4CUdbFLA',
    'Origin': 'https://www.facebook.com',
    'DNT': '1',
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

    postload_response = await httpx.AsyncClient().post(postloader_url, headers=postload_headers, data=postload_payload)
    postload_response = postload_response.content.decode('utf-8')

    postload_response_json = json.loads(postload_response)
    postload_results = postload_response_json['data']['marketplace_search']['feed_units']['edges']

    for i in postload_results:
        result_dict = {}
        fb_id = i['node']['listing']['id']
        title = i['node']['listing']['marketplace_listing_title']
        delivery_types = i['node']['listing']['delivery_types']
        price = i['node']['listing']['listing_price']['formatted_amount']
        url = f'https://www.facebook.com/marketplace/item/{fb_id}'

        tracking_info = json.loads(i['node']['tracking'])
        commerce_rank_obj = json.loads(tracking_info['commerce_rank_obj'])
        target_id = str(commerce_rank_obj['target_id'])

        result_dict['src_id'] = fb_id
        result_dict['source'] = 'fb_marketplace'
        result_dict['title'] = title
        result_dict['query'] = item
        result_dict['post_type'] = delivery_types
        result_dict['price'] = price
        result_dict['target_id'] = target_id
        result_dict['url'] = url
        results_list.append(result_dict)

    ## Initial filter
    filtered_results_list = []
    for result in results_list:
        result_price = int(result['price'].replace('$', '').replace(',', ''))
        if result_price >= item_dict['min_price'] and result_price <= item_dict['max_price']:
            if item in result['title'].lower():
                filtered_results_list.append(result)

    return filtered_results_list

async def main_one(queryList: list):

    tasks = list()

    for item_dict in queryList:
        tasks.append(run_initial_items(item_dict))

    results = await asyncio.gather(*tasks)

    compiled_results = list()
    for itemlist in results:
        for itemdict in itemlist:
            compiled_results.append(itemdict)    

    return compiled_results

async def run_item_detail(item_dict: dict):
    fb_location_code='103675689671038'
    item = item_dict['query']
    item_formatted = item.replace(' ', '%2520')    

    item_variable_string = '{"UFI2CommentsProvider_commentsKey":"MarketplacePDP",\
    "canViewCustomizedProfile":true,\
    "disableDoublePDPFieldFetchFix":false,\
    "disableMarketplaceRelay3DPDPUFI":false,\
    "feedbackSource":56,\
    "feedLocation":"MARKETPLACE_MEGAMALL",\
    "location_latitude":40.904846191406,\
    "location_longitude":-74.218139648438,\
    "location_radius":64,\
    "location_vanity_page_id":"' + item_dict['src_id'] + '",\
    "pdpContext_isHoisted":false,\
    "pdpContext_trackingData":null,\
    "referralCode":"marketplace_search",\
    "relay_flight_marketplace_enabled":false,\
    "scale":1,\
    "targetId":"'+ item_dict['target_id'] + '",\
    "useDefaultActor":false}'
    
    item_payload=f'av=0&\
    __user=0&\
    __a=1&\
    __dyn=7xeUmwlE7ibwKBWo2vwAxu13wvoKewSwMwNw9G2S0im3y4o0B-q1ew65xO0FE2awt81sbzoaEd82ly87e2l0Fwqo31wnEfo5m1mxe6E7e58jwGzEao7a222SUbElxm0zK5o4q0GpovU1aUbodEGdw46wbS&\
    __csr=gCzjFkJ4hbJkibXALWyqBixmVahHBzummcyp8lymqEjgS5VEG5-dG36il7GE8U6u6E-5WDxS688-2ufwdC1uw1quaG01nzwpo02Bxw2oE1r889f88wwx2lk09gwOw1cW0c8wiQ0hq9wiE08n82kw1ty0cUw0T2o0pjKryU0VG0iGU0Ya&\
    __req=g&\
    __hs=19056.HYP%3Acomet_loggedout_pkg.2.0.0.0.&\
    dpr=1&\
    __ccg=EXCELLENT&\
    __rev=1005153157&\
    __s=2mv3bz%3At6etgc%3A9iv1s3&\
    __hsi=7071436759572573889-0&\
    __comet_req=1&\
    lsd=AVoZjmreLJQ&\
    jazoest=21013&\
    __spin_r=1005153157&\
    __spin_b=trunk&\
    __spin_t=1646447172&\
    fb_api_caller_class=RelayModern&\
    fb_api_req_friendly_name=MarketplacePDPContainerQuery&\
    variables={urllib.parse.quote(item_variable_string)}&\
    server_timestamps=true&\
    doc_id=5624002367617034'
    item_headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': f'{os.environ.get("fb_cookie")}',
    'DNT': '1',
    'Origin': 'https://www.facebook.com',
    'Referer': f'https://www.facebook.com/marketplace/{fb_location_code}/search/?query={item_formatted}',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'X-FB-Friendly-Name': 'MarketplacePDPContainerQuery',
    'X-FB-LSD': 'AVoZjmreLJQ'
    }    

    item_response = await httpx.AsyncClient().post("https://www.facebook.com/api/graphql", headers=item_headers, data=item_payload, timeout=500)
    item_response = item_response.content.decode('utf-8')
    json_item_response = json.loads(item_response)

    item_description = json_item_response['data']['viewer']['marketplace_product_details_page']['target']['redacted_description']['text']
    creation_time = datetime.fromtimestamp(json_item_response['data']['viewer']['marketplace_product_details_page']['target']['creation_time']).strftime("%Y-%m-%d %H:%M")
    location_text =  json_item_response['data']['viewer']['marketplace_product_details_page']['target']['location_text']['text']
    loc_lat = json_item_response['data']['viewer']['marketplace_product_details_page']['marketplace_listing_renderable_target']['location']['latitude']
    loc_lng = json_item_response['data']['viewer']['marketplace_product_details_page']['marketplace_listing_renderable_target']['location']['longitude']
    distance = round(geodesic((loc_lat, loc_lng), (40.9230477, -74.3433955)).miles,2)

    item_dict['post_time'] = creation_time
    item_dict['location'] = location_text
    item_dict['distance'] = distance
    item_dict['item_description'] = item_description

    return item_dict

async def main_two(resultList: list):

    tasks = list()

    for item_dict in resultList:
        tasks.append(run_item_detail(item_dict))

    results = await asyncio.gather(*tasks)

    return results

def run_fb_items(queryList):

    def format_results(results: list):

        def convert_string(title):
            emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)

            new_title = (re.sub('[\W_]+', ' ', emoji_pattern.sub(r'', title), flags=re.UNICODE)).strip()

            return new_title   

        for i in results:
            i['title'] = convert_string(i['title'])[0:100]
            i['item_description'] = convert_string(i['item_description'])[0:200]
            post_type = 'pickup'
            for j in i['post_type']:
                if 'SHIP' in j:
                    post_type = 'ship'
            i['post_type'] = post_type
            i['price'] = float(i['price'].replace('$', '').replace(',',''))
            i.pop('target_id', None)

        return results

    
    def count_and_filter(results: list):
        result_dict = {}
        unfiltered_count = len(results)
        mile_filter = 20.0

        filtered_list = []
        for i in results:
            if i['distance'] <= mile_filter:
                filtered_list.append(i)

        filtered_count = len(filtered_list)

        return {"unfiltered_count": unfiltered_count, "filtered_count": filtered_count, "results": filtered_list}        

    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    results_list_one = asyncio.run(main_one(queryList=queryList))
    results = asyncio.run(main_two(resultList=results_list_one))
    results = format_results(results)
    results = count_and_filter(results)

    return results

if __name__ == "__main__":

    testItems = [
            {
                "item" : 'iphone 13 max',
                "min_price" : 200,
                "max_price" : 800
            },
            {
                "item" : 'digital camera',
                "min_price" : 200,
                "max_price" : 500
            }
        ]

    load_dotenv()

    results = run_fb_items(testItems)

    json_string = json.dumps(results)
    with open("./test_output/fb_items.json", "w") as file1:
        file1.write(json_string)
    print('Test completed..')   

