# Kaio3

## Description
Kaio3 est un gestionnaire de multicompte pour Dofus qui permet de gérer facilement plusieurs fenêtres de jeu via des raccourcis clavier. Développé avec PyQt6, il offre une interface moderne et intuitive pour améliorer votre expérience de jeu multicopte.

## Fonctionnalités
- 🖥️ Gestion des fenêtres Dofus et Ankama Launcher
- ⌨️ Attribution de raccourcis clavier personnalisés
- 🔄 Rafraîchissement automatique de la liste des fenêtres
- 🔍 Filtre "Only Dofus" pour n'afficher que les fenêtres de jeu
- 🎯 Passage rapide entre les fenêtres via raccourcis
- 🖼️ **Gestion avancée des icônes Windows** (meilleure compatibilité, logos spéciaux pour Dofus et Ankama Launcher.)
- ❌ Fermeture facile des fenêtres depuis l'interface
- 💬 Accès rapide au serveur Discord de la communauté
- 🖱️ Interface redimensionnable et support du mode plein écran

## Installation
1. Téléchargez la dernière version de Kaio3.exe
2. Aucune installation nécessaire, le logiciel est portable
3. Double-cliquez sur Kaio3.exe pour lancer l'application

## Utilisation
1. Lancez Kaio3.exe
2. Attendez la fin de l'écran de chargement
3. La liste des fenêtres disponibles s'affiche automatiquement
4. Pour définir un raccourci :
   - Cliquez sur "Définir un raccourci" pour la fenêtre souhaitée
   - Appuyez sur la touche que vous voulez utiliser comme raccourci
   - Le raccourci est immédiatement actif
5. Utilisez la case à cocher "Only Dofus" pour filtrer uniquement les fenêtres Dofus
6. Le bouton "Refresh" permet de mettre à jour la liste des fenêtres
7. Cliquez sur l'icône Discord pour rejoindre la communauté

## Raccourcis
- Les raccourcis sont personnalisables pour chaque fenêtre
- Évitez d'utiliser les touches Ctrl, Alt, Shift et Windows seules
- Les raccourcis restent actifs même si Kaio3 est en arrière-plan
- Les raccourcis sont automatiquement supprimés à la fermeture des fenêtres

## Configuration requise
- Windows 10 ou supérieur
- Résolution d'écran minimale : 800x600
- Pas de droits administrateur requis

## Support et Communauté
- Discord : [Rejoindre le serveur](https://discord.gg/nAN5rTxfHA)
- Contact : ankou4 sur Discord

## Développement
Si vous souhaitez compiler le projet vous-même :

### Prérequis
```bash
pip install PyQt6
pip install pywin32
pip install keyboard
pip install pyinstaller
```

### Compilation
```bash
pyinstaller kaio3.spec
```

## Problèmes connus
- Certaines fenêtres système ou web peuvent ne pas afficher leur icône spécifique ou afficher une icône générique (limitation Windows).
- Les raccourcis peuvent nécessiter des droits administrateur sur certains systèmes.
- Pour les applications système, vous pouvez ajouter des icônes personnalisées dans le dossier de l'application (ex : `CalculatorIcon.png`, `SettingsIcon.png`).

## Conseils
- Pour une meilleure expérience visuelle, ajoutez vos propres icônes PNG dans le dossier de l'application et adaptez le code si besoin.

## Sécurité
- Le logiciel ne collecte aucune donnée
- Les raccourcis sont stockés uniquement en mémoire
- Aucune modification n'est apportée aux fichiers du jeu

## Licence
Copyright (c) 2024 Ankou. Tous droits réservés.

## Contact
Pour tout bug ou suggestion, contactez-moi sur Discord : **ankou4**

Pour un suivi optimal :
- Décrivez clairement le problème rencontré
- Précisez votre version de Windows
- Indiquez les étapes pour reproduire le bug
- Si possible, joignez une capture d'écran

## Notes
- Dofus est une marque déposée d'Ankama Games
- Kaio3 n'est pas affilié à Ankama Games
- Utilisez ce logiciel en conformité avec les conditions d'utilisation de Dofus 