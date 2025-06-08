from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def evaluate_model(y_true, y_pred, model_name):
    print(f"\n Avaliação - {model_name}")
    print("Acurácia:", accuracy_score(y_true, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_true, y_pred))
    print("Matriz de Confusão:\n", confusion_matrix(y_true, y_pred))
