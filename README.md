Projeto de Refatoração com Machine Learning
Este projeto tem como objetivo aplicar boas práticas de qualidade de software e refatoração em um código Python que realiza experimentos de classificação supervisionada usando diferentes algoritmos de machine learning. Ele foi desenvolvido como parte de um trabalho acadêmico da disciplina de Gestão e Qualidade de Software.

Objetivo
Refatorar um código legado que realizava treinamento e avaliação de múltiplos classificadores em um conjunto de dados simulado. O foco da refatoração é aplicar:

Princípios SOLID;
Princípio DRY (Don't Repeat Yourself);
Padrões de projeto (Design Patterns), especialmente o Strategy;
Boas práticas de Clean Code;
Testes automatizados com pytest.

Estrutura do Projeto

├── src
│   ├── data_generator.py         # Geração de dados simulados
│   ├── data_preprocessing.py     # Tratamento e preparação dos dados
│   ├── model_training.py         # Treinamento dos modelos e comitê
│   ├── evaluation.py             # Avaliação de desempenho
│
├── tests
│   ├── test_data_generator.py
│   ├── test_data_preprocessing.py
│   ├── test_model_training.py
│   └── test_evaluation.py
│
├── main.py                       # Ponto de entrada do sistema
├── requirements.txt              # Dependências do projeto
└── README.md

Como Executar
Clone o repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie e ative um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as dependências:
pip install -r requirements.txt

Execute o projeto:
python src/main.py

Testes Automatizados:
Os testes foram desenvolvidos com pytest. Para rodar os testes:
pytest/tests
Todos os testes estão localizados na pasta tests/.

Tecnologias e Bibliotecas
pandas, numpy
scikit-learn
pytest

Objetivo do Código
Gerar dados fictícios simulando um problema de classificação binária.
Tratar e normalizar os dados.
Treinar modelos de Machine Learning (Árvore de Decisão, Naive Bayes, Rede Neural).
Avaliar o desempenho dos modelos.
Usar um comitê de classificadores (VotingClassifier).

Resultados Esperados
Código modularizado, testável e de fácil manutenção.
Complexidade reduzida com uso de abstrações e interfaces.
Facilidade para inserção de novos algoritmos e métricas sem alteração do núcleo do código.

