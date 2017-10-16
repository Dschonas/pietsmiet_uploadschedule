from bs4 import BeautifulSoup
from datetime import timedelta
import urllib2, sys, datetime

# static fields
hdrs = {'User-Agent' : 'Magic Browser'}
baseUrl = "http://www.pietsmiet.de/news/uploadplan"
urlUploadToday = "-upload-plan-am-"
index = len(baseUrl)-baseUrl.index("/news/uploadplan")
endQuote = "Alle Ang"

# changing fields
today = datetime.date.today()
date = "{:%d-%m-%Y}".format(today)
urlUploadTodayDate = urlUploadToday+date
title = "Upload-Plan am {:%d.%m.%Y}:".format(today)

# command line arguments
argument = sys.argv
argumentLen = len(sys.argv)

def getUrlContent(url):
	req = urllib2.Request(url, headers=hdrs)
	read = urllib2.urlopen(req)
	return read.read()


if __name__ == '__main__':
	print getUrlContent(baseUrl)