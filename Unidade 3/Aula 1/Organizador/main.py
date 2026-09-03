import os
import shutil

pastas_e_arquivos = {
    "imagens": ["png", "jpeg", "webp", "jpg"],
    "planilhas": ["xls", "csv", "xlsx"],
    "documentos": ["docx", "pdf", "txt"],
}

# "." => acessa a pasta atual
pasta_alvo = "." 
lista_arquivos = os.listdir(pasta_alvo)

for chave in pastas_e_arquivos.keys():
    caminho_pasta = os.path.join(pasta_alvo, chave)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

# "chave" vai iterar por cada itwm do dicionário. primeira iteração: chave = "imagens"
# o sistema trabalha com paths. vamos criar o path com os.path.join
# path = pasta_alvo, chave, ou seja, "./imagens"
# se ./imagens NÃO (not) existir, então mandamos o os criar
# os.makedirs(caminho_pasta)

for arquivo in lista_arquivos:
    extensao = arquivo.split(".")[-1]  #[-1] acessa o ultimo item da lista.

    for chave in pastas_e_arquivos.keys():
        # pastas_e_arquivos.keys()  retona ["imagens", "planillhas", "documentos"]
        # "chave" assume cada valor da lista keys
        if extensao in pastas_e_arquivos[chave]:
            path_origem = os.path.join(pasta_alvo, arquivo)
            path_destino = os.path.join(pasta_alvo, chave)
            shutil.move(path_origem, path_destino)
        



