texte1 = texte.split("--")
etudiant1 = texte1[0].split(";")
etudiant2 = texte1[1].split(";")
etudiant3 = texte1[2].split(";")
dico[etudiant1[0]] = {
	"nom": etudiant1[1],
	"prenom": etudiant1[2]
}
dico[etudiant2[0]] = {
	"nom": etudiant2[1],
	"prenom": etudiant2[2]
} 
dico[etudiant3[0]] = {
	"nom": etudiant3[1],
	"prenom": etudiant3[2]
}


 '''dico = {
 texte.split("--")[0].split(";")[0]:
 			{
 			"nom": texte.split("--")[0].split(";")[1],
 			"prenom": texte.split("--")[0].split(";")[2]
 			},
 texte.split("--")[1].split(";")[0]:
 			{
 			"nom": texte.split("--")[0].split(";")[0],
 			"prenom": texte.split("--")[0].split(";")[2]
 			},
 texte.split("--")[2].split(";")[0]:
 			{
 			"nom": texte.split("--")[2].split(";")[1],
 			"prenom": texte.split("--")[2].split(";")[2]
 			}
 }'''
