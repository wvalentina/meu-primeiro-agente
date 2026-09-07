import os
import shutil

# Pasta principal e pasta de destino
pasta_usuario = os.path.expanduser("~")
pasta_destino = os.path.join(pasta_usuario, "Organizado_IA")
os.makedirs(pasta_destino, exist_ok=True)

for raiz, pastas, arquivos in os.walk(pasta_usuario):
    # Ignora pastas do sistema e a própria pasta organizada
    if "AppData" in raiz or ".git" in raiz or "Organizado_IA" in raiz:
        continue

    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        nome_lower = arquivo.lower()
        extensao = os.path.splitext(arquivo)[1].lower()
        
        pasta_alvo = None

        # Regra 1: Se tiver 'dossie' ou 'dossier' no nome
        if "dossie" in nome_lower or "dossier" in nome_lower:
            pasta_alvo = "Dossies"

        # Regra 2: Se for arquivo do Excel (.xlsx, .xls, .csv)
        elif extensao in [".xlsx", ".xls", ".csv"]:
            pasta_alvo = "Planilhas Excel"

        # Regra 3: Documentos de texto em geral
        elif extensao in [".pdf", ".docx", ".doc", ".txt"]:
            pasta_alvo = "Documentos"

        # Regra 4: Imagens e Capturas de Tela
        elif extensao in [".png", ".jpg", ".jpeg", ".gif"]:
            pasta_alvo = "Imagens"

        # Regra 5: Vídeos
        elif extensao in [".mp4", ".mkv", ".avi", ".mov"]:
            pasta_alvo = "Videos"

        # Move o arquivo para a pasta específica
        if pasta_alvo:
            caminho_pasta_alvo = os.path.join(pasta_destino, pasta_alvo)
            os.makedirs(caminho_pasta_alvo, exist_ok=True)
            try:
                shutil.move(caminho_completo, os.path.join(caminho_pasta_alvo, arquivo))
                print(f"Guardado em '{pasta_alvo}': {arquivo}")
            except Exception:
                pass
