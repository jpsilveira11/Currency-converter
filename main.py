from babel.numbers import format_currency
from wise import get_currencies as gc, convert as c
from iban import get_database as gdb

currencies=gc()
db=gdb()

def show_countries(db):
  for d in db:
    print(f"#{d['ID']}. {d['Country']}")
  return

def get_input(db_lenght):
  usr_input=input("-> ")
  while not usr_input.isnumeric() or int(usr_input)>db_lenght or int(usr_input)<=0:
    if not usr_input.isnumeric():
      print("Não é um número")
      usr_input=input("-> ")
    else:
      print("ID não existe nos registros")
      usr_input=input("-> ")
  usr_input=int(usr_input)-1
  return usr_input
  
def query(db,usr_input):
  print(f"{db[usr_input]['Currency']} | {db[usr_input]['Code']}")
  return db[usr_input]['Code']

def get_amount():
  valid=False
  while not valid:
    usr_input=input("-> ")
    if "," in usr_input:
      usr_input=usr_input.replace(",",".")
    if any([element.isalpha() for element in usr_input]) or "-" in usr_input:
      print("Valor monetário inválido. ")
    else:
      valid=True    
  return usr_input

def new_query():
  usr_input=input("-> ").lower()
  need_answer=True
  while need_answer:
    if usr_input=='s':
      return True
    elif usr_input=='n':
      return False
    else:
      usr_input=input("Responda apenas com sim ou não. [S/n]")
  

def finish():
  print("\nFinalizado.")
  print("Winners win")
  print(u"\U0001F40D" + " Maratona Python")
  return
  
# já deixei instalado e importado o requests,
# o BeautifulSoup e o babel.numbers (caso queira usar)

# pode apagar esses comentários após ler
#test=get_input(len(db))
  
if __name__=='__main__':
  currencies=gc()
  db=gdb()
  running=True
  print("Conversor de moedas 0.1.0")
  while running:
    show_countries(db)
    print("Converter de [Input ID]: ")
    usr_input=get_input(len(db))
    currency_1=query(db,usr_input).lower()
    print("Para [Input ID]: ")
    usr_input=get_input(len(db))
    currency_2=query(db,usr_input).lower()
    print("Valor a ser convertido: ")
    amount=get_amount()
    print(c(currency_1,currency_2,amount))
    print("Nova consulta? [S/n]")
    running=new_query()
  finish()
    
'''
# BOM DESAFIO!
'''