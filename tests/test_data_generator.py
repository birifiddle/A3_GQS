from src.data_generator import generate_data

def test_data_generation_shape():
    df = generate_data(n_samples=100)
    assert df.shape == (100, 5)
    assert 'Status' in df.columns
