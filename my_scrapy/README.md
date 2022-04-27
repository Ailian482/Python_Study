### spiders 目录，爬虫的代码都放在这里面
```bash
my_scrapy/my_scrapy 是整个项目的主菜

items.py：要抓取的字段
middlewares.py：中间件
pipelines.py：管道文件
settings.py：设置文件

先将项目跑起来
    1. 进入spider目录里面， 创建一个 baidu 爬虫
    cd my_scrapy/my_scrapy
    scrapy genspider baidu "baidu.com"
    运行上面两行命令后，会自动在当前目录下创建一个spider项目，文件包括 spider/baidu.py 里面有内容
        先导入了 scrapy，定义了一个 BaiduSpider 类，必须要继承 scrapy.Spider。里面有三个属性（name、allowed_domains、start_urls）
        name：爬虫的名字，运行爬虫的时候就是看这个名字
        allowed_domains：要抓取的域名限制，这是我们刚才在命令行输入的，要抓百度，当然就要限制在百度内，别抓到京东去了，先不跨界
        start_urls：要抓取的 url 列表，类型 list
        
        parse函数，抓取后的动作，可以自己定义

```
