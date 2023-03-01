import requests
from bs4 import BeautifulSoup as bs

url = "https://www.iban.com/currency-codes"

def get_database():
  r=requests.get(url)
  #print(r.status_code) '-> 200:OK
  source_code=r.text
  soup=bs(source_code,'html.parser')
  
  list=[]
  database=[]
  index=int(1)
  
  table=soup.find('table',attrs={'class':'table table-bordered downloads tablesorter'})
  t_body=table.find('tbody')
  rows=t_body.find_all('tr')

  for row in rows:
    columns=row.find_all('td')
    columns=[element.text.strip() for element in columns]
    list.append([element for element in columns])
  #print(list) '-> OK
  for data in list:
    if data[0]=='':
      data[0]='N/A'
    if data[1]=='':
      data[1]='N/A'
    if data[2]=='':
      data[2]='N/A'
    if data[3]=='':
      data[3]='N/A'
    currency={
      'ID':str(index),
      'Country':data[0].title(),
      'Currency':data[1],
      'Code':data[2],
      'Number':str(data[3])
    }
    database.append(currency)
    index+=1
  return database