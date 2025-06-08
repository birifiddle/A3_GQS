from src.data_generator import generate_data
from src.model_training import train_models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def test_train_models_returns_all():
    data = generate_data(n_samples=100)
    X = data.drop('Status', axis=1)
    y = data['Status']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    models = train_models(X_train, y_train)
    assert len(models) == 3
    assert all(hasattr(m, "predict") for m in models.values())
