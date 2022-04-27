# Scrapy settings for my_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'my_scrapy'  # 项目名

SPIDER_MODULES = ['my_scrapy.spiders']
NEWSPIDER_MODULE = 'my_scrapy.spiders'

FEED_EXPORT_ENCODING='utf-8'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'my_scrapy (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 是否遵守 机器人协议。默认为True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32  # 最大并发数，同时允许开启多少个爬虫线程

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3  # 下载延迟时间，单位是秒，控制爬虫爬取的速率
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False  # 是否保存 cookies，开机可以记录爬取的过程，非常好用的一个参数

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}  # 默认请求头，上面写了个 USER-AGENT，其实这个东西就是放在请求头里面的，这个东西可以根据你爬取的内容做相应的设置

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'my_scrapy.middlewares.MyScrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'my_scrapy.middlewares.MyScrapyDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'my_scrapy.pipelines.MyScrapyPipeline': 300,
}  # 项目管道，300为优先级，越低越爬取的优先度越高，

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 可以设置日志的等级与日志存放的路径
# 相关变量
# LOG_LEVEL = ""
# LOG_FILE = "日志名.log"
# 日志等级
# 1. DEBUG 调试信息
# 2. INFO 一般信息
# 3. WARNING 警告
# 4. ERROR 普通错误
# 5. CRITICAL 严重错误
# 如果设置 LOG_LEVEL = "WARNING"，就只会 WARNING 等级之下的 ERROR和CRITICAL
# 默认等级是 1


