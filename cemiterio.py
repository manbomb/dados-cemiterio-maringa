import datetime
import requests
import time
from bs4 import BeautifulSoup

inicio = datetime.datetime(2019, 10, 7)
fim = datetime.datetime(2020, 12, 7)

print("comecou")

while inicio <= fim:
    date_str = str(inicio.day).zfill(2)+'/'+str(inicio.month).zfill(2)+'/'+str(inicio.year)
    page = requests.get('http://venus.maringa.pr.gov.br/cemiterio/paginar_cadastro.php?dtfalec='+date_str)
    soup = BeautifulSoup(page.text, 'html.parser')
    count = soup.text.count('Nome:')
    arquivo = open('cemiterio.txt', 'a')
    arquivo.write(date_str+' - '+str(count)+'\n')
    arquivo.close()
    print(date_str+' - '+str(count))
    inicio = inicio + datetime.timedelta(days=1)
