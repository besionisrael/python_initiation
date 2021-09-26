#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime


def main():
  pass
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is ", today)


  # print out the date's individual components

  print("Composant d'une date:", today.day, today.month, today.year)

  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Le jour de la semaine", today.weekday())

  days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimance"]
  print("Le jour de la semaine", days[today.weekday()])

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("La date et l'heure actuelle", today)

  
  # Get the current time
  print("Le temps actuel", datetime.time(today))

 

  
if __name__ == "__main__":
  main()
  