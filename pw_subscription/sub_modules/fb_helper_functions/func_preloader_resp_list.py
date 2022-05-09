import httpx, json
from parso import split_lines

def preloader_resp_list(item: str, resp: httpx.Response):
    resp_text = resp.text

    resp_split = split_lines(resp_text)

    for i in resp_split:
        if 'MarketplaceFeedListingStoryObject' in i:
            resp_filtered = json.loads(i.replace('for (;;);', ''))

    ## Obtain end cursor br for post preload call
    end_cursor = resp_filtered['result']['result']['data']['marketplace_search']['feed_units']['page_info']['end_cursor']
    end_cursor_json = json.loads(end_cursor)
    end_cursor_br = end_cursor_json['c2c']['br']

    results = resp_filtered['result']['result']['data']['marketplace_search']['feed_units']['edges']

    ## Compile initial results
    results_list = []
    for i in (g for g in results if g['node']['__typename'] == 'MarketplaceFeedListingStoryObject'):
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

    return end_cursor_br, results_list

if __name__ == "__main__":
    
    import func_preloader_req_details

    item = 'digital camera'

    preloader_req_details = func_preloader_req_details.preloader_req_details(item)

    preloader_api_response = httpx.post(
        url=preloader_req_details[0], 
        data=preloader_req_details[1], 
        headers=preloader_req_details[2], 
        follow_redirects=False
        )
        
    preloader_results = preloader_resp_list(item, preloader_api_response)

    print('End cursor ==>')
    print(preloader_results[0])
    print('Results List==>')
    print(preloader_results[1])