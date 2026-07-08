# Dataset Oficial - Projeto Integrador 02/2026

## Sistema Inteligente Multimodal para Análise Automática de Chamados e Evidências

Este dataset foi desenvolvido para utilização no Projeto Integrador da Pós-Graduação em Inteligência Artificial.

O objetivo é permitir que os estudantes desenvolvam uma solução multimodal utilizando dados estruturados, textos e imagens.

## Estrutura

```
dataset/

├── README.md
├── data/
├──     chamados.csv
├──     clientes.csv
├──     historico.csv
└── imagens/
```

## Descrição dos arquivos

### data/chamados.csv

Tabela principal contendo os chamados de suporte.

Inclui:

- informações estruturadas;
- descrição textual;
- referência para imagens;
- categoria;
- prioridade;
- SLA;
- variáveis que poderão ou não ser utilizadas pelos grupos.

---

### data/clientes.csv

Informações cadastrais dos clientes.

Pode ser utilizada para enriquecer o conjunto de dados através de operações de JOIN.

---

### data/historico.csv

Histórico das interações de cada chamado.

Pode ser utilizado para análises temporais, sumarização, PNL e Engenharia de Dados.

---

### imagens/

Contém as imagens referenciadas pela coluna `image_file` presente em `chamados.csv`.

As imagens simulam:

- prints de tela;
- fotografias;
- documentos digitalizados.

---

## Observação

Nem todas as colunas precisam ser utilizadas.

Cabe aos grupos decidir:

- quais atributos utilizar;
- quais remover;
- quais transformar;
- quais criar durante o processo de Feature Engineering.