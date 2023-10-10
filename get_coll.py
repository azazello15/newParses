import json

import requests
from bs4 import BeautifulSoup

cookies = {
    'PHPSESSID': 'j8seus9fpalrrvblf3av92dab3',
    'tmr_lvid': '0ada745e082f357fa4977a6b18dfbb8d',
    'tmr_lvidTS': '1696932848784',
    'mgo_sb_migrations': '1418474375998%253D1',
    'mgo_sb_current': 'typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529',
    'mgo_sb_first': 'typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529',
    'mgo_uid': 'hbki0KE6r5ah6sxztbq1',
    'mgo_cnt': '1',
    'mgo_sid': 'ismvs2b5rl110014y47c',
    '_ga': 'GA1.2.1683791222.1696932849',
    '_gid': 'GA1.2.1982451869.1696932849',
    'searchbooster_v2_user_id': '4i-MlAMt4xeK5hotrGHUN_DP8rPUbFYANW0KK_D_p8R%7C9.10.13.14',
    'ageCheckPopupRedirectUrl': '%2Fv2-mount-input',
    '_ym_uid': '1696932852897569826',
    '_ym_d': '1696932852',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'roistat_visit': '6586565',
    'roistat_first_visit': '6586565',
    'roistat_visit_cookie_expire': '1209600',
    'roistat_is_need_listen_requests': '0',
    'roistat_is_save_data_in_cookie': '1',
    'roistat_cookies_to_resave': 'roistat_ab%2Croistat_ab_submit%2Croistat_visit',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    '___dc': '9d984d80-640d-46b5-bc94-1960dab9a653',
    '_gat': '1',
    'mgo_sb_session': 'pgs%253D2%257C%252A%257Ccpg%253Dhttps%253A%252F%252Fbask.ru%252F',
    'UUID': 'f107a8b6-0455-48cf-a67f-9745cccbbab3',
    'mindboxDeviceUUID': '4276b443-6fd1-4482-8fb4-ea5b3280d0ee',
    'directCrm-session': '%7B%22deviceGuid%22%3A%224276b443-6fd1-4482-8fb4-ea5b3280d0ee%22%7D',
    'tmr_detect': '0%7C1696932915548',
    '_ga_4WQKB7JFT7': 'GS1.2.1696932851.1.1.1696932927.46.0.0',
}

headers = {
    'authority': 'bask.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'PHPSESSID=j8seus9fpalrrvblf3av92dab3; tmr_lvid=0ada745e082f357fa4977a6b18dfbb8d; tmr_lvidTS=1696932848784; mgo_sb_migrations=1418474375998%253D1; mgo_sb_current=typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529; mgo_sb_first=typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529; mgo_uid=hbki0KE6r5ah6sxztbq1; mgo_cnt=1; mgo_sid=ismvs2b5rl110014y47c; _ga=GA1.2.1683791222.1696932849; _gid=GA1.2.1982451869.1696932849; searchbooster_v2_user_id=4i-MlAMt4xeK5hotrGHUN_DP8rPUbFYANW0KK_D_p8R%7C9.10.13.14; ageCheckPopupRedirectUrl=%2Fv2-mount-input; _ym_uid=1696932852897569826; _ym_d=1696932852; _ym_isad=2; _ym_visorc=w; roistat_visit=6586565; roistat_first_visit=6586565; roistat_visit_cookie_expire=1209600; roistat_is_need_listen_requests=0; roistat_is_save_data_in_cookie=1; roistat_cookies_to_resave=roistat_ab%2Croistat_ab_submit%2Croistat_visit; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; ___dc=9d984d80-640d-46b5-bc94-1960dab9a653; _gat=1; mgo_sb_session=pgs%253D2%257C%252A%257Ccpg%253Dhttps%253A%252F%252Fbask.ru%252F; UUID=f107a8b6-0455-48cf-a67f-9745cccbbab3; mindboxDeviceUUID=4276b443-6fd1-4482-8fb4-ea5b3280d0ee; directCrm-session=%7B%22deviceGuid%22%3A%224276b443-6fd1-4482-8fb4-ea5b3280d0ee%22%7D; tmr_detect=0%7C1696932915548; _ga_4WQKB7JFT7=GS1.2.1696932851.1.1.1696932927.46.0.0',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}


def get_collections(url):
    response = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    collection_items = soup.find_all('a', class_='collections__item')
    collection_url_list = []
    names_list = []
    data_collection = []

    count = 0
    for col_link in collection_items:
        collection_url = 'https://bask.ru' + col_link.get('href')
        link_name = col_link.text
        names_list.append(link_name)
        collection_url_list.append(collection_url)
        link_dict = {
            'Название коллекции': link_name,
            'URL коллекции': collection_url,
        }
        for url in collection_url_list:
            r = requests.get(url)
            s = BeautifulSoup(r.text, 'lxml')
            item_links = s.find_all('a', class_='card')
            col_link_list = []
            for item_link in item_links:
                try:
                    card_link = 'https://bask.ru' + item_link.get("href")
                    col_link_list.append(card_link)
                except Exception as ex:
                    card_link = None
                try:
                    card_name = item_link.find('div', class_='card-title').text
                except Exception as ex:
                    card_name = None
                try:
                    card_text = item_link.find('div', class_='card-text').text
                except Exception as ex:
                    card_text = None
                try:
                    card_price = item_link.find('div', class_='card-price').text
                except Exception as ex:
                    card_price = None

                for u in col_link_list:
                    res = requests.get(u)
                    bs = BeautifulSoup(res.text, 'lxml')
                    try:
                        name = bs.find('div', class_='p-block__name h3').text
                    except Exception as ex:
                        name = None
                    try:
                        article = bs.find('div', class_='p-block__art').text
                    except Exception as ex:
                        article = None
                    try:
                        price = bs.find('span', class_='avail-b').find('span').text
                    except Exception as ex:
                        price = None
                    try:
                        credit = bs.find('span', class_='avail-b').find('div', class_='credit-block').text
                    except Exception as ex:
                        credit = None
                    try:
                        description = bs.find('div', class_='description-text').text
                    except Exception as ex:
                        description = None
                    card_item_dict = {
                        'Название': name,
                        'Артикул': article,
                        'Цена': price,
                        'Рассрочка': credit,
                        'Полное описание': description,
                    }
                    items_dict = {
                        'Коллекция': link_dict,
                        'Ссылка на товар': card_link,
                        'Название товара': card_name,
                        'Краткое описание': card_text,
                        'Цена': card_price,
                        'Полная информация': card_item_dict
                    }
                    data_collection.append(items_dict)
                print(data_collection)
                count += 1
                print(count)
    with open('items_collection.json', 'w', encoding='utf-8') as f:
        json.dump(data_collection, f, ensure_ascii=False, indent=4)


def main():
    get_collections('https://bask.ru/')


if __name__ == '__main__':
    main()
