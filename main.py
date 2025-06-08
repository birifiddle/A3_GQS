from src.data_generator import generate_data
from src.model_training import train_models, create_voting_classifier
from src.evaluation import evaluate_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def main():
    print("Gerando dados sintéticos...")
    data = generate_data()

    X = data.drop('Status', axis=1)
    y = data['Status']

    print("Dividindo dados...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Treinando modelos...")
    models = train_models(X_train, y_train)

    for name, model in models.items():
        y_pred = model.predict(X_test)
        evaluate_model(y_test, y_pred, name)

    print("Comitê de classificadores...")
    voting_clf = create_voting_classifier(models)
    voting_clf.fit(X_train, y_train)
    y_pred_voting = voting_clf.predict(X_test)
    evaluate_model(y_test, y_pred_voting, "Comitê de Classificadores")

if __name__ == "__main__":
    main()
