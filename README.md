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
| Fundamentos de Deep Learning (DL) | Construção e integração dos modelos neurais |
| Big Data e Engenharia de Dados (BD) | Pipeline de dados, ETL, armazenamento e preparação |
| Processamento de Linguagem Natural (PNL) | Processamento e representação dos textos |
| Visão Computacional (VC) | Extração de informações das imagens |

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

O Projeto Integrador será desenvolvido ao longo de **8 encontros remotos síncronos**, acompanhando a evolução das disciplinas participantes. A cada aula, os estudantes desenvolverão uma nova etapa da solução, construindo incrementalmente um **Sistema Inteligente Multimodal para Análise Automática de Chamados e Evidências**.

Todos os grupos utilizarão o **mesmo dataset oficial**, definido pelos professores no início do semestre.

## Cronograma das Aulas

| Aula | Data | Objetivo da Aula | Professor(es) | Marco do Projeto | Notebook da Etapa |
|:----:|:----------:|------------------|---------------|------------------|-------------------|
| **1** | **18/07/2026** | Apresentar o Projeto Integrador, formar os grupos, apresentar o dataset oficial e organizar o ambiente de desenvolvimento. | Todos (preferencialmente) ou **DL + BD** | Planejamento do projeto | **01_Exploracao.ipynb** |
| **2** | **25/07/2026** | Construir o pipeline de preparação dos dados (ETL, limpeza, transformação e particionamento). | **BD + DL** | Dados preparados | **02_Engenharia_Dados.ipynb** |
| **3** | **08/08/2026** | Desenvolver o primeiro modelo de Deep Learning utilizando um MLP como baseline. | **DL** | Primeiro modelo treinado | **03_Deep_Learning.ipynb** |
| **4** | **22/08/2026** | Desenvolver o módulo de Processamento de Linguagem Natural para análise das descrições textuais dos chamados. | **PNL + DL** | Modelo de PNL concluído | **04_PNL.ipynb** |
| **5** | **05/09/2026** | Desenvolver o módulo de Visão Computacional para análise das imagens associadas aos chamados. | **VC + DL** | Modelo de VC concluído | **05_Visao_Computacional.ipynb** |
| **6** | **19/09/2026** | Integrar os modelos de texto e imagem em um único modelo multimodal. | **DL + PNL + VC** | Modelo multimodal integrado | **06_Modelo_Multimodal.ipynb** |
| **7** | **03/10/2026** | Consolidar a solução, implementar o pipeline de inferência e discutir aspectos de escalabilidade e implantação. | **BD + DL** | Sistema integrado e operacional | **07_Pipeline_Final.ipynb** |
| **8** | **17/10/2026** | Apresentação dos projetos finais, demonstração da solução e avaliação integrada. | **Todos** | Projeto concluído | **Projeto Final** |

---

## Entregas Esperadas

Cada notebook representa uma etapa incremental da construção da solução. Ao final do semestre, todos os notebooks deverão compor um único repositório GitHub organizado, documentado e reproduzível.

| Notebook da Etapa | Aula | Objetivo | Competências Desenvolvidas | Conteúdo Esperado |
|-------------------|:----:|----------|----------------------------|-------------------|
| **01_Exploracao.ipynb** | 1 | Compreender o problema e planejar o projeto. | Planejamento de projetos, organização do trabalho em equipe, exploração de dados e definição da arquitetura da solução. | Apresentação do problema, exploração do dataset oficial (EDA), definição da arquitetura proposta e planejamento das atividades do grupo. |
| **02_Engenharia_Dados.ipynb** | 2 | Preparar os dados para utilização pelos modelos de IA. | Engenharia de Dados, ETL, preparação e documentação de pipelines. | Pipeline de ingestão, limpeza, transformação, tratamento de valores ausentes, engenharia de atributos (quando aplicável) e particionamento em treino, validação e teste. |
| **03_Deep_Learning.ipynb** | 3 | Desenvolver o modelo baseline em Deep Learning. | Construção e treinamento de redes neurais, avaliação e análise de desempenho. | Implementação do modelo MLP baseline, treinamento, ajuste de hiperparâmetros, avaliação e análise dos resultados. |
| **04_PNL.ipynb** | 4 | Desenvolver o módulo de Processamento de Linguagem Natural. | Pré-processamento textual, embeddings, classificação e avaliação de modelos de PNL. | Limpeza dos textos, geração de embeddings, treinamento do modelo, avaliação e análise dos resultados. |
| **05_Visao_Computacional.ipynb** | 5 | Desenvolver o módulo de Visão Computacional. | Processamento de imagens, CNNs, Transfer Learning e avaliação de modelos visuais. | Preparação das imagens, treinamento utilizando CNN ou Transfer Learning, avaliação e análise dos resultados. |
| **06_Modelo_Multimodal.ipynb** | 6 | Integrar os modelos de texto e imagem em uma solução única. | IA Multimodal, fusão de embeddings e integração entre modelos. | Implementação da estratégia de integração (Early Fusion, Late Fusion ou equivalente), treinamento do modelo multimodal e comparação com os modelos individuais. |
| **07_Pipeline_Final.ipynb** | 7 | Consolidar a solução completa. | Engenharia de IA, organização de pipelines, documentação e preparação para implantação. | Pipeline completo de inferência, organização do repositório, documentação técnica, avaliação final da solução e análise das limitações e oportunidades de melhoria. |
| **Projeto Final** | 8 | Apresentar e defender a solução desenvolvida. | Comunicação técnica, integração dos conhecimentos adquiridos e trabalho colaborativo. | Repositório GitHub organizado, todos os notebooks desenvolvidos durante o semestre, relatório técnico (até duas páginas), apresentação final (15 minutos) e demonstração da solução implementada. |

---

## Entregas Esperadas

Cada notebook representa uma etapa incremental da construção da solução. Ao final do semestre, todos os notebooks deverão compor um único repositório GitHub organizado, documentado e reproduzível.

| Notebook da Etapa | Aula | Objetivo | Competências Desenvolvidas | Conteúdo Esperado |
|-------------------|:----:|----------|----------------------------|-------------------|
| **01_Exploracao.ipynb** | 1 | Planejar o projeto e compreender o problema. | Planejamento de projetos, organização do trabalho em equipe, exploração de dados e definição da arquitetura da solução. | Descrição do problema, utlização do [dataset](/materiais/dataset/README.md), análise exploratória dos dados (EDA), arquitetura inicial da solução e planejamento das atividades do grupo. |
| **02_Engenharia_Dados.ipynb** | 2 | Preparar os dados para utilização pelos modelos de IA. | Engenharia de Dados, ETL, tratamento e preparação dos dados. | Pipeline de ingestão dos dados, limpeza, transformação, tratamento de valores ausentes, particionamento dos conjuntos de treino/validação/teste e documentação do processo. |
| **03_Deep_Learning.ipynb** | 3 | Desenvolver o primeiro modelo baseado em Deep Learning. | Construção de redes neurais, treinamento supervisionado, avaliação de modelos e análise de desempenho. | Implementação do modelo baseline (MLP), treinamento, ajuste de hiperparâmetros, avaliação e discussão dos resultados obtidos. |
| **04_NLP.ipynb** | 4 | Desenvolver o módulo de Processamento de Linguagem Natural. | Pré-processamento de textos, embeddings, classificação textual e avaliação de modelos NLP. | Limpeza e preparação dos textos, geração de embeddings, treinamento do modelo NLP, avaliação e análise dos resultados. |
| **05_Visao_Computacional.ipynb** | 5 | Desenvolver o módulo de Visão Computacional. | Processamento de imagens, CNNs, Transfer Learning e avaliação de modelos visuais. | Preparação das imagens, treinamento utilizando CNN ou Transfer Learning, avaliação do modelo e análise dos resultados. |
| **06_Modelo_Multimodal.ipynb** | 6 | Integrar os modelos de texto e imagem em uma única solução inteligente. | Modelagem multimodal, fusão de embeddings, integração entre modelos e comparação de arquiteturas. | Estratégia de integração (Early Fusion, Late Fusion ou similar), treinamento do modelo multimodal, avaliação comparativa e discussão dos ganhos obtidos. |
| **07_Pipeline_Final.ipynb** | 7 | Consolidar a solução desenvolvida pelo grupo. | Engenharia de IA, organização de pipelines, documentação técnica e preparação para implantação. | Pipeline completo de inferência, organização do projeto, documentação técnica, avaliação final da solução e análise das limitações e oportunidades de melhoria. |
| **Projeto Final** | 8 | Apresentar e defender a solução desenvolvida pelo grupo. | Comunicação técnica, integração de conhecimentos, trabalho colaborativo e apresentação de resultados. | Repositório GitHub organizado, todos os notebooks desenvolvidos durante o semestre, relatório técnico (até duas páginas), apresentação final (15 minutos) e demonstração da solução implementada. |


---

# Tecnologias Sugeridas

- Git
- GitHub
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-Learn
- TensorFlow
- Hugging Face Transformers
- OpenCV
- Apache Spark

---

# Organização do Repositório


- [README.md](README.md) onde temos as principais definições desse projeto.

- Diretório [grupos/](/grupos/) onde temos o template e arquivos dos grupos.

- Diretório [materiais/](/materiais/) onde teremos os datasets, templates dos notebooks, etc.

---

# Próximas Definições

Antes do início das aulas recomenda-se definir/confirmar:

- dataset oficial do projeto: sugestão inicial [aqui](/materiais/dataset/README.md);
- template do repositório dos alunos;
- template dos notebooks;
- critérios de avaliação;
- rubrica da apresentação final;
- composição dos grupos;
- cronograma de acompanhamento.

---

# Documento Vivo

Este README deverá ser atualizado sempre que decisões importantes forem tomadas ao longo do semestre.