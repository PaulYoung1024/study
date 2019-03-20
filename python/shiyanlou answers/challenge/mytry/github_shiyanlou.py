# -*- coding:utf-8 -*-
import scrapy
class GithubSpider(scrapy.Spider):
    name='shiyanlou-github'
    @property
    def start_urls(self):
        return('https://github.com/shiyanlou?tab=repositories', )
    def parse(self,response):
        for repository in response.css('li.public'):
            yield{
                    'name':repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
                    'update_time':repository.xpath('.//relative-time/@datetime').extract_first()
                    }
            spans=response.css('div.pagination span.disabled::text')
			# 如果 Next 按钮没被禁用，那么表示有下一页
            if len(spans)==0 or spans[-1].extract()!='Next':
                next_url=response.css('div.pagination a:last-child::attr(href)').extract_first()
                yield response.follow(next_url,callback=self.parse)