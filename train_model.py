import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Générer des données de test
np.random.seed(42)
n_samples = 1000

# Créer des données réalistes
data = {
    'transaction_id': range(1, n_samples + 1),
    'montant': np.random.exponential(scale=200, size=n_samples),
    'distance_domicile_km': np.random.exponential(scale=300, size=n_samples),
    'nb_transactions_24h': np.random.poisson(2, n_samples),
    'heure': np.random.randint(0, 24, n_samples),
    'pays': np.random.choice(['France', 'Allemagne', 'Italie', 'Espagne', 'Royaume-Uni', 'États-Unis'], n_samples),
}

# Générer les fraudes basées sur les patterns
fraude = []
for i in range(n_samples):
    fraud_score = 0
    if data['montant'][i] > 500:
        fraud_score += 0.3
    if data['distance_domicile_km'][i] > 1000:
        fraud_score += 0.3
    if data['nb_transactions_24h'][i] >= 3:
        fraud_score += 0.2
    if data['heure'][i] >= 22 or data['heure'][i] <= 6:
        fraud_score += 0.1
    if data['pays'][i] != 'France':
        fraud_score += 0.1
    
    # Ajouter du bruit
    fraud_score += np.random.normal(0, 0.05)
    fraude.append(1 if fraud_score > 0.4 else 0)

data['fraude'] = fraude

df = pd.DataFrame(data)

# Nettoyage des données
df.drop_duplicates(subset=['transaction_id'], inplace=True)

# Créer des variables supplémentaires (l'heure est déjà en format numérique)
df['est_nuit'] = ((df['heure'] >= 22) | (df['heure'] <= 6)).astype(int)
df['est_etranger'] = (df['pays'] != 'France').astype(int)
df['montant_suspect'] = (df['montant'] > 500).astype(int)
df['distance_elevee'] = (df['distance_domicile_km'] > 1000).astype(int)
df['activite_intense'] = (df['nb_transactions_24h'] >= 3).astype(int)
df['montant_eleve'] = (df['montant'] > 1000).astype(int)

# Sélectionner les features
features = [
    'montant', 'distance_domicile_km', 'nb_transactions_24h',
    'est_nuit', 'est_etranger', 'montant_suspect', 'distance_elevee',
    'activite_intense', 'montant_eleve'
]

X = df[features]
y = df['fraude']

# Split données
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Entraîner Random Forest (meilleur modèle)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

# Prédictions
y_pred = model.predict(x_test)

# Afficher résultats
print("=== MODÈLE ENTRAÎNÉ ===")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.2%}")
print(classification_report(y_test, y_pred, target_names=['Normal', 'Fraude']))

# Sauvegarder modèle et scaler
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(features, 'features.pkl')

print("\n✓ Modèle sauvegardé : model.pkl")
print("✓ Scaler sauvegardé : scaler.pkl")
print("✓ Features sauvegardées : features.pkl")
