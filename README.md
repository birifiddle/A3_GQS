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

├── src/
│   ├── data_generator.py        # Geração de dados simulados
│   ├── preprocessing.py         # Pré-processamento dos dados
│   ├── model_training.py        # Treinamento e avaliação dos modelos
│   └── evaluation.py            # Avaliação dos resultados
│
├── tests/
│   ├── test_data_generator.py
│   ├── test_model_training.py
│   └── test_evaluation.py
│
├── main.py                      # Script principal
├── README.md
├── requirements.txt
