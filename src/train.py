import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from preprocessing import load_data, feature_engineering, prepare_features
from model import build_linear_model, build_random_forest_model

# 1) Veriyi yükle
df = load_data("data/FatihEvFiyatları.csv")

# 2) Feature engineering
df = feature_engineering(df)

# 3) X ve y hazırla
X, y = prepare_features(df)

# 4) Modelleri oluştur
linear_reg = build_linear_model()
rf_reg = build_random_forest_model()

# 5) Modelleri eğit
linear_reg.fit(X, y)
rf_reg.fit(X, y)

# 6) Cross-validation
cv_scores_linear = cross_val_score(linear_reg, X, y, cv=5, scoring='neg_mean_squared_error')
cv_scores_rf = cross_val_score(rf_reg, X, y, cv=5, scoring='neg_mean_squared_error')

print(f"Linear Regression CV MSE: {-cv_scores_linear.mean():.2f}")
print(f"Random Forest CV MSE: {-cv_scores_rf.mean():.2f}")

# 7) Tahminler
linear_pred = linear_reg.predict(X)
rf_pred = rf_reg.predict(X)

# 8) Metrikler
print(f"\nLinear Regression MAE: {mean_absolute_error(y, linear_pred):.2f}")
print(f"Random Forest MAE: {mean_absolute_error(y, rf_pred):.2f}")

print(f"\nLinear Regression RMSE: {np.sqrt(mean_squared_error(y, linear_pred)):.2f}")
print(f"Random Forest RMSE: {np.sqrt(mean_squared_error(y, rf_pred)):.2f}")

print("\n✅ Model eğitimi tamamlandı!")
