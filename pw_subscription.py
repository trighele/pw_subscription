import os, json, concurrent.futures
from sub_modules import sub_read_database, sub_write_database, sub_send_email
from sub_modules.sub_craigslist_items import run_cl_items
from sub_modules.sub_fb_items import run_fb_items
from dotenv import load_dotenv
load_dotenv()

query_list = sub_read_database.read_queries()

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(run_cl_items, query_list)
    f2 = executor.submit(run_fb_items, query_list)
    cl_items = f1.result()
    fb_items = f2.result()

    all_items = cl_items['results'] + fb_items['results']

id_list = [item['src_id'] for item in all_items]

id_list_filtered = sub_read_database.filter_items(id_list)

if len(id_list_filtered) == 0:
    print('No new items...')
else:
    all_items_filtered = []
    for item in all_items:
        if item['src_id'] in id_list_filtered:
            all_items_filtered.append(item)

    sub_write_database.write_items(all_items_filtered)

    sub_send_email.send_email(sub_read_database.read_active_items())
    
    print('New items sent...')

    sub_write_database.deactivate_items(id_list_filtered)