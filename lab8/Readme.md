# Жич: Энэхүү код нь зөвхөн хичээлийн агуулгын зорилготой тул дата авсан сайт болон urls-ийг үндсэн кодноос хасав!
# Ашигласан материайл:
https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3

# 1. Шаардлагатай сан суулгах

pip install -r requirements.txt

# 2. url crawler

scrapy runspider url_finder.py

# 3. text crawler

scrapy runspider scraper.py
