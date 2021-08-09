#
# Fichier d'exemple pour le timedelta Objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Construire un basic timedelta et l'afficher
print (timedelta(days=365, hours=5, minutes=1))

# Afficher la date d'aujourd'hui 
now = datetime.now()
print ("today is: " + str(now))

# Ajouter un an à la date actuelle
print ("Un an à partir d'aujourd'hui sera: " + str(now + timedelta(days=365)))

# créer un timedelta qui utilise plus d'un argument
print ("Dans deux semaines et 3 jours, il sera: " + str(now + timedelta(weeks=2, days=3)))

# calcule la date d'il y a une semaine, formatée comme un String
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print ("Il y a une semaine, c'etait le  " + s)

### Combien de jours avant le poisson d'avril ?

# obtenir la date d'aujourd'hui
today = date.today()
# Obtenir la date du poisson d'avril pour la même année.
afd = date(today.year, 4, 1)  
# utiliser la comparaison des dates pour voir si le poisson d'avril est déjà passé pour cette année.
# Si c'est le cas, utilisez la fonction replace() pour obtenir la date de l'année prochaine.
if afd < today:
  print ("Le poisson d'avril est déjà passé il y a %d jours." % ((today-afd).days))
  # si oui, obtenir la date pour l'année prochaine
  afd = afd.replace(year=today.year + 1) 

# Maintenant, calculez le temps qu'il reste avant le poisson d'avril.  
time_to_afd = afd - today
print ("il reste", time_to_afd.days, "jours jusqu'au poisson d'avril!")

