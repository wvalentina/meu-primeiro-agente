import os
import shutil

pasta_usuario = os.path.expanduser("~")
pasta_destino = os.path.join(pasta_usuario, "Organizado_IA")
os.makedirs(pasta_destino, exist_ok=True)

# Tipos de arquivos permitidos para organizar
extensoes_validas = [
    ".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".csv",
    ".png", ".jpg", ".jpeg", ".gif", ".mp4", ".mkv", ".avi", ".exe", ".msi"
]

for raiz, pastas, arquivos in os.walk(pasta_usuario):
    # Protege pastas do sistema, ocultas e a pasta organizada
    if "AppData" in raiz or ".git" in raiz or "Organizado_IA" in raiz:
        continue

    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        extensao = os.path.splitext(arquivo)[1].lower()

        if extensao in extensoes_validas:
            # 1. Se for planilha do Excel, vai para 'Planilhas Excel'
            if extensao in [".xlsx", ".xls", ".csv"]:
                nome_pasta = "Planilhas Excel"
            else:
                # 2. Para os outros, pega a primeira palavra do nome (ex: Dossie, Cruzamento, Captura)
                nome_limpo = arquivo.replace("_", " ").replace("-", " ")
                primeira_palavra = nome_limpo.split()[0].capitalize()
                
                # Se a palavra for muito curta ou genérica, junta em 'Documentos Geral'
                if len(primeira_palavra) <= 2:
                    nome_pasta = "Documentos Geral"
                else:
                    nome_pasta = primeira_palavra

            # Cria a pasta do assunto e move o arquivo
            caminho_pasta_alvo = os.path.join(pasta_destino, nome_pasta)
            os.makedirs(caminho_pasta_alvo, exist_ok=True)

            try:
                shutil.move(caminho_completo, os.path.join(caminho_pasta_alvo, arquivo))
                print(f"Guardado em '{nome_pasta}': {arquivo}")
            except Exception:
                pass
