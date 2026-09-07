import os
import shutil

# Pega o caminho das pastas principais
pasta_usuario = os.path.expanduser("~")
area_de_trabalho = os.path.join(pasta_usuario, "Desktop")
if not os.path.exists(area_de_trabalho):
    area_de_trabalho = os.path.join(pasta_usuario, "Área de Trabalho")

pasta_destino = os.path.join(pasta_usuario, "Organizado_IA")
os.makedirs(pasta_destino, exist_ok=True)

# 1. Aprende como a Área de Trabalho está organizada
mapa_categorias = {}
if os.path.exists(area_de_trabalho):
    for item in os.listdir(area_de_trabalho):
        caminho_item = os.path.join(area_de_trabalho, item)
        if os.path.isdir(caminho_item) and not item.startswith("."):
            extensoes_encontradas = set()
            for raiz, _, arquivos in os.walk(caminho_item):
                for arq in arquivos:
                    ext = os.path.splitext(arq)[1].lower()
                    if ext:
                        extensoes_encontradas.add(ext)
            if extensoes_encontradas:
                mapa_categorias[item] = extensoes_encontradas

# Caso não encontre extensões específicas, usa padrão
if not mapa_categorias:
    mapa_categorias = {
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Musicas": [".mp3", ".wav"],
        "Instaladores": [".exe", ".msi"],
    }

# 2. Organiza o resto do computador usando o modelo da Área de Trabalho
for raiz, pastas, arquivos in os.walk(pasta_usuario):
    # Ignora pastas do sistema, a própria área de trabalho e a pasta destino
    if "AppData" in raiz or ".git" in raiz or "Organizado_IA" in raiz or area_de_trabalho in raiz:
        continue

    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        extensao = os.path.splitext(arquivo)[1].lower()
        if not extensao:
            continue

        for nome_pasta, extensoes in mapa_categorias.items():
            if extensao in extensoes:
                pasta_final = os.path.join(pasta_destino, nome_pasta)
                os.makedirs(pasta_final, exist_ok=True)
                try:
                    shutil.move(caminho_completo, os.path.join(pasta_final, arquivo))
                    print(f"Guardado em '{nome_pasta}': {arquivo}")
                except Exception:
                    pass
                break
            
