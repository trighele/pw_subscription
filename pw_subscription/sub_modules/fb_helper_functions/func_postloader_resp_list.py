import json, httpx

def postloader_resp_list(item: str, resp: httpx.Response, result_list: list):
    postload_response = resp.content.decode('utf-8')

    ## Remove Label Dict
    postload_response = postload_response.split('\r\n')[0]

    postload_response_json = json.loads(postload_response)

    postload_results = postload_response_json['data']['marketplace_search']['feed_units']['edges']

    for i in (g for g in postload_results if g['node']['__typename'] == 'MarketplaceFeedListingStoryObject'):
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
        result_list.append(result_dict)

    return result_list

if __name__ == "__main__":

    from func_preloader_req_details import preloader_req_details
    from func_preloader_resp_list import preloader_resp_list
    from func_postloader_req_details import postloader_req_details

    item = 'iphone 13'

    preloader_req_details = preloader_req_details(item)

    preloader_api_response = httpx.post(
        url=preloader_req_details[0], 
        data=preloader_req_details[1], 
        headers=preloader_req_details[2], 
        follow_redirects=False
        )

    preloader_results = preloader_resp_list(item, preloader_api_response)

    end_cursor_br, result_list = preloader_results

    postloader_req_details = postloader_req_details(item, end_cursor_br=end_cursor_br)
    
    postloader_api_response = httpx.post(
        url=postloader_req_details[0], 
        data=postloader_req_details[1], 
        headers=postloader_req_details[2], 
        follow_redirects=False
        )
    
    postloader_results = postloader_resp_list(item, postloader_api_response, result_list)

    print(json.dumps(postloader_results))