# 📱 Prédiction Churn Client - Application Web

Une application web pour prédire le churn (départ) des clients télécommunications en utilisant le Machine Learning.

## 🎯 Fonctionnalités

✅ Prédiction en temps réel du risque de départ client  
✅ Interface moderne et responsive  
✅ Modèle Logistic Regression entraîné  
✅ API REST pour intégration  

## 🚀 Déploiement Rapide sur Railway

### App Churn (Nouvelle)

1. **Créer un nouveau projet Railway**
   - Allez sur https://railway.app
   - New Project → Deploy from GitHub
   - Sélectionnez `MES-PROJETS-IA`
   
2. **Configurer l'app Churn**
   - Settings → Environment
   - Ajouter variable : `PROCFILE_PATH=Procfile_churn`
   - OU modifier le Procfile pour utiliser `wsgi_churn.py`

3. **Alternative simple**
   - Créez un nouveau fichier `Procfile` temporaire avec :
     ```
     web: gunicorn wsgi_churn:app
     ```
   - Push et redeploy
   - Puis revenez au `Procfile` original pour l'app de fraude

## 📊 Structure pour 2 Applications

**Option A : Deux déploiements séparés sur Railway (Recommandé)**
```
Déploiement 1 (Fraude) :
- Procfile → wsgi:app (détection fraude)
- URL : https://fraud-app.railway.app

Déploiement 2 (Churn) :
- Procfile_churn → wsgi_churn:app (prédiction churn)
- URL : https://churn-app.railway.app
```

**Option B : Deux apps dans un seul dépôt (avancé)**
Créer un `app_main.py` qui route vers `/fraud` et `/churn`.

## 🧠 Modèle

- **Algorithme** : Logistic Regression
- **Accuracy** : ~85% (données synthétiques)
- **Features** : 9 variables client

## 📝 Variables d'Entrée

- `tenure` : Ancienneté (mois)
- `MonthlyCharges` : Frais mensuels (€)
- `TotalCharges` : Frais totaux (€)
- `Contract` : Type de contrat
- `InternetService` : Service internet
- `OnlineSecurity` : Sécurité en ligne
- Et autres...

## 🔌 API REST

**Endpoint** : `/predict` (POST)

```json
{
  "tenure": 24,
  "MonthlyCharges": 65.5,
  "TotalCharges": 1500,
  "Contract_Two year": 0,
  "InternetService_Fiber optic": 1,
  "OnlineSecurity": 1
}
```

**Réponse** :
```json
{
  "churn": 0,
  "probabilite_non_churn": 87.3,
  "probabilite_churn": 12.7,
  "verdict": "✓ Client stable"
}
```

---

**Version** : 1.0.0  
**Date** : Février 2026
