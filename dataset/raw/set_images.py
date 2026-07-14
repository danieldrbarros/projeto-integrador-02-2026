from pathlib import Path
import re
import pandas as pd
from PIL import Image

# =============================================================================
# Configuração de caminhos
# =============================================================================

SCRIPT_DIR = Path(__file__).resolve().parent

INPUT_CSV = SCRIPT_DIR / "chamados_enriquecido.csv"
OUTPUT_CSV = SCRIPT_DIR / "chamados_com_imagens_individualizadas.csv"

# dataset/images
IMAGE_FOLDER = SCRIPT_DIR.parent / "images"

print(f"CSV de entrada : {INPUT_CSV}")
print(f"Pasta imagens  : {IMAGE_FOLDER}")
print(f"Existe?        : {IMAGE_FOLDER.exists()}")

# =============================================================================
# Carregar CSV
# =============================================================================

df_original = pd.read_csv(INPUT_CSV)
df = df_original.copy()

# Inicializa as colunas
df["image_path"] = ""
df["image_width"] = ""
df["image_height"] = ""

# =============================================================================
# Dicionário de imagens
# =============================================================================

termo_para_imagem = {
    # Hardware
    r"\bteclado\b": "keyboard.png",
    r"\bmouse\b": "mouse.png",
    r"\bmonitor\b": "monitor.png",
    r"\bcooler\b": "cooler.png",
    r"\bfonte\b": "power_supply.png",
    r"placa(?:[- ]de vídeo|[- ]mãe)": "motherboard.png",
    r"\bhd\b": "hard_drive.png",
    r"\bssd\b": "hard_drive.png",

    # Software
    r"\bsap\b": "sap_erp.png",
    r"\berp\b": "sap_erp.png",
    r"\bexcel\b": "office.png",
    r"\bword\b": "office.png",
    r"\bemail\b|\boutlook\b": "email.png",
    r"\bnavegador\b|\bcrm\b|\bftp\b": "browser.png",

    # Rede
    r"\bvpn\b": "vpn.png",
    r"\bwi[- ]?fi\b|\b5g\b|\bcabo\b|\brede\b": "network.png",
    r"\bservidor\b|\bbanco de dados\b": "server.png",

    # Acesso
    r"\blogin\b|\bautenticação\b": "login.png",
    r"\bpermissão\b|\bbloqueado\b|\bacesso negado\b": "access_denied.png",

    # RH
    r"portal do funcionário": "hr_portal.png",
    r"\bponto\b|\bfolha\b|\bfrequência\b": "payroll.png",
    r"\brecrutamento\b|\badmissão\b": "recruitment.png",

    # Financeiro
    r"\bnota fiscal\b|\bfatura\b|\bnf\b": "finance_report.png",
    r"\brelatório\b|\bconsulta\b|\bextrato\b": "finance_report.png",
    r"\bcontabilidade\b|\btesouraria\b|\bfinanceiro\b": "finance_report.png",
}

# =============================================================================
# Imagens padrão por categoria
# =============================================================================

fallback_por_categoria = {
    "Hardware": "default_hardware.png",
    "Software": "default_software.png",
    "Rede": "default_network.png",
    "Acesso": "default_access.png",
    "RH": "default_hr.png",
    "Financeiro": "default_finance.png",
}

# =============================================================================
# Escolha da imagem
# =============================================================================

def escolher_imagem(texto, categoria):

    if not isinstance(texto, str):
        texto = ""

    texto = texto.lower()

    # Procura pelos termos específicos
    for padrao, imagem in termo_para_imagem.items():
        if re.search(padrao, texto):
            return imagem

    # Caso contrário usa a imagem padrão da categoria
    return fallback_por_categoria.get(categoria)


# =============================================================================
# Texto para pesquisa
# =============================================================================

df["texto_completo"] = (
    df["title"].fillna("")
    + " "
    + df["description"].fillna("")
)

# Cache para não abrir a mesma imagem várias vezes
image_cache = {}

# =============================================================================
# Processamento
# =============================================================================

for idx, row in df.iterrows():

    imagem = escolher_imagem(
        row["texto_completo"],
        row["target_category"]
    )

    if imagem is None:
        continue

    caminho_imagem = IMAGE_FOLDER / imagem

    if not caminho_imagem.exists():
        print(f"Imagem não encontrada: {caminho_imagem}")
        continue

    # Lê a imagem apenas uma vez
    if caminho_imagem not in image_cache:
        with Image.open(caminho_imagem) as img:
            image_cache[caminho_imagem] = img.size

    width, height = image_cache[caminho_imagem]

    # Salva caminho relativo no CSV
    df.at[idx, "image_path"] = f"images/{imagem}"
    df.at[idx, "image_width"] = str(width)
    df.at[idx, "image_height"] = str(height)

# Remove coluna auxiliar
df.drop(columns=["texto_completo"], inplace=True)

# =============================================================================
# Relatório
# =============================================================================

sem_imagem = df[df["image_path"] == ""]
com_imagem = len(df) - len(sem_imagem)

print("\n" + "=" * 70)
print("RELATÓRIO")
print("=" * 70)
print(f"Total de chamados : {len(df)}")
print(f"Com imagem        : {com_imagem}")
print(f"Sem imagem        : {len(sem_imagem)}")

if len(sem_imagem):

    print("\nPrimeiros chamados sem imagem:\n")

    # Exibe apenas colunas que realmente existem
    colunas = []

    for coluna in [
        "id",
        "ticket_id",
        "call_id",
        "title",
        "target_category",
    ]:
        if coluna in df.columns:
            colunas.append(coluna)

    if colunas:
        print(sem_imagem[colunas].head(20))
    else:
        print(sem_imagem.head(20))

print("=" * 70)

# =============================================================================
# Salvar
# =============================================================================

df.to_csv(OUTPUT_CSV, index=False)

print(f"\nArquivo salvo com sucesso:\n{OUTPUT_CSV}")