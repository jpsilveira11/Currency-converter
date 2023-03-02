import requests
from bs4 import BeautifulSoup as bs
from babel.numbers import format_currency

urls={
  'currencies':'https://wise.com/gb/currency-converter/currencies/',
  'converter':'https://wise.com/gb/currency-converter/'
}
def get_currencies():
  currencies=[]
  index=int(1)
  r=requests.get(urls['currencies'])
  #print(r.status_code) '-> 200:OK
  source_code=r.text
  #print(source_code) '-> OK
  soup=bs(source_code,'html.parser')
  #return soup.prettify() '-> OK
  cards=soup.find_all("div", class_="col-xs-6 col-md-4 col-lg-3")
  for card in cards:
    currency={
    'ID':str(index),
    'Code':card.find("h5").string,
    'Currency':card.find("p").string
    }
    currencies.append(currency)
    index+=1
  return currencies

def convert(currency_1,currency_2,amount):
  if currency_1==currency_2:
    return "Converter o valor de uma moeda para ela mesma não faz sentido."
  url=f"{urls['converter']}{currency_1}-to-{currency_2}-rate?amount={amount}"
  #print(url)
  try:
    r=requests.get(url)
    source_code=r.text
    soup=bs(source_code,'html.parser')
    conversion=soup.find(class_="text-success").string
  except:
    return "Uma das moedas selecionadas (ou ambas) está(ão) indisponível(eis)."
  #print(conversion)
  converted=float(amount)*float(conversion)
  converted=format_currency(converted,currency_2.upper())
  amount=format_currency(amount,currency_1.upper())
  answer=(f"{amount} equivale a {converted}")
  return answer
