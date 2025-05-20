import pandas as pd
from config import data_path
from preprocessing import load_data, preprocess_data

dtype_fix = {
    'automotor_tipo_codigo': 'str',
    'titular_pais_nacimiento': 'str',
    'titular_porcentaje_titularidad': 'float',
    'titular_pais_nacimiento_id': 'str',
}

def main():
    # 1. Cargar datos
    df = load_data(data_path, dtypes=dtype_fix)

    # 2. Limpiar datos
    df = preprocess_data(df)

    # 3. Mostrar resumen básico
    print("First lines:")
    print(df.head())
    print(df.describe(include='all'))

    # 4. Guardar resultado limpio (opcional)
    df.to_csv('data/processed/robos_autos_limpio.csv', index=False)

if __name__ == "__main__":
    main()