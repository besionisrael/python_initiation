import pandas as pd


#### ECRITURE

# dico = {"Pays": ["France", "Canada", "Belgique"], "Ville": ["Paris", "Ottawa", "Bruxelles"]}

# df = pd.DataFrame(dico)
# #df.to_excel("test.xlsx")

# df.to_excel("test.xlsx", sheet_name="Pays", index = False)

# elmt1 = pd.DataFrame({"Noms": ["Henry", "Paul", "Eric"], "Salaire": ["5000", "2500", "3000"]})
# elmt2 = pd.DataFrame({"Noms": ["Thierry", "Amine", "Jerome"], "Salaire": ["5000", "2500", "3000"]})

# regroupement = {'Groupe1': elmt1, "Groupe2": elmt2}

# writer = pd.ExcelWriter("./test2.xlsx", engine="xlsxwriter")
# #writer = pd.ExcelWriter("./test3.csv", engine = )

# for in_groupe in regroupement.keys():
#     regroupement[in_groupe].to_excel(writer,sheet_name=in_groupe,index = False)
# writer.save()


#Lecture

cols = [0,1]
fichier = pd.read_excel("./mics.xlsx", usecols=cols)
try:
    xl = pd.ExcelFile("./mics.xlsx")
    print(xl.sheet_names)
except Exception as e:
    print("Fichier non trouvé")

df1 = pd.read_excel("./mics.xlsx", sheet_name=xl.sheet_names[0], header=None)
type(df1)

for x in df1.index:
    print(df1[0][x], df1[1][x],df1[2][x])
    if x > 6:
        break
#print(df1.head())





    



#les clés dans notre dictionnaire servira de nom de colonne. De même, le valeurs devenir les lignes contenant les informations.

#nous pouvons utiliser le to_excel() pour écrire le contenu dans un fichier



#sheet name



#Écriture de plusieurs DataFrames dans un fichier Excel

