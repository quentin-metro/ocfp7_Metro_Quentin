# ocfp7_Metro_Quentin
ocfp7 - Résolvez des problèmes en utilisant des algorithmes en Python

## LIRE AVEC ATTENTION ET EN ENTIER AVANT DE TENTER QUOI QUE CE SOIT:
Programme d'algorithme de stratégies d'investissement, version bruteforce et optimisé à partir d'un fichier de donnée

## Prérequis, installation, déploiement:
- Pour télécharger la dernière version, cliquer ci-dessus: Code -> Download ZIP
- apres avoir téléchargé et extraire le ZIP dans un nouveau dossier
- assurer d'avoir une version à jour de 'python'
- Ouvrir un terminal de commandes et placez-vous dans le dossier du projet
- lancer l'environnement virtuel `.\env\Scripts\activate`
- lancer la commande `pip install -r requirements.txt` afin d'installer les packages nécessaire
- puis la commande `python .\bruteforce.py` pour la version bruteforce de l'algorithme.
- puis la commande `python .\optimized.py` pour la version bruteforce de l'algorithme.

## L'algorithme 
- Contient deux constantes modifiables `BUDGET_MAX` et `DATA_FILES`
- DATA_FILES permet de modifier le nom du fichier de donnée utilisé
  - paramétré par défaut à `dataset.csv`
- BUDGET_MAX défini le budget plafond pour l'algorithme

## Le fichier de donnée
- Celui-ci est nommé par défaut `dataset.csv` ou modifier la constante DATA_FILES
- Le fichier doit contenir trois colonnes correspondant à `name` `price` `profit`