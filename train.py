import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

print("📂 Loading dataset...")

df = pd.read_csv("data/pcos.csv")
df.columns = df.columns.str.strip()

# ------------------ FEATURES ------------------

features = [
    "Age (yrs)",              # ⭐ ADDED FIRST
    "Cycle(R/I)",
    "Cycle length(days)",
    "BMI",
    "Weight gain(Y/N)",
    "hair growth(Y/N)",
    "Skin darkening (Y/N)",
    "FSH/LH"
]

target = "PCOS (Y/N)"

df = df[features + [target]]

# ------------------ CLEANING ------------------

df["Cycle(R/I)"] = df["Cycle(R/I)"].map({"R": 0, "I": 1})

df = df.apply(pd.to_numeric, errors='coerce')
df = df.fillna(df.mean())

X = df[features]
y = df[target]

print("✅ Using features:", features)

# ------------------ SPLIT ------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------ SCALING ------------------

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ------------------ MODEL ------------------

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ------------------ SAVE ------------------

os.makedirs("model", exist_ok=True)

pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(scaler, open("model/scaler.pkl", "wb"))

print("✅ Model trained & saved successfully!")