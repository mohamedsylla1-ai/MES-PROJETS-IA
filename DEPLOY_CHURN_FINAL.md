🚀 DÉPLOIEMENT AUTOMATIQUE MONCHURNAI — ÉTAPES FINALE
==================================================

Le workflow GitHub Actions est maintenant actif. Dernière étape : ajouter votre token Railway as GitHub Secret.

## 📝 Ajouter le Token Railway à GitHub Secrets

1. Allez sur GitHub → votre repo MES-PROJETS-IA
2. Settings → Secrets and variables → Actions → New repository secret
3. Name : `RAILWAY_TOKEN`
4. Value : `36256c78-006c-455a-a1e6-2ef7e4b98f1b` (votre token)
5. Click "Add secret"

⚠️ IMPORTANT : Une fois ajouté, le token est **masqué** dans les logs. Ne le partagez plus jamais.

## ✅ Fonctionnement Automatique

Après avoir ajouté le secret :

- À chaque `git push origin main`, GitHub Actions déclenche le workflow
- Le workflow buildera et déploiera automatiquement sur Railway
- Surface : https://github.com/mohamedsylla1-ai/MES-PROJETS-IA → Actions (voir les logs)

## 🔍 Vérifier le Déploiement

### Via GitHub
- Repo → Actions → "Deploy monchurnai to Railway" → voir les logs en direct

### Via Railway
- https://railway.app → votre projet → Deployments → voir le nouveau déploiement

### URL Publique
Une fois déployé, votre site sera à :
`https://monchurnai-xxxxx.railway.app` (Railway ajoute un hash)

OU un domaine personnalisé si vous l'avez configuré dans Railway

## 🐛 Si ça ne marche pas

- **Workflow échoue** : Vérifiez que `RAILWAY_TOKEN` est bien ajouté dans GitHub Secrets
- **Railway ne reconnaît pas** : Vérifiez que le service Railway s'appelle `monchurnai` (ou changez dans le workflow)
- **Port/logs** : Railway → Deployments → cliquez sur le déploiement → View Logs

## 🎯 Résumé

✅ Workflow GitHub Actions créé (.github/workflows/deploy_churn.yml)
✅ Les fichiers churn sont isolés (pas de mélange avec fraude)
⏳ À faire : Ajouter `RAILWAY_TOKEN` aux GitHub Secrets
⏳ Puis : Pushez une modification pour tester le workflow (ou allez à Railway et redéployez manuellement)

---

**Une fois le secret ajouté, tout est automatique.** 🚀
Tous les pushes sur `main` déclencheront le déploiement churn sur Railway.
