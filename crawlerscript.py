from icheckgames.crawler import *
crawlobj = PlatformCrawler()
crawlobj.crawl.apply_async([crawlobj])
