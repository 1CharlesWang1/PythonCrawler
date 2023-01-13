import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm

class CoronaVirusSpider(object):
    def __init__(self):
        self.home_url='https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self,url):
        #根据URL获取相应内容的字符串
        response= requests.get(url)
        return response.content.decode()

    def parse_home_page(self,home_page,tag_id):
        #解析首页内容,获取解析后的Python数据
        soup=BeautifulSoup(home_page,'lxml')
        script=soup.find(id=tag_id)
        text=script.text
        json_str=re.findall(r'(\[.*\])',text)[0]
        #格式转换
        data=json.loads(json_str)
        return data

    def save(self,data,path):
        #以json格式保存,最近一日疫情数据
        with open(path,'w')as fp:
            json.dump(data,fp,ensure_ascii=False)

    def crawl_last_day_data_of_China(self):
        #采集近一天各国疫情信息
        home_page=self.get_content_from_url(self.home_url)
        crawl_last_day_data_of_China=self.parse_home_page(home_page,tag_id='getAreaStat')
        self.save(crawl_last_day_data_of_China, 'E:\wcl\PythonCrawler\data\crawl_last_day_data_of_China.json')

    def crawl_recent_data_of_China(self):
        with open('E:\wcl\PythonCrawler\data\crawl_last_day_data_of_China.json') as fp:
            last_day_data_of_China=json.load(fp)
        corona_virus=[]
        for province in tqdm (last_day_data_of_China,'采集各省疫情信息'):
            statistics_data_url=province['statisticsData']
            statistics_data_json_str=self.get_content_from_url(statistics_data_url)
            statistics_data=json.loads(statistics_data_json_str)['data']
            for one_day in statistics_data:
                one_day['provinceName']=province['provinceName']
            corona_virus.extend(statistics_data)
        self.save(corona_virus, 'E:\wcl\PythonCrawler\data\crawl_recent_data_of_China.json')

    def run(self):
        self.crawl_last_day_data_of_China()
        self.crawl_recent_data_of_China()


if __name__ == '__main__':
    spider=CoronaVirusSpider()
    spider.run()




