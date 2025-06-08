from src.evaluation import evaluate_model

def test_evaluation_runs_without_error():
    y_true = [0, 1, 1, 0, 1]
    y_pred = [0, 1, 0, 0, 1]
    evaluate_model(y_true, y_pred, "Teste Simples")
