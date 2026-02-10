from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os
from pathlib import Path

app = Flask(__name__)

# Obtenir le répertoire de l'app
APP_DIR = Path(__file__).parent

# Charger le modèle et les ressources
model = None
scaler = None
features = None

try:
    model_path = APP_DIR / 'model.pkl'
    scaler_path = APP_DIR / 'scaler.pkl'
    features_path = APP_DIR / 'features.pkl'
    
    if model_path.exists() and scaler_path.exists() and features_path.exists():
        model = joblib.load(str(model_path))
        scaler = joblib.load(str(scaler_path))
        features = joblib.load(str(features_path))
        print("✓ Modèle chargé avec succès")
    else:
        print(f"⚠️ Fichiers manquants")
except Exception as e:
    print(f"❌ Erreur chargement modèle: {e}")

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API pour prédire une fraude"""
    if model is None:
        return jsonify({'error': 'Modèle non disponible'}), 500
    
    try:
        data = request.json
        
        # Extraire les données
        montant = float(data['montant'])
        distance = float(data['distance'])
        nb_transactions = int(data['nb_transactions'])
        heure = int(data['heure'])
        pays = data['pays']
        
        # Créer les features
        est_nuit = 1 if (heure >= 22 or heure <= 6) else 0
        est_etranger = 1 if pays != 'France' else 0
        montant_suspect = 1 if montant > 500 else 0
        distance_elevee = 1 if distance > 1000 else 0
        activite_intense = 1 if nb_transactions >= 3 else 0
        montant_eleve = 1 if montant > 1000 else 0
        
        # Créer le vecteur d'entrée
        input_data = np.array([[
            montant, distance, nb_transactions,
            est_nuit, est_etranger, montant_suspect, distance_elevee,
            activite_intense, montant_eleve
        ]])
        
        # Prédiction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        return jsonify({
            'fraude': int(prediction),
            'probabilite_normal': float(probability[0]) * 100,
            'probabilite_fraude': float(probability[1]) * 100,
            'verdict': "🚨 FRAUDE DÉTECTÉE" if prediction == 1 else "✓ Transaction normale"
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/stats')
def stats():
    """Page de statistiques"""
    return render_template('stats.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
