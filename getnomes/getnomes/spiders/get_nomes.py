#coding: utf-8

import scrapy
import time

lista_nomes = []
nomes = []

arquivo = open("nomes.txt", "w+")

class DmozSpider(scrapy.Spider):
    DOWNLOAD_DELAY = 0.8 # seconds
    arquivo_post = open("posts.txt", "r")
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    lista_posts = []
    for i in arquivo_post:
        lista_posts.append(i)
    start_urls = lista_posts


    def parse(self, response):
        list_final_nomes = []
        for sel in response.xpath('//table[@class="rtTable rtTablePost"]//tr//td[@class="rtPosterCell"]//div[@class="rtPosterSpacer"]//span[@class="bodyText"]/a/text()'):
            self.DOWNLOAD_DELAY = 0.8
            list_nomes = sel.extract()
            list_nomes = list_nomes.split('\n')
            for nome in list_nomes:
                list_final_nomes.append(nome.encode('utf-8'))
        arquivo.write(str(list_final_nomes))
        arquivo.write("\n")