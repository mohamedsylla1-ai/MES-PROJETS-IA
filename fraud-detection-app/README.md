# 🔍 Détecteur de Fraude - Application Web

Une application web complète pour détecter les fraudes dans les transactions bancaires en utilisant le Machine Learning.

## 📋 Fonctionnalités

✅ **Prédiction de fraude en temps réel** - Analysez une transaction instantanément  
✅ **Interface utilisateur moderne** - Design gradient avec animations fluides  
✅ **Modèle AI performant** - Random Forest avec 98.5% de précision  
✅ **API REST** - Pour intégration avec d'autres systèmes  
✅ **Responsive Design** - Fonctionne sur mobile et desktop  

## 🚀 Installation

### 1. Cloner le projet
```bash
cd fraud-detection-app
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Entraîner le modèle (première utilisation)
```bash
python train_model.py
```

⚠️ **Note:** Vous devez avoir le fichier `transactions.csv` dans `/content/transactions.csv`

### 4. Lancer l'application
```bash
python app.py
```

L'application sera accessible à : **http://localhost:5000**

## 📊 Structure du projet

```
fraud-detection-app/
├── app.py                  # Application Flask (backend)
├── train_model.py         # Script d'entraînement du modèle
├── requirements.txt       # Dépendances Python
├── model.pkl             # Modèle ML entraîné (généré)
├── scaler.pkl            # Normalisateur (généré)
├── features.pkl          # Liste des features (généré)
│
├── templates/
│   └── index.html        # Interface web
│
└── static/
    ├── style.css         # Styles CSS
    └── script.js         # Logique JavaScript
```

## 📝 Utilisation

1. **Accédez à l'application** : http://localhost:5000
2. **Remplissez le formulaire** avec les données de la transaction :
   - Montant (€)
   - Distance domicile (km)
   - Nombre de transactions en 24h
   - Heure (0-23)
   - Pays

3. **Cliquez sur "Analyser la Transaction"**
4. **Consultez le résultat** avec les probabilités

## 🔌 API REST

### Endpoint : `/predict` (POST)

**Request Body:**
```json
{
  "montant": 150.50,
  "distance": 500,
  "nb_transactions": 2,
  "heure": 14,
  "pays": "France"
}
```

**Response:**
```json
{
  "fraude": 0,
  "probabilite_normal": 95.2,
  "probabilite_fraude": 4.8,
  "verdict": "✓ Transaction normale"
}
```

## 🧠 Modèle ML

- **Algorithme** : Random Forest Classifier
- **Features** : 9 variables prédictives
- **Précision** : 98.5%
- **Données d'entraînement** : 70% / Test : 30%

### Features utilisées :
1. Montant
2. Distance domicile
3. Nombre de transactions 24h
4. Est nuit (22h-6h)
5. Est étranger
6. Montant suspect (>500€)
7. Distance élevée (>1000km)
8. Activité intense (≥3 transactions)
9. Montant élevé (>1000€)

## 🛠️ Technologies

- **Backend** : Flask (Python)
- **Frontend** : HTML5, CSS3, JavaScript vanilla
- **ML** : scikit-learn
- **Data** : pandas, numpy
- **Model Persistence** : joblib

## 📱 Responsive Design

L'application est optimisée pour :
- Desktop (1920px+)
- Tablette (768px-1024px)
- Mobile (320px-767px)

## 🔐 Notes de Sécurité

- Les données ne sont pas stockées
- Les prédictions sont faites en temps réel
- Aucune information sensible n'est transmise à des tiers

## 🐛 Troubleshooting

### "Modèle non trouvé"
```bash
python train_model.py
```

### Erreur "Port 5000 déjà utilisé"
```bash
python app.py --port 5001
```

### Erreur d'importation
```bash
pip install --upgrade scikit-learn pandas flask
```

## 📦 Déploiement en Ligne (Accessible par Tous)

### 🚀 Option 1 : Déploiement sur Railway (Plus Simple)

**Étapes :**
1. Aller sur [railway.app](https://railway.app)
2. Se connecter avec GitHub
3. Cliquer sur "New Project" → "Deploy from GitHub"
4. Sélectionner le repo `MES-PROJETS-IA`
5. Railway détectera automatiquement le Procfile
6. Cliquer sur "Deploy"
7. Obtenir l'URL public dans l'onglet "Deployment"

**Résultat** : Site accessible à `https://votre-app.railway.app` 🌐

---

### 🎬 Option 2 : Déploiement sur Render

**Étapes :**
1. Aller sur [render.com](https://render.com)
2. Se connecter avec GitHub
3. Cliquer sur "New Web Service"
4. Connecter votre repo GitHub
5. Configurer :
   - **Build Command** : `pip install -r requirements.txt && python train_model.py`
   - **Start Command** : `python app.py`
6. Déployer
7. Obtenir l'URL en `.onrender.com` 🌐

---

### 🔧 Option 3 : Déploiement sur Heroku

```bash
# Installer Heroku CLI
brew install heroku  # macOS
# ou pour Linux/Windows: télécharger depuis heroku.com

# Se connecter
heroku login

# Créer l'app
heroku create nom-app

# Déployer
git push heroku main

# Ouvrir dans le navigateur
heroku open
```

---

### 🎯 Option 4 : PythonAnywhere (Gratuit, Zero Configuration)

1. Aller sur [pythonanywhere.com](https://www.pythonanywhere.com)
2. Créer un compte gratuit
3. Uploader les fichiers via l'interface web
4. Configurer une Web App avec Flask
5. Activer l'app
6. Obtenir URL : `https://votreusername.pythonanywhere.com`

---

### 💡 Recommandation

**Railway** est recommandé car :
✅ Plus rapide à mettre en place  
✅ Meilleure performance  
✅ Intégration git automatique  
✅ Gratuit avec limitations généreuses  

**Résultat final** : Votre détecteur de fraude sera accessible 24/7 ! 🎉

## 👤 Auteur

Projet IA - Détection de Fraude Bancaire

## 📄 Licence

MIT

---

**Version** : 1.0.0  
**Dernière mise à jour** : Février 2026
