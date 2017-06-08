import urllib2,cookielib
import re
from bs4 import BeautifulSoup
import time
from datetime import datetime,date,timedelta




#Todo :
#	2. Get current stock price and other data
# 	3. Put data into googlefirebase

table = []

def split(text):
	operation = text.split(None,1)[1]
	operation = operation.replace ("with a", ",").replace("of", "").replace("call on ", "").replace("--", ":")
	company = operation.split("target", 1)[0]
	target = re.search('Rs (.*):',operation).group(1)
	#print company,target
	content = {"call": text.split(None,1)[0], "Company": company, "Target":target}
	table.append(content)

def printTable(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] or '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))

# webiste to scrap data from
et = "http://economictimes.indiatimes.com/markets/stocks/recos"
moneycontrol = "http://www.moneycontrol.com/news/stock-advice-261-1-next-0.html"
hdfcsec = "http://www.hdfcsec.com/Share-Market-Research/StockPicks/201106160710148685141"
hdfcfundamendal = "http://www.hdfcsec.com/fundamentalstockpicks/201407171239409261528"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

#retrving data from ET
req = urllib2.Request(et, headers=hdr)

page = urllib2.urlopen(req)
soup = BeautifulSoup(page, "html.parser")

for element in soup.findAll("div", {"class":"eachStory"}):
	
	flag = 0
#print soup.prettify()
	for date in element.findAll("time"):
		date = date.text.replace("IST", " ").strip()
		#print date
		#newdate1 = time.strptime("Jun 7, 2017, 08:49 AM", "%b %d, %Y, %I:%M %p")
		newdate1 = datetime.strptime(date,"%b %d, %Y, %I:%M %p");
		datetime.today().date()
		
		if newdate1.date() != datetime.today().date():
			flag = 1

	if flag == 1:
		break

	for h3 in element.findAll("h3"):
		ip = BeautifulSoup(repr(h3), "html.parser")
		text = ip.get_text()
		pattern = re.compile("Buy|Sell")
	#print text
		if text.find("Buy") == 0 :
			split(text)
		if text.find("Hold") == 0:
			split(text)
		
		if text.find("Accumulate") ==0:
			split(text)

		if text.find("Sell") ==0:
			split(text)
		


#Getting data from HDFC



#printing the result
printTable(table)


