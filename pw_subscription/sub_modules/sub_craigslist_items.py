import json, asyncio, re
from playwright.async_api import async_playwright, BrowserContext

async def run_item(context: BrowserContext, query: dict): 
    min_price = str(query['min_price'])
    max_price = str(query['max_price'])
    zip='07082'
    item_formatted = query['item'].replace(' ','+')
    url = f'https://newjersey.craigslist.org/search/sss?query={item_formatted}&purveyor-input=all&srchType=T&postedToday=1&search_distance=40&postal={zip}&min_price={min_price}&max_price={max_price}'    

    

    page = await context.new_page()
    await page.goto(url)

    results = await page.query_selector_all('.result-info')

    item_list = []

    for row in results:    
        item_dict={}

        title_handler = await row.query_selector('.result-title.hdrlnk')
        title = await title_handler.inner_text()
        url = await title_handler.get_attribute('href')
        cl_id = await title_handler.get_attribute('data-id')

        if await row.query_selector('.result-price'):
            price_handler = await row.query_selector('.result-price')
            price = await price_handler.inner_text()
        else:
            price = "$0"

        if await row.query_selector('.result-hood'):
            location_handler = await row.query_selector('.result-hood')
            location = await location_handler.inner_text()
        elif await row.query_selector('.nearby'):
            location_handler = await row.query_selector('.nearby')
            location = await location_handler.inner_text()
        else:
            location = 'N/A'

        location = await location_handler.inner_text()

        distance_handler = await row.query_selector('.maptag')
        distance = await distance_handler.inner_text()
        distance = float(distance.replace('mi', ''))

        post_time_handler = await page.query_selector('.result-date')
        post_time = await post_time_handler.get_attribute('datetime')

        item_dict['src_id'] = cl_id
        item_dict['source'] = 'craigslist'
        item_dict['query'] = query['item']
        item_dict["title"] = title
        item_dict["price"] = price
        item_dict['post_type'] = 'pickup'
        item_dict['post_time'] = post_time
        item_dict["location"] = location
        item_dict["distance"] = distance
        item_dict["url"] = url

        item_list.append(item_dict)

    return item_list

async def main(queryList: list):

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()

        tasks = list()

        for query in queryList:
            tasks.append(run_item(context, query))

        results = await asyncio.gather(*tasks)

        compiled_results = list()
        for itemlist in results:
            for itemdict in itemlist:
                compiled_results.append(itemdict)

        await context.close() 
        await browser.close()
    
    return compiled_results


def run_cl_items(queryList: list):

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
            i['location'] = i['location'].replace('(','').replace(')','')
            i['price'] = float(i['price'].replace('$', '').replace(',',''))


        return results

    
    def count_and_filter(results: list):
        result_dict = {}
        unfiltered_count = len(results)
        mile_filter = 20.0

        filtered_list = []
        for i in results:
            if i['distance'] <= mile_filter:
                if(i['query'].lower() in i['title'].lower()):
                    filtered_list.append(i)

        filtered_count = len(filtered_list)

        return {"unfiltered_count": unfiltered_count, "filtered_count": filtered_count, "results": filtered_list}        

    results = asyncio.run(main(queryList=queryList))
    results = format_results(results)
    results = count_and_filter(results)

    return results


if __name__ == "__main__":

    testItems = [
            {
                "item" : 'iphone 13 max',
                "min_price" : 200,
                "max_price" : 500
            },
            {
                "item" : 'digital camera',
                "min_price" : 200,
                "max_price" : 500
            }
        ]

    results = run_cl_items(testItems)

    json_string = json.dumps(results)
    with open("./test_output/cl_items.json", "w") as file1:
        file1.write(json_string)
    print('Test completed..')       