import os

from dotenv import load_dotenv
load_dotenv()

def preloader_req_details(item: str):

    item_formatted = item.replace(' ', '%2520')

    url = 'https://www.facebook.com/ajax/route-definition/'

    # payload=f'client_previous_actor_id=100077957444098&\
    # route_url=%2Fmarketplace%2F103675689671038%2Fsearch%2F%3Fquery%3D{item_formatted}&\
    # routing_namespace=fb_comet&\
    # __user=100077957444098&\
    # __a=1&\
    # __dyn=7AzHK4HwkEng5KbxG4VuC0BVU98nwgU7SbgS3q2ibwNw9G2S7o762S1DwUx609vCxS320om782Cwwwqo465o-cw5MKdwGwQw9m8wsU9kbxS1Fwc61axe3S68f85qfK6E7e58jwGzE7W7oqBwJK2W5olwUwgojUlDw-wUws9ovUaU3VBwJCwLyESE2KwkQq0xoc84K2e&\
    # __csr=gF6Fn9mzgx8BQW6FPOk-Bt8kAzkmDjQgxd4hvETR_iZTlBrgxaBnAhbQKCaBAWmdKcGmcKlbKiaBoCSWDx92QfAxWfAyVEG4A9iggz-gwGA3i48hmuiXyGwhUuHzUkwFgbEWq1JxK9xu9AG0R98pwh89-i5po7K3C2K0Eof82Zwm84GcwkUeE66321YwAK18w8S0gu0GU2bw2fU0nCg03cSxi46micw0Gbw0l0ES039q6EdU1sUdqx-1Mg0_20lK&\
    # __req=s&\
    # __hs=19115.HYP%3Acomet_pkg.2.1.0.2.&\
    # dpr=1&\
    # __ccg=EXCELLENT&\
    # __rev=1005444505&\
    # __s=nufs72%3A8txo3e%3Am5ql8a&\
    # __hsi=7093652700381737707-0&\
    # __comet_req=1&\
    # fb_dtsg=AQGjnBHuZPJ-YJQ%3A48%3A1649072784&\
    # jazoest=21973&\
    # lsd=ffUNZgbzj9EEqu5l7MrpzM&\
    # __spin_r=1005444505&\
    # __spin_b=trunk&\
    # __spin_t=1651619724'

    payload='client_previous_actor_id=100077957444098&route_url=%2Fmarketplace%2F103675689671038%2Fsearch%2F%3Fquery%3Diphone%252013&routing_namespace=fb_comet&__user=100077957444098&__a=1&__dyn=7AzHK4HwkEng5KbxG4VuC0BVU98nwgU7SbgS3q2ibwNw9G2S7o762S1DwUx60gu0luq7oc81xoswaq221FwgolzUO0n2US2G3i0Boy1PwBgK7o884y0Mo4G4UfoowYwlE-UqwsUkxe2GewGwkUtxGm2SUbElxm3y3aexfxmu3W3y1MBx_wHwfCm2Sq2-azqwaW1jhE25wMwiU8U&__csr=gllbnEWYhOQxsAy6il5EWqbpcyPr9GxLZ9vAXyqWEBeBisSLjpKq8ICl4BFWrJoyv-4pbhCUlx28gOC8Czk4-V9VEKeKl7yK5XGaze-545oycAGmuueAgeUoKqi698hoGchVUqwtUau4k36aGqq9xW1yG8wNz8S2zxm4E9E8A6Uqxi2q3q1Gwootwko4S10z87R0oU7u6E4yewk8eUaE-1axG2ufw9q0ZA08Iw38o0Bq015Uym0594U02e6o1HQ040o0cT69z8dUaE5m03cJ0iE5Ra0sO05J80Ze09YjF0no&__req=10&__hs=19118.HYP%3Acomet_pkg.2.1.0.2.&dpr=1&__ccg=EXCELLENT&__rev=1005466579&__s=vp4rp4%3Axsae9p%3Aexawex&__hsi=7094648204719588714-0&__comet_req=1&fb_dtsg=AQGgwWT8udDRoO4%3A9%3A1651841504&jazoest=21963&lsd=1SimanNrOP_v69G2uelmjK&__spin_r=1005466579&__spin_b=trunk&__spin_t=1651851508'

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    #     'Accept': '*/*',
    #     'Accept-Language': 'en-US,en;q=0.5',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'X-FB-LSD': 'ffUNZgbzj9EEqu5l7MrpzM',
    #     'Origin': 'https://www.facebook.com',
    #     'Connection': 'keep-alive',
    #     'Referer': 'https://www.facebook.com/marketplace/103675689671038',
    #     'Cookie': f'{os.environ.get("fb_cookie")}',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'Pragma': 'no-cache',
    #     'Cache-Control': 'no-cache',
    #     'TE': 'trailers'
    # }

    headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'sb=lxl1YktUNBFzDOGzLWZzuu6L; wd=996x616; datr=lxl1Yp56WP3neEND2wOX9m-O; c_user=100077957444098; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1651851516905%2C%22v%22%3A1%7D; xs=9%3ACKtrbNP9GuZMYA%3A2%3A1651841504%3A-1%3A7312%3A%3AAcVm8NTcZfWSkspH8p5sp5swcW0-y19OEZFE1bppuQ; fr=0uxKrYiUdVqxvDGtM.AWXz3u3u5H9l6yDyhI9JZdSSDAk.BidUEL.e3.AAA.0.0.BidUEL.AWVH3UMFXjw; c_user=100077957444098; fr=00vXq7Zv6Y9IapuFq.AWWqqdAZ3MfI2_bY9FQ6xKTxE0U.BidUmv.e3.AAA.0.0.BidUmv.AWWMihbTVOA; xs=9%3ACKtrbNP9GuZMYA%3A2%3A1651841504%3A-1%3A7312%3A%3AAcVkAW4CVijJNndhsPLOL7SOU96283OolpTKuUc_Yg',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/marketplace/103675689671038',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'viewport-width': '318',
    'x-fb-lsd': '1SimanNrOP_v69G2uelmjK'
    }


    return url, payload, headers


if __name__ == "__main__":
    import httpx

    preloader_req_details = preloader_req_details('iphone 13')

    preloader_api_response = httpx.post(
        url=preloader_req_details[0], 
        data=preloader_req_details[1], 
        headers=preloader_req_details[2], 
        follow_redirects=False
        )
    
    print(preloader_api_response.text)