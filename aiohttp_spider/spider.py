import aiohttp
import asyncio
import logging
from fake_useragent import UserAgent
from lxml import etree
import openpyxl
from datetime import datetime

# 日志输出的基本配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['品名', '最新报价', '单位', '报价数', '报价时间'])
start = datetime.now()


class Spider(object):
    def __init__(self):
        # self.semaphore = asyncio.Semaphore(6)  # 信号量，有时候需要控制协程数，防止爬的过快被反爬
        self.header = {
            "Accept-Encoding": "gzip",  # 使用gzip压缩传输数据让访问更快
            "User-Agent": ua.random
        }

    async def scrape(self, url):
        # async with self.semaphore:  # 设置最大信号量，有时候需要控制协程数，防止爬的过快被反爬
        session = aiohttp.ClientSession(headers=self.header, connector=aiohttp.TCPConnector(ssl=False))
        response = await session.get(url)
        result = await response.text()
        await session.close()
        return result

    async def scrape_index(self, page):
        url = f'https://www.zhongnongwang.com/quote/product-htm-page-{page}.html'
        text = await self.scrape(url)
        await self.parse(text)

    async def parse(self, text):
        # Xpath定位提取数据
        html = etree.HTML(text)
        items = html.xpath('/html/body/div[10]/table/tr[@align="center"]')
        logging.info(f'该页有多少条信息：{len(items)}')  # 一页有20条信息
        # 遍历提取出数据
        for item in items:
            name = ''.join(item.xpath('.//td[1]/a/text()'))  # 品名
            price = ''.join(item.xpath('.//td[3]/text()'))  # 最新报价
            unit = ''.join(item.xpath('.//td[4]/text()'))  # 单位
            nums = ''.join(item.xpath('.//td[5]/text()'))  # 报价数
            time_ = ''.join(item.xpath('.//td[6]/text()'))  # 报价时间
            sheet.append([name, price, unit, nums, time_])
            logging.info([name, price, unit, nums, time_])

    def main(self):
        # 50页的数据
        scrape_index_tasks = [asyncio.ensure_future(self.scrape_index(page)) for page in range(1, 51)]
        loop = asyncio.get_event_loop()
        tasks = asyncio.gather(*scrape_index_tasks)
        loop.run_until_complete(tasks)


if __name__ == '__main__':
    spider = Spider()
    spider.main()
    wb.save('data3.xlsx')
    delta = (datetime.now() - start).total_seconds()
    print("用时：{:.3f}s".format(delta))
