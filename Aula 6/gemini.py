from google import genai

client = genai.Client(api_key=)

def perguntar_na_ia():
    interaction_id = None
    
    print("Digite sua dúvida. Em breve um especialista ira atender-lo.")

    while True:
        pergunta_usuario = input()

        if pergunta_usuario.lower() == "sair":
            break

        interaction = client.interactions.create(
            model ="gemini-3.5-flash",
            input = pergunta_usuario,
            system_instruction = "Você é o atendente do Python." \
            " Seu objetivo é responder a pergunta do usuário e capturar as informações básicas: nome, e-mail e telefone.",
            previous_interaction_id = interaction_id
        )

        interaction_id = interaction.id 

        print(interaction.output_text)
        print("Digite 'sair' se deseja encerrar a conversa.")