import pandas as pd


def load_data(file_path: str, dtypes =None) -> pd.DataFrame:
    """
    Load the dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    try:
        data = pd.read_csv(file_path, dtype=dtypes)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"No data: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the dataset.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Preprocessed DataFrame.
    """
    # Example preprocessing steps
    # Remove duplicates
    df = df.drop_duplicates()
    df['tramite_fecha'] = pd.to_datetime(df['tramite_fecha'], errors='coerce')

    # Remove columns not needed
    cols = [
        'titular_pais_nacimiento_id', 
        'titular_domicilio_provincia_id',
        'titular_pais_nacimiento_indec_id',
        'titular_domicilio_provincia_indec_id',
        'automotor_uso_codigo',
        'automotor_modelo_codigo',
        'automotor_marca_codigo',
        'automotor_tipo_codigo',
    ]
    df = df.drop(columns=cols, errors='ignore')
# Ordenar de más antiguo a más reciente
    df = df.sort_values(by='tramite_fecha')
    

    return df