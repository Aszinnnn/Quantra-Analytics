import pandas as pd
import numpy as np
from faker import Faker

fake = Faker('pt_BR')

def generate_fake_data(num_records):
    data = []
    for i in range(1, num_records + 1):
        data.append({
            "id": i,
            "cnpj": fake.cnpj(),
            "razao_social": fake.company(),
            "nome_fantasia": f"{fake.company_suffix()} {fake.company()}",
            "ramo": np.random.choice(["Tecnologia", "Saúde", "Finanças", "Varejo", "Educação"]),
            "telefone": f"({fake.random_int(11, 99)}) {fake.random_int(1000, 9999)}-{fake.random_int(1000, 9999)}",
            "email": fake.company_email(),
            "endereco": fake.street_address(),
            "cidade": fake.city(),
            "estado": fake.estado_sigla(),
            "faturamento_anual": round(np.random.lognormal(10, 1), 2),
            "funcionarios": np.random.randint(1, 500),
            "site": fake.url()
        })
    return pd.DataFrame(data)