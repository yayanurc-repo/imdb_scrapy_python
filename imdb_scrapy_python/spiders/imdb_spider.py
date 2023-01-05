# text cleaning
import re

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/search/title/?groups=top_1000&adult=include&sort=user_rating,desc']

    def parse(self, response):
        # Extract film data
        for film in response.css('div.lister-item'):
            year = film.css('.lister-item-year::text').get()
            try:
                year = int(year.strip('()'))
            except ValueError:
                year = int(year.strip('(I)').strip('(II)').replace(' (', ''))
            year = str(year)

            yield {
                'name': film.css('h3 a::text').get(),
                'year': year,
                'stars': film.css('.ratings-imdb-rating strong::text').get(),
                'rank': film.css('.lister-item-index::text').get().strip('.'),
                'duration': film.css('.runtime::text').get(),
                'genre': film.css('.genre::text').get().strip(),
                'director': film.css("p:contains('Director') a::text").get(),
                'synopsis': self.__remove_html_tags__(
                    film.css('.ratings-bar + p').get()
                ),
            }

        # Follow pagination links
        next_page = response.css('a.lister-page-next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def __remove_html_tags__(self, text):
        """remove html tags from string"""
        html_tags = re.compile('<.*?>')
        return re.sub(html_tags, '', text).strip('\n')