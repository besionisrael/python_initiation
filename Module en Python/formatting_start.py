#
# Fichier d'exemple pour formatter l'affichage de la date et de l'heure
#


from datetime import datetime


def main():
  pass
  # Les heures et les dates peuvent être formatées à l'aide d'un ensemble de chaînes prédéfinies.
  # obtenir la date et l'heure actuelles

  now = datetime.now()
  
  
  #### Formattage de la Date  ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month

  ## Année complète avec siècle
  print(now.strftime("%a, %d %B, %y"))


  


  ## jour abrégé, num, mois complet, année abrégée


  
  ## %c - locale's date and time, %x - locale's date, %X - locale's time

  print(now.strftime("Date Local et time: %c"))
  print(now.strftime("Local Date %x"))



  
  #### Formattage Heure ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM

  print(now.strftime("Heure actuelle %I:%M:%S  %p"))

  ## 12-Hour:Minute:Second:AM


  ## 24-Hour:Minute



if __name__ == "__main__":
  main()
