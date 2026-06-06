import json
import os

ARQUIVO_PADRAO = "estoque.json"

def carregar_dados(caminho_arquivo=ARQUIVO_PADRAO):
    if not os.path.exists(caminho_arquivo):
        return {"nao_ordenado": [], "ordenado": []}
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return {"nao_ordenado": [], "ordenado": []}

def salvar_dados(dados, caminho_arquivo=ARQUIVO_PADRAO):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)