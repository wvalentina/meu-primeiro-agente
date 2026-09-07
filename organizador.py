import os
import shutil
from datetime import datetime

# Pasta principal do seu usuário
pasta_usuario = os.path.expanduser("~")

# Caixas organizadoras
categorias = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Musicas": [".mp3", ".wav"],
    "Instaladores": [".exe", ".msi"],
}

pasta_destino = os.path.join(pasta_usuario, "Organizado_IA")
os.makedirs(pasta_destino, exist_ok=True)

# Anos que devem ser apagados
anos_para_apagar = range(2017, 2021)  # 2017, 2018, 2019, 2020

# Varre as pastas do computador
for raiz, pastas, arquivos in os.walk(pasta_usuario):
    if "AppData" in raiz or ".git" in raiz or "Organizado_IA" in raiz:
        continue

    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        
        try:
            # Checa a data do arquivo
            data_criacao = os.path.getmtime(caminho_completo)
            ano_arquivo = datetime.fromtimestamp(data_criacao).year
            
            # Se for entre 2017 e 2020, apaga
            if ano_arquivo in anos_para_apagar:
                os.remove(caminho_completo)
                print(f"Apagado ({ano_arquivo}): {arquivo}")
                continue

            # Se não for desses anos, organiza em pastas
            extensao = os.path.splitext(arquivo)[1].lower()
            for categoria, extensoes in categorias.items():
                if extensao in extensoes:
                    pasta_cat = os.path.join(pasta_destino, categoria)
                    os.makedirs(pasta_cat, exist_ok=True)
                    shutil.move(caminho_completo, os.path.join(pasta_cat, arquivo))
                    print(f"Guardado: {arquivo} na pasta {categoria}")
                    break
        except Exception:
            pass
            
