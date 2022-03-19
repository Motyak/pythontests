# yearprogress

## Description de la fonction
Donne la progression dans l'année d'une date

## Analyse technique

### Quoi ? (Que fait concrètement la fonction)
- Calcule le quotient de deux valeurs

### Comment ?
Quels arguments ?
- [x] Numéro de jour de l'année et nombre de jours dans l'année ?
- [ ] Date ? -- Jour, mois, année
  
Quels type de retour ?
- [ ] Nombre décimal ?
- [ ] Pourcentage ?
- [x] Aucun ? (affichage console)

Quel format (arguments) ?
- [ ] Nombre ?
- [x] Texte ?

### Exemples pertinents
|Id|Description|Entrée|Attendu|
|:-|-|-|-:|
|#1|premier jour d'une année|1;2019|0%|
|#2|dernier jour d'une année non-bissextile|365;2019|100%|
|#3|avant dernier jour d'une année non-bissextile|364;2019|99%|
|#4|avant dernier jour d'une année bissextile|365;2020|99%|
|#5|aujourd'hui|*aucune*|*progression d'aujourd'hui*|

### Stratégie de test
Pour les tests #1-4, on appelle la fonction à tester avec les paramètres en entrée et vérifie que la sortie corresponde à l'attendu.

Pour le test #5, on procède à 3 tests différents :
- Vérifier que la fonction retournant la date du jour appelle la fonction système prévue à cet effet
- Vérifier que la fonction système utilisée pour déterminer la date système donne le résultat escompté
- Vérifier que l'heure système est à l'heure
