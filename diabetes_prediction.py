import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, classification_report, confusion_matrix
import xgboost as xgb
from imblearn.over_sampling import SMOTE


file_path = Path.home() / "Documents" / "Proiect" / "dataset" / "diabetes_health_indicators.csv"
df = pd.read_csv(file_path)

#subsample 1st class
df_0 = df[df.Diabetes_012 == 0].sample(80000, random_state=42, replace=False)
df_1 = df[df.Diabetes_012 == 1]
df_2 = df[df.Diabetes_012 == 2]


df_combined = pd.concat([df_0, df_1, df_2])

X = df_combined.drop("Diabetes_012", axis=1)
y = df_combined["Diabetes_012"]

#xgboost params
best_params = {
    "objective": "multi:softprob",
    "num_class": 3,
    "max_depth": 15,
    "learning_rate": 0.05,
    "subsample": 0.6,
    "n_estimators": 300,
    "verbosity": 0,
    "n_jobs": -1,
    "random_state": 42,
    "colsample_bytree": 0.7,
    "min_child_weight": 1,
    "gamma": 0
}

#sampling
best_sampling_strategy = {
    0: 80000,
    1: 59428,
    2: 79980
}


smote = SMOTE(sampling_strategy=best_sampling_strategy, random_state=42)
X_res, y_res = smote.fit_resample(X, y)


X_train_valid, X_test, y_train_valid, y_test = train_test_split(
    X_res, y_res, test_size=0.2, stratify=y_res, random_state=42
)
X_train, X_valid, y_train, y_valid = train_test_split(
    X_train_valid, y_train_valid, test_size=0.1, stratify=y_train_valid, random_state=42
)


model = xgb.XGBClassifier(**best_params)
model.fit(X_train, y_train)

#validation metrics
y_pred_valid = model.predict(X_valid)
print("\nValidation Set Evaluation:")
print(f"F1 Macro: {f1_score(y_valid, y_pred_valid, average='macro'):.4f}")
print(f"Accuracy: {accuracy_score(y_valid, y_pred_valid):.4f}")

#test metrics
y_pred_test = model.predict(X_test)
print("\nTest Set Evaluation:")
print(f"F1 Macro: {f1_score(y_test, y_pred_test, average='macro'):.4f}")
print(f"Accuracy: {accuracy_score(y_test, y_pred_test):.4f}")

print("\nClassification Report on Test Set:")
print(classification_report(y_test, y_pred_test))

print("Confusion Matrix on Test Set:")
print(confusion_matrix(y_test, y_pred_test))
