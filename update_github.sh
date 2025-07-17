#!/bin/bash

# Ajoute tous les fichiers modifiés
git add .

# Vérifie s'il y a des modifications à commiter
if git diff-index --quiet HEAD -- ; then
    echo "Aucune modification détectée – rien à pousser"
    exit 0
fi

# Si des modifications sont présentes, fait un commit avec date
echo "Des modifications détectées – commit en cours..."
git commit -m "Mise à jour $(date '+%Y-%m-%d %H:%M')"

# Pousse sur GitHub (via SSH)
git push origin master

echo "Mise à jour poussée sur GitHub"