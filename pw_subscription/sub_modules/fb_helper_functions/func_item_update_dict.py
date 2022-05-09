import httpx, json
from datetime import datetime
from geopy.distance import geodesic

def item_update_dict(item_dict: dict, resp: httpx.Response):

    item_response = resp.content.decode('utf-8')
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

if __name__ == "__main__":
    import func_item_req_details

    item='iphone 13'
    src_id='725492411932215'
    target_id='4944658752311726'

    item_dict={'src_id': '725492411932215', 'source': 'fb_marketplace', 'title': 'Iphone 13 Pro Max Unlocked 128gb', 'query': 'iphone 13', 'post_type': ['IN_PERSON', 'PUBLIC_MEETUP'], 'price': '$900', 'target_id': '4944658752311726', 'url': 'https://www.facebook.com/marketplace/item/725492411932215'}

    item_req_details = func_item_req_details.item_req_details(item, src_id, target_id)

    item_api_response = httpx.post(
        url=item_req_details[0], 
        data=item_req_details[1], 
        headers=item_req_details[2], 
        follow_redirects=False
        )       

    item_dict = item_update_dict(item_dict, item_api_response)

    print(json.dumps(item_dict))