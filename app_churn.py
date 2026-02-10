from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os
from pathlib import Path

app = Flask(__name__)

APP_DIR = Path(__file__).parent
model = None
scaler = None
features = None

try:
    model = joblib.load(str(APP_DIR / 'churn_model.pkl'))
    scaler = joblib.load(str(APP_DIR / 'churn_scaler.pkl'))
    features = joblib.load(str(APP_DIR / 'churn_features.pkl'))
    print("✓ Modèle de churn chargé avec succès")
except Exception as e:
    print(f"❌ Erreur: {e}")

@app.route('/')
def index():
    return render_template('churn_index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Modèle non disponible'}), 500
    
    try:
        data = request.json
        
        input_data = []
        for feature in features:
            if feature in data:
                value = float(data[feature])
            else:
                value = 0.0
            input_data.append(value)
        
        input_array = np.array([input_data])
        
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0]
        
        return jsonify({
            'churn': int(prediction),
            'probabilite_non_churn': float(probability[0]) * 100,
            'probabilite_churn': float(probability[1]) * 100,
            'verdict': "⚠️ RISQUE DE CHURN" if prediction == 1 else "✓ Client stable"
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
