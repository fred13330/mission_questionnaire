
import json

class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def fromjsondata(questionnaire):
        question = questionnaire["titre"]
        liste_choix = [i[0] for i in questionnaire["choix"]]
        reponse_correcte = [i[0] for i in questionnaire["choix"] if i[1]]
        q = Question(question, liste_choix, reponse_correcte[0])
        return q


    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score

def load_file(file):
    file = open(file, "r")
    data = file.read()
    file.close()
    return json.loads(data)
    

""" def creer_questionnaire_formate(questionnaire):
    question_formatee = []
    questionnaire_formate = []
    questions = questionnaire["questions"]
 """
    
    
    
questionnaire_jeu = ()

questionnaire_json = load_file("animaux_leschats_confirme.json")
questionnaire = questionnaire_json["questions"]
# questionnaire = creer_questionnaire_formate(questionnaire)
# categorie = questionnaire["categorie"]
# titre = questionnaire["titre"]
# difficulte = questionnaire["difficulte"]

q = Question.fromjsondata(questionnaire[0])

q.poser()

# Questionnaire(questionnaire_jeu).lancer()
