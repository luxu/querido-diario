from scrapy import cmdline

# city = 'sp_franca -a start_date=2020-11-01'
city = 'sp_assis'

cmdline.execute(f"scrapy crawl {city}".split())
