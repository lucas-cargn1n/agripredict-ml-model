# 🌱 AgriPredict: Sistema Inteligente de Recomendação Agrícola

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](COLOQUE_O_LINK_DO_SEU_STREAMLIT_AQUI)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)](https://scikit-learn.org/)

## 📖 Visão Geral do Produto
O **AgriPredict** é um sistema de recomendação (AgTech) projetado para produtores agrícolas que precisam otimizar o uso do solo e maximizar a colheita. Diferentemente da intuição empírica, este produto garante uma decisão guiada por dados para sugerir a cultura mais adequada com base nas condições químicas do solo e do clima, visando reduzir perdas e aumentar a lucratividade.

Este projeto faz parte do portfólio prático focado na aplicação ponta a ponta de **Machine Learning**, desenvolvido com os conceitos da Especialização em Data Science (UTFPR).

## 🎯 O Problema
A escolha incorreta da cultura para um determinado tipo de solo pode resultar em safras de baixa qualidade, desperdício de fertilizantes e prejuízos financeiros. O objetivo deste projeto é responder à pergunta: *Dadas as métricas de Nitrogênio (N), Fósforo (P), Potássio (K), pH, temperatura, umidade e volume de chuvas, qual é a melhor planta para se cultivar?*

## ⚙️ Tecnologias e Metodologia
Este projeto foi desenvolvido utilizando ferramentas *Open Source* e Cloud gratuitas:
* **Linguagem & Manipulação de Dados:** Python, Pandas, NumPy
* **Análise Exploratória e Visualização:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest e Multilayer Perceptron - Redes Neurais)
* **Deploy / Interface Web:** Streamlit Community Cloud

### Etapas do Pipeline de Dados:
1. **Coleta de Dados:** Utilização do *Crop Recommendation Dataset* (Kaggle).
2. **Análise Exploratória (EDA):** Verificação de correlações entre nutrientes e clima.
3. **Pré-processamento:** Separação de treino/teste (80/20) e padronização de escala com `StandardScaler`.
4. **Modelagem:** Treinamento e comparação entre algoritmos baseados em árvores (`Random Forest`) e Deep Learning clássico (`MLPClassifier`).
5. **Avaliação:** Análise baseada em Acurácia, F1-Score e Matriz de Confusão.

## 📊 Resultados e Desempenho
Durante os testes, os modelos apresentaram o seguinte desempenho no conjunto de validação:

* **Random Forest:** Acurácia de **[PREENCHA COM SUA ACURÁCIA, ex: 99.3%]**
* **Rede Neural (MLP):** Acurácia de **[PREENCHA COM SUA ACURÁCIA, ex: 97.5%]**

A Matriz de Confusão revelou que o modelo [INCLUA UMA BREVE OBSERVAÇÃO, ex: "consegue distinguir perfeitamente entre culturas de clima quente e frio, com uma taxa de erro quase nula"]. 

O **Random Forest** foi selecionado para o deploy na interface final por apresentar a melhor relação entre acurácia e velocidade de inferência.

## 🚀 Como testar o projeto na Web

O modelo final foi implantado e pode ser testado diretamente no seu navegador, sem necessidade de instalação:
👉 **[Acessar o AgriPredict no Streamlit](COLOQUE_O_LINK_DO_SEU_STREAMLIT_AQUI)**

## 💻 Como rodar o código localmente

Caso queira clonar o repositório e executar o código na sua máquina:

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação Streamlit:
   ```bash
   streamlit run app.py
   ```

## 🤝 Autor
Desenvolvido por **[Seu Nome/Sobrenome]** 
* Conecte-se comigo no [LinkedIn](LINK_DO_SEU_LINKEDIN)
