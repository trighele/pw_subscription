import os, mysql.connector
from dotenv import load_dotenv

load_dotenv()

env = os.environ.get('env')

def read_queries():
    mydb = mysql.connector.connect(
        host=os.environ.get('mysql_host'),
        user=os.environ.get('mysql_user'),
        password=os.environ.get('mysql_password'),
        database=os.environ.get('mysql_database_prefix') + env
    )

    cursor = mydb.cursor()

    cursor.execute(f'SELECT * FROM query_items where active = 1')
    result = cursor.fetchall()

    query_list = []
    for i in result:
        query_dict = {}
        query_dict['item'] = i[1]
        query_dict['min_price'] = i[2]
        query_dict['max_price'] = i[3]
        query_list.append(query_dict)

    return query_list

def filter_items(idList):
    mydb = mysql.connector.connect(
        host=os.environ.get('mysql_host'),
        user=os.environ.get('mysql_user'),
        password=os.environ.get('mysql_password'),
        database=os.environ.get('mysql_database_prefix') + env
    )

    cursor = mydb.cursor()

    id_list_filtered = list()

    for id in idList:
        cursor.execute(f"SELECT COUNT(*) FROM listings where src_id = '{id}'")
        result = cursor.fetchall()

        if result[0][0] == 0:
            id_list_filtered.append(id)

    return id_list_filtered

def read_active_items():
    mydb = mysql.connector.connect(
        host=os.environ.get('mysql_host'),
        user=os.environ.get('mysql_user'),
        password=os.environ.get('mysql_password'),
        database=os.environ.get('mysql_database_prefix') + env
    )

    cursor = mydb.cursor()

    cursor.execute(f'SELECT * FROM listings where active = 1')
    result = cursor.fetchall()

    result_list = list()
    for i in result:
        item_dict = {}
        item_dict['src_id'] = i[1]
        item_dict['source'] = i[2]
        item_dict['query'] = i[3]
        item_dict['title'] = i[4]
        item_dict['price'] = float(i[5])
        item_dict['post_type'] = i[6]
        item_dict['post_time'] = i[7].strftime("%Y-%m-%d %H:%M")
        item_dict['location'] = i[8]
        item_dict['distance'] = float(i[9])
        item_dict['url'] = i[10]
        item_dict['item_description'] = i[11]
        result_list.append(item_dict)

    return result_list


if __name__ == "__main__":

    # test = read_items()
    # print(test)

    # testIDs = ['7465407650',  '7465048658',  '699796994483303',   '367591711908867',  '1290304091461943']
    # print(filter_items(testIDs))

    print(read_active_items())