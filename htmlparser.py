from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import urllib.request as urllib2

class parser(object):
    def get_new_urls(self, page_url, soup):
        newurls = set()
        links = soup.div.find_all('a',href=re.compile(r'/videos/'))
        for link in links:
            new_url = link['href']
            print(link)
            new_full_url = urljoin(page_url,new_url)
            newurls.add(new_full_url)
            return newurls

    # < dd class ="lemmaWgt-lemmaTitle-title" >
    def get_new_data(self, page_url, soup):
        res_data = {}
        res_data['urls'] = page_url
        title_node = soup.find('a',class_='kt_imgrc bbb')
        res_data['title'] = title_node['title']
        return res_data

    def parse(self, page_url, htmlcont):
        if page_url is None or htmlcont is None:
            return
        soup = BeautifulSoup(htmlcont, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(page_url, soup)
        new_datas = self.get_new_data(page_url, soup)
        return new_urls, new_datas