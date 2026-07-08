# Projeto Integrador 02/2026

> Repositório interno dos professores da Pós-Graduação em Inteligência Artificial.

## Objetivo

Este repositório tem como objetivo organizar o Projeto Integrador do segundo semestre de 2026, servindo como ponto central de documentação, acompanhamento e alinhamento entre os professores participantes.

O Projeto Integrador busca aproximar os estudantes de um cenário real de desenvolvimento de soluções baseadas em Inteligência Artificial, promovendo a integração entre as disciplinas da pós-graduação em torno de um único problema.

Este documento deverá ser utilizado como referência ao longo de todo o semestre.

---

# Visão Geral do Projeto

Durante o semestre, os estudantes desenvolverão uma solução completa de Inteligência Artificial, percorrendo todas as etapas do ciclo de desenvolvimento:

- engenharia de dados;
- preparação dos dados;
- desenvolvimento dos modelos;
- processamento de linguagem natural;
- visão computacional;
- integração multimodal;
- avaliação dos modelos;
- apresentação dos resultados.

Cada disciplina contribui com uma parte da solução, mantendo sua autonomia e seus objetivos de aprendizagem, mas trabalhando sobre um mesmo problema.

---

# Tema do Projeto

## Sistema Inteligente Multimodal para Análise Automática de Chamados e Evidências

Imagine uma empresa que recebe milhares de chamados diariamente contendo:

- descrição textual do problema;
- imagens (prints de tela, fotografias, documentos);
- dados históricos dos atendimentos.

O objetivo é desenvolver um sistema inteligente capaz de:

- compreender o texto;
- analisar imagens;
- combinar diferentes modalidades de informação;
- classificar automaticamente os chamados;
- sugerir prioridade;
- gerar um resumo para auxiliar o atendente.

---

# Disciplinas Envolvidas

| Disciplina | Papel no Projeto |
|------------|------------------|
| Fundamentos de Deep Learning | Construção e integração dos modelos neurais |
| Big Data e Engenharia de Dados | Pipeline de dados, ETL, armazenamento e preparação |
| Processamento de Linguagem Natural | Processamento e representação dos textos |
| Visão Computacional | Extração de informações das imagens |

---

# Arquitetura Geral

```text
                         Chamados

                ┌──────────┴──────────┐
                │                     │
             Texto                Imagem
                │                     │
                └──────────┬──────────┘
                           │
           Big Data e Engenharia de Dados
                           │
            ┌──────────────┴──────────────┐
            │                             │
            ▼                             ▼

 Processamento de                 Visão
 Linguagem Natural            Computacional

            └──────────────┬──────────────┘
                           │
                 Deep Learning
                           │
                           ▼
            Sistema Inteligente Final
```

---

# Objetivos Pedagógicos

Ao final do projeto espera-se que os estudantes sejam capazes de:

- desenvolver soluções reais utilizando IA;
- integrar diferentes áreas da Inteligência Artificial;
- trabalhar colaborativamente em equipes;
- organizar projetos utilizando Git e GitHub;
- documentar adequadamente seus experimentos;
- apresentar resultados técnicos de forma clara e objetiva.

---

# Organização entre os Professores

Cada professor permanece responsável pelos conteúdos da sua disciplina.

O Projeto Integrador não substitui as disciplinas individuais, mas fornece um problema comum que será desenvolvido incrementalmente ao longo do semestre.

Espera-se que cada disciplina produza um componente que será incorporado ao sistema final.

Recomenda-se que os professores mantenham reuniões rápidas de alinhamento sempre que necessário para acompanhar a evolução dos grupos e garantir a integração entre as etapas.

---

# Cronograma

## Aula 1 — 18/07/2026

### Tema

Introdução ao Projeto Integrador

### Conteúdo

- apresentação do projeto;
- apresentação do problema;
- apresentação dos datasets;
- definição dos grupos;
- arquitetura geral;
- organização do GitHub;
- preparação do ambiente Python.

### Prática

Cada grupo deverá:

- escolher o domínio do problema;
- escolher o dataset;
- definir uma arquitetura inicial;
- criar o repositório GitHub.

### Professores

Idealmente todos os professores.

Alternativamente:

- Fundamentos de Deep Learning
- Big Data e Engenharia de Dados

### Entrega

Notebook0_Exploracao.ipynb

Conteúdo esperado:

- descrição do problema;
- exploração inicial dos dados;
- planejamento do grupo.

---

## Aula 2 — 25/07/2026

### Tema

Pipeline de Dados

### Conteúdo

- ETL;
- limpeza;
- tratamento;
- Feature Store;
- Pandas;
- Spark;
- organização dos dados.

### Prática

Construção do pipeline de preparação dos dados.

### Professores

- Big Data e Engenharia de Dados
- Fundamentos de Deep Learning

### Entrega

Notebook1_EngenhariaDados.ipynb

---

## Aula 3 — 08/08/2026

### Tema

Fundamentos de Deep Learning

### Conteúdo

- Perceptron;
- MLP;
- funções de ativação;
- treinamento;
- backpropagation.

### Prática

Treinamento de um modelo baseline utilizando MLP.

### Professor

Fundamentos de Deep Learning

### Entrega

Notebook2_BaselineMLP.ipynb

---

## Aula 4 — 22/08/2026

### Tema

Processamento de Linguagem Natural

### Conteúdo

- embeddings;
- Word2Vec;
- FastText;
- BERT;
- Transformers.

### Prática

Construção de um modelo para classificação de textos.

### Professores

- Processamento de Linguagem Natural
- Fundamentos de Deep Learning

### Entrega

Notebook3_NLP.ipynb

---

## Aula 5 — 05/09/2026

### Tema

Visão Computacional

### Conteúdo

- CNN;
- Transfer Learning;
- ResNet;
- EfficientNet.

### Prática

Construção do modelo de classificação de imagens.

### Professores

- Visão Computacional
- Fundamentos de Deep Learning

### Entrega

Notebook4_Visao.ipynb

---

## Aula 6 — 19/09/2026

### Tema

Integração Multimodal

### Conteúdo

- Early Fusion;
- Late Fusion;
- Attention;
- fusão de embeddings;
- integração entre modelos.

### Prática

Integração dos modelos de texto e imagem.

### Professores

- Fundamentos de Deep Learning
- Processamento de Linguagem Natural
- Visão Computacional

### Entrega

Notebook5_ModeloMultimodal.ipynb

---

## Aula 7 — 03/10/2026

### Tema

Pipeline Final e Escalabilidade

### Conteúdo

- Spark;
- APIs;
- Docker;
- inferência em lote;
- monitoramento.

### Prática

Construção do pipeline completo de inferência.

### Professores

- Big Data e Engenharia de Dados
- Fundamentos de Deep Learning

### Entrega

Notebook6_PipelineFinal.ipynb

---

## Aula 8 — 17/10/2026

### Tema

Apresentações Finais

Cada grupo deverá apresentar:

- arquitetura da solução;
- pipeline desenvolvido;
- modelos utilizados;
- resultados obtidos;
- métricas;
- limitações;
- trabalhos futuros.

### Professores

Todos os professores.

### Entrega Final

Cada grupo deverá entregar:

- repositório GitHub organizado;
- notebooks desenvolvidos durante o semestre;
- relatório técnico (até duas páginas);
- apresentação final (15 minutos).

---

# Organização dos Notebooks

```
Notebook0_Exploracao.ipynb

Notebook1_EngenhariaDados.ipynb

Notebook2_BaselineMLP.ipynb

Notebook3_NLP.ipynb

Notebook4_Visao.ipynb

Notebook5_ModeloMultimodal.ipynb

Notebook6_PipelineFinal.ipynb
```

---

# Tecnologias Sugeridas

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-Learn
- PyTorch
- TensorFlow (opcional)
- Hugging Face Transformers
- OpenCV
- Apache Spark
- MLflow (opcional)
- Git
- GitHub

---

# Organização do Repositório

```
README.md

grupos/

materiais/

reunioes/
```

---

# Próximas Definições

Antes do início das aulas recomenda-se definir:

- dataset oficial do projeto;
- template do repositório dos alunos;
- template dos notebooks;
- critérios de avaliação;
- rubrica da apresentação final;
- composição dos grupos;
- cronograma de acompanhamento.

---

# Documento Vivo

Este README deverá ser atualizado sempre que decisões importantes forem tomadas ao longo do semestre.