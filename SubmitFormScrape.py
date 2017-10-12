
import requests
from bs4 import BeautifulSoup
import csv
# import pandas as pd

# Enter data and submit form

url = 'http://website.com'

session = requests.session()

r = session.get(url)

payload = {'Field1' : 'text',
'Field2' : 'text2' ,
'Field3' : 'text3'}

r = session.post(url, data=payload)
with open("./address.abcd", "w") as f:
	f.write(r.content)

soup = BeautifulSoup(r.content, 'lxml') # Parse the HTML as a string

data = []

parsed_data = [data]

table = soup.find_all('table')[0] # Grab the first table
table_body = table.find('tbody')

# Convert Table to rows
rows = table.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    cols = [ele.text.strip() for ele in cols]
    parsed_data.append([ele for ele in cols if ele])

#    	for td in cols:
#        text = td.find(text=True) + ","
#       print text,
#    print

# Write as csv
with open("C:\\Users\\user.one\\result_file.csv", "wb") as resultFile:
	wr = csv.writer(resultFile, dialect="excel", delimiter=",")
	wr.writerows(parsed_data)