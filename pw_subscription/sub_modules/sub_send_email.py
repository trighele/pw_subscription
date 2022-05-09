import pandas as pd
from pandas.core.base import PandasObject
from pandas.core.frame import DataFrame
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl, datetime, os
from dotenv import load_dotenv
load_dotenv()




def send_email(itemlist: list):

    def create_dataframe(itemlist: list):

        data_list = list()

        for item in itemlist:
            item_data = []
            for k in item:
                item_data.append(item[k])
            data_list.append(item_data)


        df = pd.DataFrame(data_list, columns = ['Src_ID','Source','Query', 'Title', 'Price','Post_Type', 'Posted_Time','Location','Distance','Link', 'Description'])
        dtypes = {"Src_ID": "string",\
            "Source": "string",\
            "Query": "string", \
            "Title": "string", \
            "Price": "int32", \
            "Post_Type": "string",\
            "Posted_Time": "datetime64",\
            "Location": "string",\
            "Distance": "int32",\
            "Link": "string", \
            "Description": "string"}
        df = df.astype(dtypes)

        return df

    
    def create_html_message(df: PandasObject):
        
        text = """
        Hello, Friend.
        We found something. Here is your report:
        {table}
        Regards,
        Me"""

        html = """
        <html>
        <head>
        <style> 
        table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
        th, td {{ padding: 5px; }}
        </style>
        </head>
        <body><p>Hello, friend. We found something. Here is your dataframe report:</p>
        <p>Here is your data:</p>
        {table}
        <p>Regards,</p>
        <p>Tom's WebScrape Fun</p>
        </body></html>
        """

        headers = ['Src_ID','Source','Query', 'Title', 'Price','Post_Type', 'Posted_Time','Location','Distance','Link', 'Description']
        text = text.format(table=tabulate(df, headers=headers, tablefmt="grid"))
        html = html.format(table=tabulate(df, headers=headers, tablefmt="html"))
        env = os.environ.get("env")

        message = MIMEMultipart(
        "alternative", None, [MIMEText(text), MIMEText(html,'html')])
        message['Subject'] = f'{env.upper()} - New Items from Project_Webscrape - {datetime.datetime.today().strftime("%Y-%m-%d %I:%M %p")}'

        return message
    
    
    df =  create_dataframe(itemlist)

    message = create_html_message(df)

    # User configuration
    sender_email = os.environ.get('sender_email')
    sender_password = os.environ.get('sender_password')
    receiver_email = os.environ.get('receiver_email')
    
    # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Encrypts the email
    context = ssl.create_default_context()
    server.starttls(context=context)
    # We log in into our Google account
    server.login(sender_email, sender_password)
    # Sending email from sender, to receiver with the email body
    server.sendmail(sender_email, receiver_email, message.as_string())
    
    server.quit()



if __name__ == "__main__":

    # test = read_items()
    # print(test)

    testList = [{'src_id': '7465407650', 'source': 'craigslist', 'query': 'iphone 13 pro max', 'title': 'Iphone 13 Pro Max Unlocked', 'price': 980.0, 'post_type': 'pickup', 'post_time': '2022-03-31 19:18', 'location': 'Wayne', 'distance': 5.2, 'url': 'https://newjersey.craigslist.org/mob/d/wayne-iphone-13-pro-max-unlocked/7465407650.html', 'item_description': None}, {'src_id': '7465048658', 'source': 'craigslist', 'query': 'digital camera', 'title': 'Kodak Pixpro Digital Camera', 'price': 200.0, 'post_type': 'pickup', 'post_time': '2022-03-30 20:50', 'location': 'Morris County', 'distance': 13.3, 'url': 'https://newjersey.craigslist.org/pho/d/randolph-kodak-pixpro-digital-camera/7465048658.html', 'item_description': None}, {'src_id': '699796994483303', 'source': 'fb_marketplace', 'query': 'iphone 13 pro max', 'title': 'Iphone 13 Pro Max 256 UNLOCK ANY CARRIER Devi', 'price': 975.0, 'post_type': 'pickup', 'post_time': '2022-03-29 15:25', 'location': 'Montclair, NJ', 'distance': 10.12, 'url': 'https://www.facebook.com/marketplace/item/699796994483303', 'item_description': ''}, {'src_id': '367591711908867', 'source': 'fb_marketplace', 'query': 'iphone 13 pro max', 'title': 'iphone 13 pro Max Sierra Blue 128GB', 'price': 950.0, 'post_type': 'pickup', 'post_time': '2022-03-30 16:05', 'location': 'Elizabeth, NJ', 'distance': 19.81, 'url': 'https://www.facebook.com/marketplace/item/367591711908867', 'item_description': 'iphone 13 pro Max Sierra Blue 128GB New T Mobile only'}]
    send_email(testList)