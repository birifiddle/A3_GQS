import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 1. Gerando dados simulados (em substituição ao db.csv)
def gerar_dados_simulados(n=100):
    np.random.seed(42)
    data = pd.DataFrame({
        'feature1': np.random.choice(['A', 'B', 'C'], n),
        'feature2': np.random.randn(n),
        'feature3': np.random.choice(['X', 'Y'], n),
        'Status': np.random.choice([0, 1], n)
    })
    return data


# 2. Tratamento de dados
def tratar_dados(data):
    data = data.dropna()
    label_encoder = LabelEncoder()
    for col in data.select_dtypes(include=['object']).columns:
        data[col] = label_encoder.fit_transform(data[col])
    return data


# 3. Separando variáveis independentes e target
def separar_variaveis(data):
    X = data.drop('Status', axis=1)
    y = data['Status']
    return X, y


# 4. Dividindo dados treino/teste
def dividir_dados(X, y, test_size=0.3, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


# 5. Normalizando os dados
def normalizar_dados(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled


# 6. Treinando e avaliando modelos
def treinar_avaliar_modelos(X_train, y_train, X_test, y_test):
    # Modelos
    modelos = {
        "Árvore de Decisão": DecisionTreeClassifier(random_state=42),
        "Naive Bayes": GaussianNB(),
        "Rede Neural": MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, random_state=42)
    }

    for nome, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)

        print(f"\n{nome}")
        print(f"Acurácia: {accuracy_score(y_test, y_pred):.4f}")
        print("Relatório de Classificação:\n", classification_report(y_test, y_pred))
        print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))

    return modelos


# 7. Comitê de classificadores
def treinar_avaliar_comite(modelos, X_train, y_train, X_test, y_test):
    comite = VotingClassifier(
        estimators=[(nome.lower().replace(" ", "_"), modelo) for nome, modelo in modelos.items()],
        voting='hard'
    )
    comite.fit(X_train, y_train)
    y_pred = comite.predict(X_test)

    print("\nComitê de Classificadores")
    print(f"Acurácia: {accuracy_score(y_test, y_pred):.4f}")
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))
    print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))


def main():
    # Gerar dados simulados
    data = gerar_dados_simulados(200)

    # Pré-processar
    data = tratar_dados(data)
    X, y = separar_variaveis(data)
    X_train, X_test, y_train, y_test = dividir_dados(X, y)
    X_train, X_test = normalizar_dados(X_train, X_test)

    # Treinar e avaliar modelos
    modelos = treinar_avaliar_modelos(X_train, y_train, X_test, y_test)

    # Treinar e avaliar comitê
    treinar_avaliar_comite(modelos, X_train, y_train, X_test, y_test)


if __name__ == "__main__":
    main()
