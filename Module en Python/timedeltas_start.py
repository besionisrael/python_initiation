#
# Fichier d'exemple pour le timedelta Objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Construire un basic timedelta et l'afficher
print(timedelta(days=365, hours=5, minutes=1))

# Afficher la date d'aujourd'hui
today = datetime.now() 

# Ajouter un an à la date actuelle
temps = today + timedelta(days=365)
print("Un an à partir d'aujourd'hui ", temps )

# créer un timedelta qui utilise plus d'un argument
temps = today + timedelta(weeks=2, days = 3)
print("Dans deux semaines et 3 jours, il sera: ", temps )

# calcule la date d'il y a une semaine, formatée comme un String
t = today - timedelta(weeks=1)
st = t.strftime("%A %B %d, %Y")
print("il y a une semaine, c'était le ", st)



### Combien de jours avant le poisson d'avril ?

## obtenir la date d'aujourd'hui
today = date.today()

nouvel_an = date(today.year, 1, 1)
diff = today - nouvel_an

print(diff.days, diff.min, diff.seconds)

## Obtenir la date du poisson d'avril pour la même année.



# utiliser la comparaison des dates pour voir si le poisson d'avril est déjà passé pour cette année.
#- Si c'est le cas, utilisez la fonction replace() pour obtenir la date de l'année prochaine.



# Maintenant, calculez le temps qu'il reste avant le poisson d'avril.  

