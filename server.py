import requests
import time

idDoAgente = "151030354270"
statusPendente = "2"
statusEmAberto = "6"

def getIdTicket():
    url = f"https://magazord.freshdesk.com/api/v2/search/tickets?query=\"(status:{statusPendente}%20OR%20status:{statusEmAberto})%20AND%20agent_id:{idDoAgente}\""
    token = "XHrurcWAzDjXeus2oU"
    headers = {'Cache-Control': 'no-cache'}

    requisicao = requests.get(url, auth=(token, "x"), headers=headers)

    if requisicao.status_code == 200:
        responseTicket = requisicao.json()
        if responseTicket["results"]:
            idTicket = responseTicket["results"][0]["id"]
            with open('saida.txt', 'a') as file:
                file.write(f"O id do ticket é: {idTicket}\n")
            return idTicket
        else:
            with open('saida.txt', 'a') as file:
                file.write("Nenhum ticket em aberto foi encontrado.\n")
            return None
    else:
        with open('saida.txt', 'a') as file:
            file.write(f"Erro: {requisicao.status_code}\n")
        return None

def PostResposta(idTicketPost):
    url_base = f"https://magazord.freshdesk.com/api/v2/tickets/{idTicketPost}/reply"
    token = "XHrurcWAzDjXeus2oU"
    headers = {'Cache-Control': 'no-cache'}
    
    with open('saida.txt', 'a') as file:
        file.write("Fazendo o Post com a resposta do ticket...\n")

    body = {
        "body": "<div>Olá! Estou verificando a situação do seu chamado e ja irei retornar com uma resposta!</div><br>Atenciosamente,<br><p><div><img src='https://i.imgur.com/gqmqFLn.png' alt='assinaturaCristhian'></div>"
    }

    requisicaoPost = requests.post(url_base, auth=(token, "x"), headers=headers, json=body)

    if requisicaoPost.status_code == 201:
         with open('saida.txt', 'a') as file:
             file.write("Ticket respondido com sucesso!\n")
    else:
         with open('saida.txt', 'a') as file:
             file.write(f"O ticket não pode ser respondido! Código do erro: {requisicaoPost.status_code}\n")

def putStatusTicket():
    url_base = "https://magazord.freshdesk.com/api/v2/tickets/"
    token = "XHrurcWAzDjXeus2oU"
    headers = {'Cache-Control': 'no-cache'}
    
    with open('saida.txt', 'a') as file:
        file.write("Fazendo um Put para alterar a situação do ticket...\n")

    idDoTicket = getIdTicket()

    if idDoTicket is not None:
       url = url_base + str(idDoTicket)
    else:
        with open('saida.txt', 'a') as file:
            file.write("ID do ticket não encontrado\n")

    body = {
        "status": 3,
        "priority": 2
    }

    requisicaoPut = requests.put(url, auth=(token,"x"), headers=headers, json=body)

    if requisicaoPut.status_code == 200:
         with open('saida.txt', 'a') as file:
             file.write("Alteração concluída com sucesso!\n")
    else:
         with open('saida.txt', 'a') as file:
             file.write(f"Alteração não pode ser concluída! Código do erro: {requisicaoPut.status_code}\n")


    time.sleep(120)