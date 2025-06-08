from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import VotingClassifier

def train_models(X_train, y_train):
    model_dt = DecisionTreeClassifier(random_state=42)
    model_nb = GaussianNB()
    model_nn = MLPClassifier(hidden_layer_sizes=(50,), max_iter=1000, random_state=42)

    model_dt.fit(X_train, y_train)
    model_nb.fit(X_train, y_train)
    model_nn.fit(X_train, y_train)

    return {
        'Árvore de Decisão': model_dt,
        'Naive Bayes': model_nb,
        'Rede Neural': model_nn
    }

def create_voting_classifier(models):
    return VotingClassifier(estimators=[
        ('dt', models['Árvore de Decisão']),
        ('nb', models['Naive Bayes']),
        ('nn', models['Rede Neural'])
    ], voting='hard')
