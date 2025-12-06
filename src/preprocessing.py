import pandas as pd
import numpy as np

def load_data(path):
    """CSV dosyasını yükler."""
    df = pd.read_csv(path, sep=";")
    return df

def feature_engineering(df):
    """Yeni özellikler oluşturur."""
    df['odasayi_binayasi'] = df['odasayisi'] * df['binayasi']
    df['log_fiyat'] = np.log(df['fiyat'])
    return df

def prepare_features(df):
    """Model için X ve y ayırır."""
    X = df[['alan', 'odasayisi', 'binayasi', 'odasayi_binayasi']]
    y = df['fiyat']
    return X, y
