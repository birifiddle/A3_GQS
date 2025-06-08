# Projeto de Refatoração com Clean Code e Padrões de Projeto

Este projeto consiste na refatoração de um código legado de machine learning com foco na aplicação de boas práticas de desenvolvimento, tais como **Clean Code**, **princípios SOLID**, uso de **padrões de projeto**, **testes unitários** e **modularização**.

---

## Objetivos

- Refatorar um código legado utilizando princípios de engenharia de software.
- Aplicar os princípios **SOLID**.
- Garantir legibilidade e manutenção com **Clean Code**.
- Utilizar **Design Pattern** (comitê de votação).
- Escrever **testes unitários com Pytest**.
- Separar responsabilidades e criar uma arquitetura modular.

---

## Tecnologias Utilizadas

- Python 3.11+
- scikit-learn
- pandas
- numpy
- pytest

---

## Estrutura do Projeto

```bash
seu_projeto/
│
├── src/
│   ├── data_generator.py       # Geração de dados sintéticos
│   ├── data_preprocessor.py    # Pré-processamento e codificação
│   ├── data_splitter.py        # Separação entre treino e teste
│   ├── data_scaler.py          # Escalonamento dos dados
│   ├── model_trainer.py        # Treinamento dos modelos
│   └── voting_committee.py     # Implementação do comitê de votação
│
└── tests/
    └── test_ml_module.py       # Testes unitários com Pytest
