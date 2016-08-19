#coding: utf-8

import scrapy
import time

lista_url = []
arquivo = open("posts.txt", "w+")

class DmozSpider(scrapy.Spider):
    DOWNLOAD_DELAY = 1 # seconds
    arquivo_post = open("algorithm-general-posts.txt", "r")
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    lista_posts = []
    for i in arquivo_post:
        lista_posts.append(i.strip())
    start_urls = lista_posts

    def parse(self, response):
        for sel in response.xpath('//table[@class="rtTable"]//tr//td[@class="rtThreadCellWrap"]'):
            self.DOWNLOAD_DELAY = 1
            link = sel.xpath('a[1]/@href').extract()
            #Remover caracter 'u' da lista
            link = [x.encode('utf-8') for x in link]
            head = 'http://apps.topcoder.com/forums/'
            link_with_head = [head + x for x in link]
            link_with_head2 = ''.join(link_with_head)
            arquivo.write("%s\n" % link_with_head2)
