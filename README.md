# Projet GIF-7001: Équipe 11

Répertoire de code officiel pour le projet final de l'équipe 11 dans le cours GIF-7001: "Vision Numérique".

## Installation initiale

Créez un environnement virtuel

`python3 -m venv ${YOUR_VENVS_DIR}/gif7001e11`

Activez le

`source ${YOUR_VENVS_DIR}/gif7001e11/bin/activate`

Installez les librairies requises

`pip3 install -r requirements.txt`

## Rouler le projet

Pour faire rouler le projet sur votre ordinateur personnel, il vous suffit désormais d'exécuter la commande

`python gesture_music_player.py`

Par défaut, le code ira lire le dossier `music` situé à la racine de votre projet pour obtenir son répertoire de chansons.
Le répertoire fourni contient des classiques des fêtes, mais vous pouvez modifier son contenu librement ou encore spécifier votre propre dossier contenant le répertoire de fichiers audio au format mp3 de votre choix :

`python gesture_music_player.py --path ${YOUR_FOLDER}`

Pour mettre un terme au programme, il suffit d'entrer la touche `q` sur le clavier.
