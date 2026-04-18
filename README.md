# RobynMMM — Marketing Mix Modelling · Ekimetrics MCE

> **Analyse de l'efficacité media et optimisation budgétaire pour une marque FMCG**
>
> Dataset Robyn (Meta) · 4 ans · 5 canaux media · Approche consultant MCE

---

## Contexte business

Une marque FMCG investit chaque semaine dans 5 canaux media (TV, OOH, Print, Facebook, Search). La question centrale : **quel canal génère vraiment des ventes, et comment redistribuer le budget pour maximiser le ROI ?**

Ce projet reproduit une mission type **Business Scientist MCE** chez Ekimetrics — de l'ingestion des données brutes jusqu'à la recommandation d'allocation budgétaire présentée au client.

---

## Dataset

**Source :** [Robyn — Meta Open Source](https://github.com/facebookexperimental/Robyn)

| Variable | Description |
|---|---|
| `revenue` | Ventes hebdomadaires (variable réponse) |
| `tv_spend` | Dépenses TV |
| `ooh_spend` | Dépenses Out-of-Home |
| `print_spend` | Dépenses Print |
| `facebook_spend` | Dépenses Facebook/Meta |
| `search_spend` | Dépenses Search (Google) |
| `price_index` | Indice de prix |
| `promotion` | Semaines promotionnelles |
| `events` | Événements saisonniers |

208 semaines · Janvier 2018 → Décembre 2021

---

## Architecture du projet

```
RobynMMM/
├── data/
│   ├── raw/
│   │   └── dt_simulated_weekly.csv   # Dataset Robyn original
│   └── processed/                    # Features transformées
├── notebooks/
│   ├── 01_EDA.ipynb                  # Exploration & statistiques descriptives
│   ├── 02_features.ipynb             # Adstock & saturation
│   ├── 03_model_ols.ipynb            # Régression OLS (statsmodels)
│   ├── 04_model_bayes.ipynb          # Régression bayésienne (PyMC)
│   ├── 05_decomposition.ipynb        # Décomposition des ventes
│   ├── 06_roi_analysis.ipynb         # ROI & ROAS par canal
│   ├── 07_optimization.ipynb         # Optimisation budgétaire
│   └── 08_what_if.ipynb              # Simulations scénarios
├── src/
│   ├── config.py                     # Paramètres globaux
│   ├── data_loader.py                # Chargement & validation données
│   ├── adstock.py                    # Transformations adstock
│   ├── saturation.py                 # Fonctions de saturation (Hill)
│   ├── mmm_model.py                  # Pipeline modélisation
│   ├── optimizer.py                  # Optimisation budgétaire (scipy)
│   ├── metrics.py                    # ROAS, ROI, diagnostics
│   └── plots.py                      # Visualisations consultant
├── app/
│   └── streamlit_app.py              # Dashboard interactif
├── outputs/
│   ├── figures/                      # Graphiques exportés
│   ├── models/                       # Modèles sauvegardés
│   └── reports/                      # Rapports client
├── requirements.txt
└── README.md
```

---

## Concepts MMM implémentés

### Adstock — mémoire de la publicité
L'effet d'une campagne ne disparaît pas instantanément. Le modèle de Koyck (geometric decay) capture cette persistance :

```
adstock(t) = spend(t) + λ × adstock(t−1)
```

où λ ∈ (0,1) est le taux de rétention. Une TV avec λ=0.65 signifie que 65% de l'effet de la semaine passée persiste la semaine suivante.

### Saturation — rendement décroissant
Au-delà d'un certain seuil, investir davantage dans un canal génère de moins en moins de ventes. On modélise cela via la **Hill function** :

```
saturation(x) = xᵅ / (xᵅ + γᵅ)
```

où γ est le point d'inflexion (budget optimal) et α contrôle la forme de la courbe.

### Modèle MMM

```
revenue(t) = baseline
           + β_TV      × sat(adstock(TV, λ_TV))
           + β_OOH     × sat(adstock(OOH, λ_OOH))
           + β_Print   × sat(adstock(Print, λ_Print))
           + β_Facebook× sat(adstock(FB, λ_FB))
           + β_Search  × sat(adstock(Search, λ_Search))
           + γ_price   × price_index
           + γ_promo   × promotion
           + saisonnalité + ε
```

---

## Outputs & livrables

| Output | Description | Notebook |
|---|---|---|
| Décomposition des ventes | Baseline vs contribution de chaque canal | 05 |
| ROAS par canal | €ventes générées par €investi | 06 |
| Courbes de saturation | Point optimal d'investissement | 06 |
| Budget optimal | Allocation qui maximise les ventes sous contrainte | 07 |
| Simulation what-if | Impact d'un réallocations budgétaire | 08 |

---

## Installation

```bash
git clone https://github.com/SouhaiLOps/RobynMMM.git
cd RobynMMM
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

---

## Stack technique

| Usage | Librairie |
|---|---|
| Manipulation données | `pandas` · `numpy` |
| Modèle classique | `statsmodels` |
| Modèle bayésien | `pymc` · `arviz` |
| Optimisation | `scipy.optimize` |
| Visualisation | `matplotlib` · `plotly` · `seaborn` |
| Dashboard | `streamlit` |

---

## Contexte

Projet réalisé dans le cadre de la préparation au poste **Business Scientist MCE** chez **Ekimetrics** — leader européen du Marketing Mix Modelling.

L'objectif est de reproduire une mission consultant complète : de l'analyse exploratoire jusqu'à la recommandation d'allocation budgétaire, en passant par la modélisation économétrique et l'interprétation business des résultats.