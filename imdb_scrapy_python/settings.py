BOT_NAME = 'imdb_scrapy_python'

SPIDER_MODULES = ['imdb_scrapy_python.spiders']
NEWSPIDER_MODULE = 'imdb_scrapy_python.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'imdb_scrapy_python.middlewares.ImdbScrapyPythonSpiderMiddleware': 543,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'imdb_scrapy_python.pipelines.GoogleSheetsPipeline': 300,
# }