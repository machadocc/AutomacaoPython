import requests
import time

idDoAgente = "151030354270"
statusPendente = "2"
statusEmAberto = "6"

#Get para pegar o Id do ticket para ser utilizado no Put de Status
def getIdTicket():
    
    url = f"https://magazord.freshdesk.com/api/v2/search/tickets?query=\"(status:{statusPendente})%20AND%20agent_id:{idDoAgente}\""
    token = "XHrurcWAzDjXeus2oU"
    headers = {'Cache-Control': 'no-cache'}

    requisicao = requests.get(url, auth=(token, "x"), headers=headers)

    if requisicao.status_code == 200:
        responseTicket = requisicao.json()
        if responseTicket["results"]:
            idTicket = responseTicket["results"][0]["id"]
            print("O id do ticket é:", idTicket)
            return idTicket
        else:
            print("Nenhum ticket em aberto foi encontrado.")
            return None
    else:
        print("Erro: ", requisicao.status_code)
        return None

#Post com a resposta e assinatura no ticket de acordo com o ID do ticket coletado na primeira função
def PostResposta(idTicketPost):
    url_base = f"https://magazord.freshdesk.com/api/v2/tickets/{idTicketPost}/reply"
    token = "XHrurcWAzDjXeus2oU"
    headers = {'Cache-Control': 'no-cache'}
    
    print("Fazendo o Post com a resposta do ticket...")

    body = {
        "body": "<div>Olá! Estou verificando a situação do seu chamado e ja irei retornar com uma resposta!</div><br>Atenciosamente,<br><p><div><img src='https://i.imgur.com/gqmqFLn.png' alt='assinaturaCristhian'></div>"
    }

    requisicaoPost = requests.post(url_base, auth=(token, "x"), headers=headers, json=body)

    if requisicaoPost.status_code == 201:
         print("Ticket respondido com sucesso!")
    else:
         print("O ticket não pode ser respondido!")
         print("o codigo do erro é:", requisicaoPost.status_code)
         print(requisicaoPost.url)


#Put Alteração de status do ticket para pendente
def putStatusTicket():

    url_base = "https://magazord.freshdesk.com/api/v2/tickets/"
    token = "XHrurcWAzDjXeus2oU"
    headers = {'Cache-Control': 'no-cache'}
    print("Fazendo um Put para alterar a situação do ticket...")
    idDoTicket = getIdTicket()

    if idDoTicket is not None:
       url = url_base + str(idDoTicket)
    else:
        print("ID do ticket não encontrado")

    body = {
        "status": 3,
        "priority": 2
    }

    requisicaoPut = requests.put(url, auth=(token,"x"), headers=headers, json=body)

    if requisicaoPut.status_code == 200:
         print("Alteração concluída com sucesso!")
    else:
         print("Alteração não pode ser concluida!")
         print("o codigo do erro é:", requisicaoPut.status_code)
         print("url:", requisicaoPut.url)    
while True:
        ticketId = getIdTicket()

        if ticketId:
            PostResposta(ticketId)
            putStatusTicket()
        else:
            print("Não foi possível obter o ID do ticket.")

        time.sleep(180)

