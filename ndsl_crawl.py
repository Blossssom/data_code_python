import requests
import urllib
import json
import numpy as np
import pandas as pd

def getPatent(query):
    for i in query:
        file_dir = '/Users/blossom/ndsl' + i + '초록문' + '.csv'
        empty = pd.DataFrame({'abstract':[]})    #({'title':[],'year':[],'title':[],'abstract':[],'author':[],'keyword':[]})
        empty.to_csv(file_dir)

        url_front = "http://openapi.ndsl.kr/itemsearch.do?"
        key = "keyValue=03824157"                       # 인증키
        query = "&query=" + urllib.parse.quote(i)       # 검색어
        print(query)
        target = "&target=JAKO"                         # 검색대상 컨텐츠 ( PATENT=특허전체, KPAT=한국특허전체, KUPA=한국공개특허, KPTN=한국등록특허, KUUM=한국공개실용신안, KUMO=한국등록실용실안,
                                                        #KODE=한국의장등록, UPAT=미국특허전체, USPA=미국등록특허, USAP=미국공개특허, JEPA=일본특허, WOPA=국제특허, EUPA=유럽특허
        search_field = "&searchField=BI"                # 검색대상 항목 ( BI=전체, TI=명칭, PA=출원인, AN=출원번호, AD=출원일자, UN=공개번호, UD=공개일자, RN=등록번호, RD=등록일자, PRAN=우선권번호
                                                        #  PRAD=우선권일자, IPN=국제출원번호, IPD=국제출원일자, IUN=국제공개번호, IUD=국제공개일자, AB=초록, IN=발명자, AG=대리인, IC=IPC분류, UC=USC분류, ID=대표IPC, MC=디자인분류, NULL=쿼리에직접작성
        display_count = "&displayCount=10"              # 검색결과 출력건수 ( Default=10, Max=100)
        start_pos = "&startPosition="                   # 검색시작위치 ( 출력건수*페이지번호, Default=1, Max=100 displayCount가 10인 경우), 숫자는 공란으로 두어야함!
        return_type = "&returnType=json"                # 검색결과 출력형식 (xml, json)
        callback = "&callback=true"                     # 콜백함수 (returnType이 json인 경우 필수)
        res_group = "&responseGroup=advance"
        sort_by = "&sortby="                     # 정렬항목 ( Default=정확도, adate=출원일자, title=명칭, aname=출원인, iname=발명자, anum=출원번호, unum=공개번호, udate=공개일자, mum=등록번호, rdate=등록일자, country=국가, ic=IPC)


        url = url_front + key + target + search_field + display_count + start_pos + sort_by + return_type + res_group + query + callback
        print('url = ',url)
        req = requests.get(url)
        respones = req.text                             # json받아오면서 앞의 true와 괄호 지우기
        parse = respones[5:-1]
        dic = json.loads(parse)
        summary = dic['resultSummary']
        total_count = summary['totalCount']
        start = 0
        count = int(total_count)
        dsp_count = 10
        sol_num = count/dsp_count
        sol_num = int(float(sol_num))
        print(sol_num)
        if count % dsp_count != 0:
            sol_num += 1
        for page_num in range(0, sol_num):
            print("page num = " + str(page_num))
            start = (page_num * dsp_count) + 1
            url = url_front + key + target + search_field + display_count + start_pos + str(start) + sort_by + return_type + res_group + query + callback
            print(url)
            req = requests.get(url)
            respones = req.text
            try:
                dic = json.loads(parse)
            except ValueError:
                print('========== 브레잌 ==========')
                break
            parse = respones[5:-1]
            for info in dic['outputData']:
                #jounal_info = info['journalInfo']
                #year = jounal_info['year']
                article_info = info['articleInfo']
                #title_temp = article_info['articleTitleInfo']
                #title = title_temp['articleTitle']
                abstract_temp = article_info['abstractInfo']
                abstract = abstract_temp[0]
                if isinstance(abstract, list):
                    abstract = 'Null'
                '''author_info = article_info['authorInfo']
                name = ''
                for author_name in author_info:
                    if isinstance(author_name, str):
                        author = author_info
                    else:
                        try:
                            add_name = author_name['#text']
                        except TypeError:
                            continue
                        if name in '':
                            name += add_name
                        else:
                            name += ',' + add_name
                author = name
                keyword = article_info['keyword']
                keyword_type = type(keyword)
                if keyword_type == list:
                    keyword = "Null"
                print('=' * 100)'''
                df = pd.DataFrame(data=np.array([[abstract]]))      #([[year, title, abstract, author, keyword]]))
                df.to_csv(file_dir, sep=',', mode='a', encoding='utf-8', header=False)

if __name__ == '__main__':
    query = ['"교통량"']#['미세먼지', '온실가스', '배기가스', '이산화탄소', '매연', '아황산가스', '교통량', '배출량', '유기화합물']
    #query2 = '대기오염&'
    for i in query:
        #query_fin = [query2+i]
        getPatent(query)