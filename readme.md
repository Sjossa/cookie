Parfait Johnny, voici une version prête à mettre dans ton README, claire et concise pour que quelqu’un puisse installer ton jeu :

---

## Installation des dépendances

Pour jouer à **Cookie Clicker**, installez les bibliothèques nécessaires :

### 1. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv mon_env
```

### 2. Activer l’environnement

* **Linux / macOS** :

```bash
source mon_env/bin/activate
```

* **Windows** :

```bash
mon_env\Scripts\activate
```

### 3. Installer les dépendances

Si tu as un fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

Sinon, installer directement les dépendances minimales :

```bash
pip install pygame numpy Pillow
```

---

### 4. Lancer le jeu

```bash
python main.py
```
