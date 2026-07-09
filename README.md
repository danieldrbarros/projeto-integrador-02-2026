# Projeto Integrador 02/2026
## Pós-Graduação em Inteligência Artificial

![GitHub](https://img.shields.io/badge/status-em%20desenvolvimento-blue)
![Python](https://img.shields.io/badge/Python-3.11+-yellow)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![License](https://img.shields.io/badge/license-Acad%C3%AAmico-green)

---

# Sobre o Projeto

O Projeto Integrador tem como objetivo agregar os conhecimentos desenvolvidos nas disciplinas da Pós-Graduação em Inteligência Artificial por meio da construção de uma solução baseada em Inteligência Artificial aplicada a um problema real.

Durante o semestre, os estudantes desenvolverão incrementalmente um **Sistema Inteligente Multimodal para Análise Automática de Chamados e Evidências**, explorando conceitos de *Big Data e Engenharia de Dados*, *Processamento de Linguagem Natural*, *Visão Computacional*, e *Deep Learning*.

Todo o desenvolvimento deverá ser realizado em equipes utilizando GitHub como ferramenta de gerenciamento do projeto.

---

# Objetivos de Aprendizagem

Ao final do Projeto Integrador espera-se que os estudantes sejam capazes de:

- trabalhar em equipes utilizando GitHub;
- desenvolver pipelines de Big Data e Engenharia de Dados;
- aplicar técnicas modernas de Processamento de Linguagem Natural;
- desenvolver modelos de Visão Computacional;
- construir modelos de Deep Learning;
- integrar diferentes modalidades de dados em um único sistema inteligente;
- documentar adequadamente um projeto de IA;
- apresentar tecnicamente uma solução completa.

---

# Disciplinas Envolvidas

| Sigla | Disciplina | Professor |
|--------|------------|------------|
| **BD** | Big Data e Engenharia de Dados | Daniel Carvalho |
| **PLN** | Processamento de Linguagem Natural | Gabriel Santos |
| **VC** | Visão Computacional | Silvio Stanzani |
| **DL** | Fundamentos de Deep Learning | [Daniel Barros](https://github.com/danieldrbarros) |

---

# Projeto Integrador

## Tema

**Sistema Inteligente Multimodal para Análise Automática de Chamados e Evidências**

Imagine uma empresa que recebe milhares de chamados contendo:

- descrição textual;
- imagens anexadas;
- dados históricos;
- informações do cliente;
- informações operacionais.

O objetivo é desenvolver um sistema capaz de:

- compreender o texto;
- analisar as imagens;
- combinar diferentes modalidades de dados;
- classificar automaticamente o chamado;
- sugerir prioridade;
- auxiliar o processo de atendimento.

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

Todos os grupos utilizarão o **mesmo [dataset](/materiais/dataset/README.md) oficial**, definido pelos professores no início do semestre.

## Cronograma das Aulas

| Aula | Data | Objetivo da Aula | Professor(es) | Marco do Projeto | Notebook da Etapa |
|:----:|:----------:|------------------|---------------|------------------|-------------------|
| **1** | **18/07/2026** | Apresentar o Projeto Integrador, formar os grupos, apresentar o dataset oficial e organizar o ambiente de desenvolvimento. | Todos (preferencialmente) ou **DL + BD** | Planejamento do projeto | **01_Exploracao.ipynb** |
| **2** | **25/07/2026** | Construir o pipeline de preparação dos dados (ETL, limpeza, transformação e particionamento). | **BD + DL** | Dados preparados | **02_Engenharia_Dados.ipynb** |
| **3** | **08/08/2026** | Desenvolver o primeiro modelo de Deep Learning utilizando um MLP como baseline. | **DL** | Primeiro modelo treinado | **03_Deep_Learning.ipynb** |
| **4** | **22/08/2026** | Desenvolver o módulo de Processamento de Linguagem Natural para análise das descrições textuais dos chamados. | **PLN + DL** | Modelo de PLN concluído | **04_PLN.ipynb** |
| **5** | **05/09/2026** | Desenvolver o módulo de Visão Computacional para análise das imagens associadas aos chamados. | **VC + DL** | Modelo de VC concluído | **05_Visao_Computacional.ipynb** |
| **6** | **19/09/2026** | Integrar os modelos de texto e imagem em um único modelo multimodal. | **DL + PLN + VC** | Modelo multimodal integrado | **06_Modelo_Multimodal.ipynb** |
| **7** | **03/10/2026** | Consolidar a solução, implementar o pipeline de inferência e discutir aspectos de escalabilidade e implantação. | **BD + DL** | Sistema integrado e operacional | **07_Pipeline_Final.ipynb** |
| **8** | **17/10/2026** | Apresentação dos projetos finais, demonstração da solução e avaliação integrada. | **Todos** | Projeto concluído | **Projeto Final** |

---

## Entregas Esperadas

Cada notebook representa uma etapa incremental da construção da solução. Ao final do semestre, todos os notebooks deverão compor um único repositório GitHub organizado, documentado e reproduzível.

| Notebook da Etapa | Aula | Objetivo | Competências Desenvolvidas | Conteúdo Esperado |
|-------------------|:----:|----------|----------------------------|-------------------|
| **01_Exploracao.ipynb** | 1 | Planejar o projeto e compreender o problema. | Planejamento de projetos, organização do trabalho em equipe, exploração de dados e definição da arquitetura da solução. | Descrição do problema, utlização do [dataset](/materiais/dataset/README.md), análise exploratória dos dados (EDA), arquitetura inicial da solução e planejamento das atividades do grupo. |
| **02_Engenharia_Dados.ipynb** | 2 | Preparar os dados para utilização pelos modelos de IA. | Engenharia de Dados, ETL, tratamento e preparação dos dados. | Pipeline de ingestão dos dados, limpeza, transformação, tratamento de valores ausentes, particionamento dos conjuntos de treino/validação/teste e documentação do processo. |
| **03_Deep_Learning.ipynb** | 3 | Desenvolver o primeiro modelo baseado em Deep Learning. | Construção de redes neurais, treinamento supervisionado, avaliação de modelos e análise de desempenho. | Implementação do modelo baseline (MLP), treinamento, ajuste de hiperparâmetros, avaliação e discussão dos resultados obtidos. |
| **04_PLN.ipynb** | 4 | Desenvolver o módulo de Processamento de Linguagem Natural. | Pré-processamento de textos, embeddings, classificação textual e avaliação de modelos PLN. | Limpeza e preparação dos textos, geração de embeddings, treinamento do modelo PLN, avaliação e análise dos resultados. |
| **05_Visao_Computacional.ipynb** | 5 | Desenvolver o módulo de Visão Computacional. | Processamento de imagens, CNNs, Transfer Learning e avaliação de modelos visuais. | Preparação das imagens, treinamento utilizando CNN ou Transfer Learning, avaliação do modelo e análise dos resultados. |
| **06_Modelo_Multimodal.ipynb** | 6 | Integrar os modelos de texto e imagem em uma única solução inteligente. | Modelagem multimodal, fusão de embeddings, integração entre modelos e comparação de arquiteturas. | Estratégia de integração (Early Fusion, Late Fusion ou similar), treinamento do modelo multimodal, avaliação comparativa e discussão dos ganhos obtidos. |
| **07_Pipeline_Final.ipynb** | 7 | Consolidar a solução desenvolvida pelo grupo. | Engenharia de IA, organização de pipelines, documentação técnica e preparação para implantação. | Pipeline completo de inferência, organização do projeto, documentação técnica, avaliação final da solução e análise das limitações e oportunidades de melhoria. |
| **Projeto Final** | 8 | Apresentar e defender a solução desenvolvida pelo grupo. | Comunicação técnica, integração de conhecimentos, trabalho colaborativo e apresentação de resultados. | Repositório GitHub organizado, todos os notebooks desenvolvidos durante o semestre, relatório técnico (até duas páginas), apresentação final (15 minutos) e demonstração da solução implementada. |

---

# Produto Final

Cada grupo deverá entregar:

- Repositório GitHub organizado;
- Todos os notebooks desenvolvidos;
- Relatório técnico (até 2 páginas);
- Apresentação final (15 minutos);
- Demonstração da solução.

---

# Critérios de Avaliação

| Critério | Disciplina Relacionada | Peso |
|-----------|-----------|:---:|
| | BD | 15% |
| | DL | 20% |
| | PLN | 15% |
| | VC | 15% |
| | Modelo Multimodal | 20% |
| | Organização do GitHub | 5% |
| | Relatório Técnico | 5% |
| Apresentação oral e defesa do Projeto | Transversal | 5% |

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

# Estrutura Esperada dos Repositórios dos Grupos

```
grupo-XX/
├── README.md
├── notebooks/
├── models/
├── reports/
├── presentation/
├── src/
├── requirements.txt
```

---

# Organização do Projeto

Cada grupo deverá utilizar GitHub durante todo o desenvolvimento.

Recomenda-se:

- utilização de Issues;
- utilização de Pull Requests;
- commits frequentes;
- documentação contínua;
- versionamento dos notebooks.

---

# FAQ

### Podemos utilizar TensorFlow?

Sim.

---

### Podemos utilizar PyTorch?

Sim.

---

### Podemos utilizar outros modelos além dos apresentados em aula?

Sim, desde que devidamente documentados.

---

### Podemos utilizar bibliotecas adicionais?

Sim.

---

### Podemos utilizar Inteligência Artificial Generativa?

Sim, desde que o uso seja informado e documentado no relatório técnico.

---

### Podemos utilizar outro dataset?

Não.

Todos os grupos deverão utilizar o dataset oficial disponibilizado pelos professores.

---
