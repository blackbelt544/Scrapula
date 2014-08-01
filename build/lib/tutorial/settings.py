# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Googlebot'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
USER_AGENT = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
# ITEM_PIPELINES = { 'tutorial.pipelines.JsonExportPipeline': 200}
# DOWNLOADER_MIDDLEWARE = [ 'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware']
COOKIES_DEBUG=True
AUTO_THROTTLE_ENABLED = True
AUTO_THROTTLE_DEBUG = True
RANDOMIZE_DONWLOAD_DELAY = True
AUTO_THROTTLE_DELAY = 5
CONCURRENT_REQUESTS = 5


def overrides():
    return None