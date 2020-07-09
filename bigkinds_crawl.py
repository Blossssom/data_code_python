#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import time


headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
           'Connection': 'keep-alive',
           'Content-Type': 'application/json;charset=UTF-8',
           'Cookie': '_ga=GA1.3.979412710.1589275883; Bigkinds=F4682561DF4DF94181A26D3A61805756; _gid=GA1.3.911838880.1590646896; _gat=1',
           'Host': 'www.bigkinds.or.kr',
           'Origin': 'https://www.bigkinds.or.kr',
           'Referer': 'https://www.bigkinds.or.kr/v2/news/search.do',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}

def get_news_id(word, s_date, e_date):
    global news_id_li
    news_id_li = []
    key_word = '"' + word + '"'
    start_date = '"' + s_date + '"'
    end_date = '"' + e_date + '"'
    print(word, start_date, end_date)
    url = "https://www.bigkinds.or.kr/api/news/search.do"
    params = '''{"indexName": "news", "searchKey": %s, "searchKeys": [{}], "byLine": "", "searchFilterType": "1", "searchScopeType": "1", "mainTodayPersonYn": "", "startDate": %s, "endDate": %s, "newsIds": [], "categoryCodes": [], "incidentCodes": [], "networkNodeType": "", "topicOrigin": "", "startNo": "1", "resultNumber": "1"}''' %(key_word, start_date, end_date)
    req = requests.post(url, data = json.dumps(eval(params)), headers = headers)
    sol = req.json()
    t_count =  '"' + str(sol['totalCount']) + '"'
    go_params = '''{"indexName": "news", "searchKey": %s, "searchKeys": [{}], "byLine": "", "searchFilterType": "1", "searchScopeType": "1", "mainTodayPersonYn": "", "startDate": %s, "endDate": %s, "newsIds": [], "categoryCodes": [], "incidentCodes": [], "networkNodeType": "", "topicOrigin": "", "startNo": "1", "resultNumber": %s}''' %(key_word, start_date, end_date, t_count)
    go_req = requests.post(url, data = json.dumps(eval(go_params)), headers = headers)
    go_sol = go_req.json()

    for tag in go_sol['resultList']:
        news_id = tag['NEWS_ID']
        news_id_li.append(news_id)

def crawl(the_list):
    print('crawl start')
    fin_li = []
    for n_id in the_list:
        try:
            content_dict = {}
            cl_url = "https://www.bigkinds.or.kr/news/detailView.do?docId=%s&returnCnt=1&sectionDiv=1000" %n_id
            cl_req = requests.get(cl_url, headers = headers)
            json_cl = cl_req.json()
            #print(json_cl)
            content_dict['id'] = n_id
            content_dict['date'] = json_cl['detail']['DATE']
            content_dict['category'] = json_cl['detail']['CATEGORY_CODE']
            content_dict['category_main'] = json_cl['detail']['CATEGORY_MAIN']
            content_dict['title'] = json_cl['detail']['TITLE']
            content_dict['content'] = json_cl['detail']['CONTENT']
            fin_li.append(content_dict)
            #print(fin_li)
        except:
            print('error')
            print('start sleep')
            time.sleep(100)
            break
            print('let`s go')
        print(*fin_li, sep='\n')
    file_name = str(word)+'.csv'
    with open(file_name, 'a', encoding='utf-8') as sf:
        for save_csv in fin_li:
            sf.write(str(save_csv) + '\n')
    #print(*fin_li, sep='\n')


word = str(input('검색 : '))
s_date = str(input('start_date ( ex) 2020-02-01 ) : '))
e_date = str(input('end_date ( ex) 2020-02-15 ) : '))
get_news_id(word, s_date, e_date)
crawl(news_id_li)



'''for word in word_li:
    year = 2016
    for t_year in range(10):
        month = 12
        for k in range(12):
            if k == 11:
                e_year = str(year)
                s_year = str(year - 1)
                e_month = str(month).zfill(2)
                s_month = '12'
                get_news_id(word, s_year, e_year, s_month, e_month)
                crawl(news_id_li)
            else:
                e_month = str(month).zfill(2)
                s_month = str(month-1).zfill(2)
                e_year = str(year)
                s_year = str(year)
                get_news_id(word, s_year, e_year, s_month, e_month)
                crawl(news_id_li)

            month -= 1
            time.sleep(5)
        year -= 1
        time.sleep(60)'''




