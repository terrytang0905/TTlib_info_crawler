# -*- coding: utf-8 -*-

# Scrapy settings for babaSR project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'babaSR'

SPIDER_MODULES = ['babaSR.spiders']
NEWSPIDER_MODULE = 'babaSR.spiders'


ITEM_PIPELINES = ['babaSR.csvpipelines.CsvPipeline']
#ITEM_PIPELINES = ['babaSR.filepipelines.FilePipeline']
# ITEM_PIPELINES = ['babaSR.mysqlpipelines.MySQLPipeline']
# DB_SERVER="127.0.0.1"
# DB_PORT=3306
# DB_USERNAME="tt"
# DB_PASSWORD="tt2015"
# DB_NAME="investment"

# ITEM_PIPELINES = ['babaSR.mongopipelines.MongoDBPipeline']
# MONGODB_SERVER = "127.0.0.1"
# MONGODB_PORT = 10001
# MONGODB_USERNAME = "invest"
# MONGODB_PASSWORD = "mac2015"
# MONGODB_DB = "investment"
# MONGODB_COLLECTION = "startup"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'babaSR (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

LOG_ENABLED = True
LOG_LEVEL = 'INFO'