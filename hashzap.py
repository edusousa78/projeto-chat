# Titulo Hashzap
# Batão - iniciar chat
    # Popup/modal/alert
        # titulo - bem vindo ao hashzap
        # Campo Text - Ecreva seu nome no chat
        # Botão - Entrar no chat
            # sumir com o tiatulo e o botão inicial
            # Fechar o popup
            # Criaer o Chat(com nome do usuario)
            # embaixo do chat:
                # Campo text - Digite sua mensagem
                # Batão enviar
                    # visualisar a mensagem

import flet as ft


# funcão principal 
def main(pagina):
    # criar o titulo
    titulo = ft.Text("HashZap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel) # cria o tunel de comunicação

    titulo_janela = ft.Text("Bem vindo ao HashZap!")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no Chat")
    

    #enviar mensagem
    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        

        # envia mensagem no tunel

        pagina.pubsub.send_all(texto)

        # Limpar campo
        texto_mensagem.value = ""

        pagina.update()
    #criar o texto enviar mensagem
    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    #criar o botão enviar mendsagem
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    #coluna chat

    chat = ft.Column()

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    def entrar_chat(evento):
        # tirar titulo da página
        pagina.remove(titulo)
        # tirar o botão iniciar
        pagina.remove(botao_iniciar)
        # fechar o Popup
        janela.open = False
        #criar o chat
        pagina.add(chat)
        #add o texto enviar mensagem e o botão enviar mendsagem
        pagina.add(linha_mensagem)
        # Escrver mensagem: usuario entrou no chat
    
        texto_entrou_chat = f"{campo_nome_usuario.value}, Entrou no chat!"

        pagina.pubsub.send_all(texto_entrou_chat)
        #chat.controls.append(ft.Text(texto_entrou_chat))



        pagina.update()





    batao_entrar = ft.ElevatedButton("Entrar no Chat",on_click=entrar_chat)

    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[batao_entrar])

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)


    # add o titulo na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

#executar o sistema
ft.app(main, view=ft.WEB_BROWSER)
