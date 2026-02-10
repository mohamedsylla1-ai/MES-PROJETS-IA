#!/bin/bash

# 🚀 Script de déploiement sur Railway
# Exécuter ce script : bash deploy.sh

echo "🔍 Vérification de l'environnement..."

# Vérifier Git
if ! command -v git &> /dev/null; then
    echo "❌ Git n'est pas installé. Installez-le d'abord."
    exit 1
fi

# Vérifier que les fichiers pkl existent
if [ ! -f "model.pkl" ]; then
    echo "⚠️  Entraînement du modèle..."
    python train_model.py
fi

echo "✅ Tous les fichiers sont prêts !"
echo ""
echo "📋 Prochaines étapes :"
echo "1. Aller sur https://railway.app"
echo "2. Se connecter avec GitHub"
echo "3. Cliquer sur 'New Project' → 'Deploy from GitHub'"
echo "4. Sélectionner 'MES-PROJETS-IA'"
echo "5. Choisir le dossier 'fraud-detection-app'"
echo "6. Railway déploiera automatiquement !"
echo ""
echo "💡 Vous pouvez aussi faire un git push traditionnel :"
echo "   git add ."
echo "   git commit -m 'Deploy fraud detection app'"
echo "   git push origin main"
echo ""
echo "🎉 Votre site sera accessible depuis n'importe quel navigateur !"
