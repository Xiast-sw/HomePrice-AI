from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

def build_linear_model():
    """Linear Regression modeli oluşturur."""
    return LinearRegression()

def build_random_forest_model():
    """Random Forest modeli oluşturur."""
    return RandomForestRegressor(n_estimators=100, random_state=42)
