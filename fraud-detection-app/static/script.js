document.getElementById('fraudForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Récupérer les données du formulaire
    const formData = {
        montant: document.getElementById('montant').value,
        distance: document.getElementById('distance').value,
        nb_transactions: document.getElementById('nb_transactions').value,
        heure: document.getElementById('heure').value,
        pays: document.getElementById('pays').value
    };
    
    // Envoyer la prédiction
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            throw new Error('Erreur lors de la prédiction');
        }
        
        const result = await response.json();
        
        // Afficher les résultats
        displayResults(result, formData);
        
    } catch (error) {
        displayError(error.message);
    }
});

function displayResults(result, formData) {
    // Masquer la section d'erreur
    document.getElementById('errorSection').classList.add('hidden');
    
    // Afficher la section de résultats
    const resultSection = document.getElementById('resultSection');
    resultSection.classList.remove('hidden');
    
    // Verdict
    const verdict = document.getElementById('verdict');
    if (result.fraude === 1) {
        verdict.textContent = result.verdict;
        verdict.className = 'verdict fraude';
    } else {
        verdict.textContent = result.verdict;
        verdict.className = 'verdict normal';
    }
    
    // Probabilités
    const probNormal = result.probabilite_normal;
    const probFraude = result.probabilite_fraude;
    
    document.getElementById('probNormal').style.width = probNormal + '%';
    document.getElementById('probNormalText').textContent = probNormal.toFixed(1) + '%';
    
    document.getElementById('probFraude').style.width = probFraude + '%';
    document.getElementById('probFraudeText').textContent = probFraude.toFixed(1) + '%';
    
    // Résumé
    document.getElementById('summaryMontant').textContent = parseFloat(formData.montant).toFixed(2);
    document.getElementById('summaryDistance').textContent = formData.distance;
    document.getElementById('summaryTransactions').textContent = formData.nb_transactions;
    document.getElementById('summaryHeure').textContent = formData.heure;
    document.getElementById('summaryPays').textContent = formData.pays;
    
    // Scroll vers les résultats
    resultSection.scrollIntoView({ behavior: 'smooth' });
}

function displayError(errorMessage) {
    // Masquer la section de résultats
    document.getElementById('resultSection').classList.add('hidden');
    
    // Afficher la section d'erreur
    const errorSection = document.getElementById('errorSection');
    document.getElementById('errorMessage').textContent = '❌ Erreur: ' + errorMessage;
    errorSection.classList.remove('hidden');
    
    // Scroll vers l'erreur
    errorSection.scrollIntoView({ behavior: 'smooth' });
}

// Validation en temps réel
document.getElementById('heure').addEventListener('change', function() {
    const value = parseInt(this.value);
    if (value < 0 || value > 23) {
        alert('L\'heure doit être entre 0 et 23');
        this.value = '';
    }
});

document.getElementById('montant').addEventListener('input', function() {
    if (parseFloat(this.value) < 0) {
        this.value = '';
    }
});

document.getElementById('distance').addEventListener('input', function() {
    if (parseFloat(this.value) < 0) {
        this.value = '';
    }
});

document.getElementById('nb_transactions').addEventListener('input', function() {
    if (parseInt(this.value) < 0) {
        this.value = '';
    }
});
