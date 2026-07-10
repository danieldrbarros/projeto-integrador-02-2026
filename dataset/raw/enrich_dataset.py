import pandas as pd
import random
import os

# --------------------------------------------
# 1. CONFIGURAÇÕES DE CAMINHO
# --------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAMADOS_PATH = os.path.join(BASE_DIR, 'chamados.csv')
CLIENTES_PATH = os.path.join(BASE_DIR, 'clientes.csv')
HISTORICO_PATH = os.path.join(BASE_DIR, 'historico.csv')
SAIDA_PATH = os.path.join(BASE_DIR, 'chamados_enriquecido.csv')

# --------------------------------------------
# 2. CARREGAR DADOS
# --------------------------------------------
df_chamados = pd.read_csv(CHAMADOS_PATH)
df_clientes = pd.read_csv(CLIENTES_PATH)
df_historico = pd.read_csv(HISTORICO_PATH)

# --------------------------------------------
# 3. REMOVER DUPLICIDADE: manter target_category
# --------------------------------------------
if 'category' in df_chamados.columns:
    df_chamados.drop('category', axis=1, inplace=True)

# --------------------------------------------
# 4. ENRIQUECER TEXTO
# --------------------------------------------
templates = {
    'Hardware': [
        'O {componente} apresenta {problema} e {sintoma}.',
        'O usuário relatou que o {componente} {problema} durante o {momento}.',
        'Falha crítica no {componente}: {problema} com {sintoma}.',
        'O {componente} não responde e exibe {sintoma}.',
        'Problema de hardware: o {componente} {problema} inesperadamente.'
    ],
    'Software': [
        'O sistema {software} exibe {problema} ao {acao}.',
        'Erro {tipo} no {software} durante a {acao}.',
        'O aplicativo {software} fecha inesperadamente quando {acao}.',
        'Falha no {software}: {problema} ao tentar {acao}.',
        'O {software} apresenta {sintoma} e não {acao}.'
    ],
    'Rede': [
        'A conexão de rede está {problema} e {sintoma}.',
        'O acesso à {recurso} falha com {problema}.',
        'Problema de conectividade: {problema} durante {acao}.',
        'Rede instável, {problema} ao acessar {recurso}.',
        'Falha de rede: {sintoma} ao tentar {acao}.'
    ],
    'RH': [
        'O {sistema} não está {problema} para {acao}.',
        'Falha no {sistema} ao tentar {acao}.',
        'O usuário não consegue {acao} devido a {problema}.',
        'Erro no sistema de RH: {problema} ao {acao}.',
        'O {sistema} apresenta {sintoma} durante {acao}.'
    ],
    'Financeiro': [
        'O módulo financeiro {problema} ao {acao}.',
        'Erro no {sistema_financeiro} durante {acao}.',
        'Relatório financeiro não {problema} corretamente.',
        'Falha no sistema financeiro: {problema} ao {acao}.',
        'O {sistema_financeiro} exibe {sintoma} ao gerar relatório.'
    ],
    'Acesso': [
        'O usuário não consegue {acao} devido a {problema}.',
        'Falha de autenticação ao tentar {acao}.',
        'O acesso ao {sistema} está bloqueado por {problema}.',
        'Problema de login: {problema} ao {acao}.',
        'O usuário relata {sintoma} ao tentar acessar {sistema}.'
    ]
}

substituicoes = {
    'componente': ['computador', 'notebook', 'monitor', 'teclado', 'mouse', 'placa-mãe', 'memória', 'HD', 'SSD',
                   'fonte', 'placa de vídeo', 'cooler'],
    'problema': ['apresenta erro', 'não funciona', 'reinicia sozinho', 'desliga', 'congela', 'fica lento', 'emite beep',
                 'superaquece', 'não liga', 'falha'],
    'sintoma': ['tela azul', 'tela preta', 'mensagem de erro', 'ruído', 'cheiro de queimado', 'sem resposta',
                'tela piscando', 'perda de dados'],
    'momento': ['inicialização', 'uso normal', 'execução de tarefa', 'impressão', 'acesso à rede',
                'abertura de arquivo', 'salvamento'],
    'software': ['Word', 'Excel', 'Navegador', 'Sistema ERP', 'CRM', 'Sistema de RH', 'Email', 'FTP',
                 'Sistema de Notas Fiscais', 'SAP'],
    'acao': ['salvar arquivo', 'abrir documento', 'enviar email', 'gerar relatório', 'fazer login', 'importar dados',
             'executar consulta', 'imprimir', 'exportar dados'],
    'tipo': ['de compilação', 'de runtime', 'de permissão', 'de sintaxe', 'de conexão', 'de memória'],
    'recurso': ['internet', 'intranet', 'VPN', 'servidor de arquivos', 'aplicação web', 'banco de dados'],
    'sistema': ['sistema de RH', 'sistema de ponto', 'portal do funcionário', 'sistema de folha',
                'sistema de recrutamento'],
    'sistema_financeiro': ['ERP', 'SAP', 'Sistema de contabilidade', 'Módulo de notas fiscais', 'Sistema de tesouraria']
}

def gerar_descricao(categoria):
    template = random.choice(templates.get(categoria, templates['Hardware']))
    for chave, opcoes in substituicoes.items():
        placeholder = '{' + chave + '}'
        if placeholder in template:
            template = template.replace(placeholder, random.choice(opcoes))
    return template

df_chamados['description'] = df_chamados['target_category'].apply(gerar_descricao)
df_chamados['title'] = df_chamados['description'].apply(lambda x: x[:60] + ('...' if len(x) > 60 else ''))

# --------------------------------------------
# 5. MANTER IMAGENS ORIGINAIS (sem gerar novas)
# --------------------------------------------
# As colunas image_path, image_width e image_height já existem em df_chamados
# e serão mantidas inalteradas.

# --------------------------------------------
# 6. INCORPORAR DADOS DE CLIENTES
# --------------------------------------------
df_enriquecido = df_chamados.merge(df_clientes, on='customer_id', how='left')

# --------------------------------------------
# 7. INCORPORAR DADOS DE HISTÓRICO (agregações)
# --------------------------------------------
historico_agg = df_historico.groupby('ticket_id').agg(
    num_events=('history_id', 'count'),
    last_event_date=('event_date', 'max'),
    event_types=('event_type', lambda x: '|'.join(x.unique()))
).reset_index()

pivot = df_historico.pivot_table(index='ticket_id', columns='event_type', aggfunc='size', fill_value=0).reset_index()
rename_map = {'Abertura': 'num_abertura', 'Atualização': 'num_updates', 'Imagem': 'num_images',
              'Encerramento': 'num_encerramento'}
pivot.rename(columns=rename_map, inplace=True)

historico_agg = historico_agg.merge(pivot, on='ticket_id', how='left')

# Garantir que todas as colunas esperadas existam
cols_esperadas = ['num_images', 'num_updates', 'num_abertura', 'num_encerramento']
for col in cols_esperadas:
    if col not in historico_agg.columns:
        historico_agg[col] = 0

# Mesclar com o DataFrame principal
df_enriquecido = df_enriquecido.merge(historico_agg, on='ticket_id', how='left')

# Preencher nulos e garantir tipos
df_enriquecido['num_events'] = df_enriquecido['num_events'].fillna(0).astype(int)
df_enriquecido['last_event_date'] = df_enriquecido['last_event_date'].fillna('')
df_enriquecido['event_types'] = df_enriquecido['event_types'].fillna('')

for col in cols_esperadas:
    if col in df_enriquecido.columns:
        df_enriquecido[col] = df_enriquecido[col].fillna(0).astype(int)

# --------------------------------------------
# 8. MOVER target_category PARA A ÚLTIMA COLUNA
# --------------------------------------------
if 'target_category' in df_enriquecido.columns:
    cols = [c for c in df_enriquecido.columns if c != 'target_category'] + ['target_category']
    df_enriquecido = df_enriquecido[cols]

# --------------------------------------------
# 9. SALVAR
# --------------------------------------------
df_enriquecido.to_csv(SAIDA_PATH, index=False)

print(f"✅ Dataset enriquecido salvo em: {SAIDA_PATH}")
print(f"Total de registros: {len(df_enriquecido)}")
print("As imagens originais foram mantidas (sem geração sintética).")