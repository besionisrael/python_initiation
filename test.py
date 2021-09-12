t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet',  'Août',  'Septembre',  'Octobre',  'Novembre','Décembre']
list = []
newlist = []
for numero in range(0,len(t1)):
    newlist.append(t2[numero])
    newlist.append(t1[numero])
print(newlist)