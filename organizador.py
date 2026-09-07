import os
import shutil

# Pega a pasta principal do seu usuário (Documentos, Downloads, Area de Trabalho, etc.)
pasta_usuario = os.path.expanduser("~")

# Caixas organizadoras
categorias = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Musicas": [".mp3", ".wav"],
    "Instaladores": [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".7z"]
}

# O robo varrendo todas as pastas do seu notebook
for raiz, pastas, arquivos in os.walk(pasta_usuario):
    # Evita mexer em pastas do sistema ou ocultas
    if "AppData" in raiz or ".git" in raiz:
        continue
        
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(raiz, arquivo)
        ext = os.path.splitext(arquivo)[1].lower()
        
        for categoria, extensoes in categorias.items():
            if ext in extensoes:
                pasta_destino = os.path.join(pasta_usuario, "Organizado_IA", categoria)
                os.makedirs(pasta_destino, exist_ok=True)
                
                # Move o arquivo para a caixa certa dentro de Organizado_IA
                try:
                    shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                    print(f"Guardado: {arquivo} na pasta {categoria}")
                except Exception as e:
                    pass
                  
