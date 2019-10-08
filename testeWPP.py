import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

def sendWppPromocao(nome, link):
    account_sid = '(sid da sua conta do twilio)'
    auth_token = '(token da sua conta do twilio)'
    client = Client(account_sid,auth_token)

    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+5531(numero do wpp que vai receber a msg)'

    client.messages.create(body=nome + '\n' + link,
                           from_=from_whatsapp_number, to=to_whatsapp_number)

def sendWppSemPromocao(nome):
    account_sid = '(sid da sua conta do twilio)'
    auth_token = '(token da sua conta do twilio)'
    client = Client(account_sid,auth_token)

    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+5531(numero que vai receber a msg)'

    client.messages.create(body='Sem promoções para o produto: ' + nome,
                           from_=from_whatsapp_number, to=to_whatsapp_number)

def verifica_Teste():
    URL = 'https://www.kabum.com.br/produto/99683/processador-intel-core-i5-9400f-coffee-lake-cache-9mb-2-9ghz-4-1ghz-max-turbo-lga-1151-bx80684i59400f'

    headers = {"User-Agent": '(procura no seu browser : check my user agent e copia ele aqui no lugar desses parenteses)'}

    page = requests.get( URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    nome = soup.find(id='titulo_det').get_text().strip()
    if(soup.find(id="contador-cm")):
        sendWppPromocao(nome, URL)
    else: sendWppSemPromocao(nome)

verifica_Teste()