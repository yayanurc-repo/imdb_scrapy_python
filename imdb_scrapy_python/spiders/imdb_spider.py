import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/search/title/?groups=top_1000&adult=include&sort=user_rating,desc']

    def parse(self, response):
        # Extract film data
        for film in response.css('div.lister-item'):
            yield {
                'name': film.css('h3 a::text').get(),
                'year': film.css('h3 span.lister-item-year::text').get(),
                'stars': film.css('p.text-muted span.certificate::text').get(),
                'rank': film.css('div.lister-item-index::text').get(),
                'duration': film.css('p.text-muted span.runtime::text').get(),
                'genre': film.css('p.text-muted span.genre::text').get(),
                'director': film.css('p.text-muted span.credit::text').get(),
                'synopsis': film.css('p.text-muted span.plot::text').get(),
            }