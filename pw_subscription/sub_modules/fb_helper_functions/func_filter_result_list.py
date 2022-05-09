
def filter_result_list(result_list: list, item: str, min_price: int, max_price: int):
    filtered_results_list = []
    for result in result_list:
        result_price = float(result['price'].replace('$', '').replace(',', ''))
        if result_price >= min_price and result_price <=  max_price:
            if item in result['title'].lower():
                filtered_results_list.append(result)

    return filtered_results_list

if __name__ == "__main__":
    import json

    item = 'iphone 13'
    min_price = 100
    max_price = 300

    result_list = [{'src_id': '419615899511418',   'source': 'fb_marketplace',   'title': 'Iphone 13 brand New 128GB factory unlocked midnight color .only for pick up Newark NJ 07104',   'query': 'iphone 13',   'post_type': ['IN_PERSON', 'DOOR_PICKUP'],   'price': '$699',   'target_id': '4848683045228923',   'url': 'https://www.facebook.com/marketplace/item/419615899511418'},  {'src_id': '1425771911206002',   'source': 'fb_marketplace',   'title': 'iPhone 13',   'query': 'iphone 13',   'post_type': ['SHIPPING_ONSITE', 'IN_PERSON'],   'price': '$350',   'target_id': '4353250221378081',   'url': 'https://www.facebook.com/marketplace/item/1425771911206002'},  {'src_id': '725492411932215',   'source': 'fb_marketplace',   'title': 'Iphone 13 Pro Max Unlocked 128gb',   'query': 'iphone 13',   'post_type': ['IN_PERSON', 'PUBLIC_MEETUP'],   'price': '$900',   'target_id': '4944658752311726',   'url': 'https://www.facebook.com/marketplace/item/725492411932215'},  {'src_id': '313792140832989',   'source': 'fb_marketplace',   'title': 'Apple iPhone 13 Pro Max 128 GB in Graphite',   'query': 'iphone 13',   'post_type': ['IN_PERSON', 'SHIPPING_ONSITE'],   'price': '$500',   'target_id': '4024463841011748',   'url': 'https://www.facebook.com/marketplace/item/313792140832989'},  {'src_id': '1019365302351884',   'source': 'fb_marketplace',   'title': 'Apple iPhone 13 used like new!',   'query': 'iphone 13',   'post_type': ['SHIPPING_ONSITE'],   'price': '$350',   'target_id': '5191903177514226',   'url': 'https://www.facebook.com/marketplace/item/1019365302351884'},  {'src_id': '528695802323870',   'source': 'fb_marketplace',   'title': 'Iphone 13',   'query': 'iphone 13',   'post_type': ['SHIPPING_ONSITE', 'IN_PERSON'],   'price': '$500',   'target_id': '7305393242864306',   'url': 'https://www.facebook.com/marketplace/item/528695802323870'},  {'src_id': '2083481521808277',   'source': 'fb_marketplace',   'title': 'iPhone 13 pro',   'query': 'iphone 13',   'post_type': ['IN_PERSON', 'SHIPPING_ONSITE'],   'price': '$500',   'target_id': '7004231166315621',   'url': 'https://www.facebook.com/marketplace/item/2083481521808277'},  {'src_id': '867088690762533',   'source': 'fb_marketplace',   'title': 'iPhone 13 Pro',   'query': 'iphone 13',   'post_type': ['SHIPPING_ONSITE', 'IN_PERSON'],   'price': '$450',   'target_id': '4887978991289777',   'url': 'https://www.facebook.com/marketplace/item/867088690762533'},  {'src_id': '484019486741237',   'source': 'fb_marketplace',   'title': 'Iphone 13 Fully Unlocked',   'query': 'iphone 13',   'post_type': ['SHIPPING_ONSITE', 'IN_PERSON'],   'price': '$400',   'target_id': '4827677910687682',   'url': 'https://www.facebook.com/marketplace/item/484019486741237'},  {'src_id': '568620650787029',   'source': 'fb_marketplace',   'title': 'APPLE IPHONE 13 (UNLOCKED)',   'query': 'iphone 13',   'post_type': ['SHIPPING_ONSITE'],   'price': '$300',   'target_id': '5599071323450945',   'url': 'https://www.facebook.com/marketplace/item/568620650787029'}]

    result_list = filter_result_list(result_list, item, min_price, max_price)

    print(json.dumps(result_list))