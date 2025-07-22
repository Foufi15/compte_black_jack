# 🃏 Blackjack — Projet NSI

### 🎮 Un mini-jeu de blackjack avec affichage des cartes et système de comptage

---

## 📌 Présentation

Ce projet est une application en Python qui simule un mini-jeu de **blackjack en solo**, avec les éléments suivants :

- Affichage des cartes via **`pygame`**
- Interaction utilisateur via **`customtkinter`**
- Système de **comptage des cartes** basé sur la méthode Hi-Lo
- Interface moderne et responsive
- Option pour ajuster la vitesse d'apparition des cartes

> Projet réalisé dans le cadre du cours de NSI (Numérique et Sciences Informatiques).

---

## 🛠️ Technologies utilisées

- Python `3.12`
- [`pygame`](https://www.pygame.org/)
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)
- Interface graphique + affichage plein écran

---

## 📂 Structure du projet

```
projet/
│
├── black-jack.py        # Fichier principal du jeu
├── README.md            # Ce fichier
├── /projet              # Dossier contenant les images de cartes
│   ├── 2 de coeur.jpg
│   ├── As de carreau.jpg
│   └── etc.
```

---

## 📸 Fonctionnalités

- 🎴 Cartes tirées aléatoirement
- 🧠 Compte automatique basé sur la valeur Hi-Lo :
  - Cartes 2–6 → +1
  - Cartes 7–9 → 0
  - Cartes 10–As → -1
- ⌛ Vitesse réglable (temps d'apparition des cartes)
- ✅ Vérification manuelle du résultat par le joueur
- 🌙 Interface stylée (Dark Mode)

---

## 🚀 Lancer le projet

### 1. Prérequis

Assurez-vous d’avoir **Python 3.12** installé sur votre machine.

### 2. Installer les dépendances

```bash
pip install pygame customtkinter
```

### 3. Lancer le jeu

```bash
python black-jack.py
```

---

## 🎯 Règles simplifiées du comptage de cartes (Hi-Lo)

Le système Hi-Lo permet de suivre les cartes hautes et basses :

| Carte          | Valeur Hi-Lo |
|----------------|---------------|
| 2 à 6          | +1            |
| 7 à 9          | 0             |
| 10, J, Q, K, A | -1            |

Un **compte positif** indique que les cartes restantes favorisent le joueur.

---

## 👨‍💻 Auteurs

- [Votre Prénom/Nom]
- Projet NSI 2025

---

## 📃 Licence

Ce projet est open-source dans un but éducatif.

