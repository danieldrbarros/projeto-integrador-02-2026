import pandas as pd
import re

# Carregar o CSV
df = pd.read_csv('chamados.csv')  # substitua pelo caminho real

# Dicionário: palavra-chave (regex) -> nome do arquivo de imagem
# A ordem importa: coloque os termos mais específicos primeiro
termo_para_imagem = {
    # Hardware
    r'\bteclado\b': 'keyboard.jpg',
    r'\bmouse\b': 'mouse.jpg',
    r'\bmonitor\b': 'monitor.jpg',
    r'\bcooler\b': 'cooler.jpg',
    r'\bfonte\b': 'power_supply.jpg',
    r'placa(?:[- ]de vídeo|[- ]mãe)': 'motherboard.jpg',
    r'\bhd\b': 'hard_drive.jpg',
    r'\bssd\b': 'hard_drive.jpg',
    # Software
    r'\bsap\b': 'sap_erp.jpg',
    r'\berp\b': 'sap_erp.jpg',
    r'\bexcel\b': 'office.jpg',
    r'\bword\b': 'office.jpg',
    r'\bemail\b|\boutlook\b': 'email.jpg',
    r'\bnavegador\b|\bcrm\b|\bftp\b': 'browser.jpg',
    # Rede
    r'\bvpn\b': 'vpn.jpg',
    r'\bwi[- ]?fi\b|\b5g\b|\bcabo\b|\brede\b': 'network.jpg',
    r'\bservidor\b|\bbanco de dados\b': 'server.jpg',
    # Acesso
    r'\blogin\b|\bautenticação\b': 'login.jpg',
    r'\bpermissão\b|\bbloqueado\b|\bacesso negado\b': 'access_denied.jpg',
    # RH
    r'portal do funcionário': 'hr_portal.jpg',
    r'\bponto\b|\bfolha\b|\bfrequência\b': 'payroll.jpg',
    r'\brecrutamento\b|\badmissão\b': 'recruitment.jpg',
    # Financeiro
    r'\bnota fiscal\b|\bfatura\b|\bnf\b': 'finance_report.jpg',
    r'\brelatório\b|\bconsulta\b|\bextrato\b': 'finance_report.jpg',
    r'\bcontabilidade\b|\btesouraria\b|\bfinanceiro\b': 'finance_report.jpg',
}

# Fallback por categoria (quando nenhum termo específico é encontrado)
fallback_por_categoria = {
    'Hardware': 'default_hardware.jpg',
    'Software': 'default_software.jpg',
    'Rede': 'default_network.jpg',
    'Acesso': 'default_access.jpg',
    'RH': 'default_hr.jpg',
    'Financeiro': 'default_finance.jpg'
}

# Função para escolher a imagem com base no texto
def escolher_imagem(texto, categoria):
    if not isinstance(texto, str):
        texto = ''
    texto = texto.lower()
    # Verifica cada termo (na ordem do dicionário)
    for padrao, imagem in termo_para_imagem.items():
        if re.search(padrao, texto, re.IGNORECASE):
            return imagem
    # Fallback
    return fallback_por_categoria.get(categoria, 'default.jpg')

# Aplicar: concatenar título e descrição para busca
df['texto_completo'] = df['title'].fillna('') + ' ' + df['description'].fillna('')
df['image_path'] = df.apply(lambda row: escolher_imagem(row['texto_completo'], row['target_category']), axis=1)

# Você pode definir largura e altura fixas ou extrair das imagens reais
df['image_width'] = 800
df['image_height'] = 600

# Remover coluna auxiliar (opcional)
df.drop('texto_completo', axis=1, inplace=True)

# Salvar CSV atualizado
df.to_csv('chamados_com_imagens_individualizadas.csv', index=False)