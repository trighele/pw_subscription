import os, mysql.connector, datetime
from dotenv import load_dotenv

load_dotenv()

env = os.environ.get('env')

def write_items(itemList: list):
    mydb = mysql.connector.connect(
        host=os.environ.get('mysql_host'),
        user=os.environ.get('mysql_user'),
        password=os.environ.get('mysql_password'),
        database=os.environ.get('mysql_database_prefix') + env
    )

    cursor = mydb.cursor()

    for item in itemList:
        if 'item_description' in item:
            sql = "INSERT INTO listings \
                (src_id,source,query,title,price,post_type,post_time,location,distance,url,item_description,record_createddate,active) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (item["src_id"], \
                item["source"], \
                item["query"], \
                item["title"], \
                item["price"], \
                item["post_type"], \
                item["post_time"], \
                item["location"], \
                item["distance"], \
                item["url"], \
                item["item_description"], \
                datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),\
                1)
            cursor.execute(sql, val)
        else:
            sql = "INSERT INTO listings \
                (src_id,source,query,title,price,post_type,post_time,location,distance,url,record_createddate,active) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (item["src_id"], \
                item["source"], \
                item["query"], \
                item["title"], \
                item["price"], \
                item["post_type"], \
                item["post_time"], \
                item["location"], \
                item["distance"], \
                item["url"], \
                datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),\
                1)
            cursor.execute(sql, val)

        mydb.commit()            

    return 

def deactivate_items(idList: list):
    mydb = mysql.connector.connect(
        host=os.environ.get('mysql_host'),
        user=os.environ.get('mysql_user'),
        password=os.environ.get('mysql_password'),
        database=os.environ.get('mysql_database_prefix') + env
    )

    cursor = mydb.cursor()

    for id in idList:

        cursor.execute(f'UPDATE listings set active = 0 where src_id ={id}')

        mydb.commit()
        
    return


if __name__ == "__main__":

    # test = read_items()
    # print(test)

    testList = [{'src_id': '7465407650',
  'source': 'craigslist',
  'query': 'iphone 13 pro max',
  'title': 'Iphone 13 Pro Max Unlocked',
  'price': 980.0,
  'post_type': 'pickup',
  'post_time': '2022-03-31 18:13',
  'location': 'Wayne',
  'distance': 5.2,
  'url': 'https://newjersey.craigslist.org/mob/d/wayne-iphone-13-pro-max-unlocked/7465407650.html'}]
    write_items(testList)