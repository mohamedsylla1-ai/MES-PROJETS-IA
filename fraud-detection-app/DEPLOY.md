# 🚀 DÉPLOYER VOTRE SITE - Guide Rapide

## Vous avez 3 options :

### 🥇 OPTION 1 : Railway (RECOMMANDÉ) - 3 minutes
```
1. Aller sur railway.app
2. Sign Up with GitHub
3. New Project → Deploy from GitHub
4. Choisir "fraud-detection-app"
5. Cliquer Deploy
6. Copier l'URL générée
✅ Votre site est en ligne !
```

---

### 🥈 OPTION 2 : Render - 5 minutes
```
1. Aller sur render.com
2. Sign Up with GitHub
3. New Web Service
4. Connecter votre repo
5. Build Command: pip install -r requirements.txt && python train_model.py
6. Start Command: python app.py
7. Create Web Service
✅ Votre site est en ligne !
```

---

### 🥉 OPTION 3 : Heroku (Legacy)
```
heroku login
heroku create mon-app-fraude
git push heroku main
heroku open
✅ Votre site est en ligne !
```

---

## Après le déploiement :

- ✅ Votre site sera accessible 24/7
- ✅ URL publique à partager
- ✅ Tout le monde peut l'utiliser
- ✅ Modèle ML active sur le cloud

**Choisissez Railway si vous ne savez pas quoi faire ! C'est le plus simple. 🎯**

---

## Problèmes ?

Si le déploiement rate :
1. Vérifiez que `model.pkl` existe
2. Vérifiez que `requirements.txt` est à jour
3. Consultez les logs du déploiement
4. Contactez le support de la plateforme

**Bonne chance ! 🚀**
