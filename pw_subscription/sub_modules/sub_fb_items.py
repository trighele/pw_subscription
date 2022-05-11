import httpx, json, asyncio, platform, urllib.parse, os
from dotenv import load_dotenv
from datetime import datetime
import re

from sub_modules.fb_helper_functions import func_preloader_req_details, \
    func_preloader_resp_list, \
    func_postloader_req_details, \
    func_postloader_resp_list, \
    func_filter_result_list, \
    func_item_req_details, \
    func_item_update_dict

async def run_initial_items(item_dict: dict):
    
    item = item_dict['item']

    preloader_req_details = func_preloader_req_details.preloader_req_details(item)

    preloader_api_response = await httpx.AsyncClient().post(
        url=preloader_req_details[0],
        data=preloader_req_details[1],
        headers=preloader_req_details[2],
        follow_redirects=False
        )

    end_cursor_br, result_list = func_preloader_resp_list.preloader_resp_list(item, preloader_api_response)

    ## Postloader Call
    postloader_req_details = func_postloader_req_details.postloader_req_details(item, end_cursor_br)

    postload_response = await httpx.AsyncClient().post(
        url=postloader_req_details[0],
        data=postloader_req_details[1],
        headers=postloader_req_details[2]
        )

    result_list = func_postloader_resp_list.postloader_resp_list(item, postload_response, result_list)

    ## Initial filter
    result_list = func_filter_result_list.filter_result_list(result_list, item, min_price=item_dict['min_price'], max_price=item_dict['max_price'])

    return result_list

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

    item = item_dict['query']

    item_req_details = func_item_req_details.item_req_details(item, item_dict['src_id'], item_dict['target_id'])

    item_response = await httpx.AsyncClient().post(
        url=item_req_details[0],
        data=item_req_details[1],
        headers=item_req_details[2],
        timeout=500,
        follow_redirects=False
        )

    item_dict = func_item_update_dict.item_update_dict(item_dict=item_dict, resp=item_response)

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
                "item" : 'iphone 13',
                "min_price" : 200,
                "max_price" : 800
            },
            {
                "item" : 'power washer',
                "min_price" : 100,
                "max_price" : 200
            }
        ]

    load_dotenv()

    results = run_fb_items(testItems)

    json_string = json.dumps(results)
    print(json_string)

    # with open("./test_output/fb_items.json", "w") as file1:
    #     file1.write(json_string)
    # print('Test completed..')
