import pandas as pd
import numpy as np

def generate_data(n_samples=500, random_state=42):
    np.random.seed(random_state)
    
    idade = np.random.randint(20, 60, size=n_samples)
    salario = np.random.randint(2000, 10000, size=n_samples)
    tempo_empresa = np.random.randint(0, 20, size=n_samples)
    bonus_recebido = np.random.randint(0, 2, size=n_samples)

    status = [
        1 if (sal > 5000 and tempo > 5 and bonus == 1) else 0
        for sal, tempo, bonus in zip(salario, tempo_empresa, bonus_recebido)
    ]

    data = pd.DataFrame({
        'Idade': idade,
        'Salario': salario,
        'TempoEmpresa': tempo_empresa,
        'BonusRecebido': bonus_recebido,
        'Status': status
    })

    return data
