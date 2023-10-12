import json
import time

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
    session = requests.Session()
    response = session.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.content, 'lxml')
    collection_links = soup.find_all('a', class_='collections__item')
    collection_links_list = []
    for links in collection_links:
        collection_links_list.append('https://bask.ru' + links.get('href'))
        for collection_item in collection_links_list:
            response = session.get(collection_item)
            soup = BeautifulSoup(response.content, 'lxml')
            item_urls = soup.find_all('a', class_='card')
            item_urls_list = []
            for item_url in item_urls:
                iu = 'https://bask.ru' + item_url.get('href')
                item_urls_list.append(iu)

            with open('urls.txt', 'w', encoding='utf-8') as file:
                for url in item_urls_list:
                    file.write(f'{url}\n')


def get_collections_data(file_path):
    with open(file_path) as file:
        url_list = [line.strip() for line in file.readlines()]

    session = requests.Session()
    data = []
    for url in url_list:
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find('h1', class_='p-block__name sm-hidden h3').text
        article = soup.find('span', class_='art').text
        price = soup.find('meta', attrs={'itemprop': 'price'}).get('content')
        credit = soup.find('div', class_='credit-block').text
        images = soup.find_all('img', class_='object-fit-cover')
        images_list = []
        for i in images:
            image = 'https://bask.ru' + i.get('src')
            images_list.append(image)
        description = soup.find('div', class_='description-text').text
        try:
            features = soup.find('ul', class_='list').find_all('li')
            features_list = []
            for feat in features:
                features_list.append(feat.text)
        except Exception as ex:
            features_list = None
        data.append(
            {
                'title': title,
                'link': url,
                'article': article,
                'price': price,
                'credit': credit,
                'images': images_list,
                'description': description,
                'features': features_list
            }
        )
        with open('items_collection.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    # print(get_collections('https://bask.ru/'))
    get_collections_data('urls.txt')


if __name__ == '__main__':
    main()
