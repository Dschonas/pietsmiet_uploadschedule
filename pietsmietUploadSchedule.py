from bs4 import BeautifulSoup
from datetime import timedelta
import urllib3, sys, datetime

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

def correctDate(amountDays):
	global today, date, urlUploadTodayDate, title
	today = datetime.date.today()-timedelta(days=amountDays)
	date = "{:%d-%m-%Y}".format(today)
	urlUploadTodayDate = urlUploadToday+date
	title = "Upload-Plan am {:%d.%m.%Y}:".format(today)

def checkArguments():
	if(argumentLen < 2):
		outputUploadPlan()
	elif (argumentLen >= 2):
		if (argument[1] in("yesterday", "y")):
			correctDate(1)
			outputUploadPlan()

def outputUploadPlan():
	try:
		print (getList())
	except Exception as e:
		print ("No Upload-Plan yet...")

def getList():
	sp = getSoupOf(getUrlContent(getUrlUploadPlan())).prettify()
	start = sp.find(title)
	end = len(sp)-sp.find(endQuote)
	return getSoupOf(sp[start:-end]).get_text()

def getUrlContent(url):
	http = urllib3.PoolManager()
	req = http.request('GET', url)
	return req.data

def getSoupOf(urlContent):
	return BeautifulSoup(urlContent, 'html.parser')

def getUrlUploadPlan():
	for link in getSoupOf(getUrlContent(baseUrl)).find_all('a'):
		if "readmore-link" in str(link.get('class')) and urlUploadTodayDate in str(link.get('href')):
			return baseUrl[0:-index]+link.get('href')

if __name__ == '__main__':
	checkArguments()