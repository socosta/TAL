import nltk
import string
import re
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os

#Importation du corpus
f = open('corpus__zombie.txt','r')
corpus = f.read()
f.close()

#Importation du lexique
f = open('lexique.txt','r')
lexique = f.readlines()
f.close()

#On nettoie les lexiques pour leur enlever '\n'
def nettoyer_lexique(lexique) :
    lexique2 = []
    for lignes in lexique:
        ligne=lignes.strip("\n")
        lexique2.append(ligne)
    return lexique2

lexique = nettoyer_lexique(lexique)

#Une fois le corpus importé, nous tokenisons ce dernier pour obtenir toutes les phrases.
def segmentation_phrase(corpus):
    tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    corpus_phrases=tokenizer.tokenize(corpus)
    return corpus_phrases

corpus_phrases = segmentation_phrase(corpus)

#Ensuite, on tri le corpus en gardant uniquement les phrases ayant une correspondance avec nos champs lexicaux
#Pour ce faire, on crée un programme qui prend un paramètre un mot d'un lexique
#Ainsi on regarde chaque phrase si elle contient un des mots au minimum
#Dans ce cas on la garde et on l'ajoute à corpus_triee
#On utilise une expression régulière pour indiquer que l'on cherche un mot à part
#On cherche 'rope' et non 'property'
def tri(corpus_de_base):
    f = open('corpus_triee.txt','r')
    corpus_triee = f.read()
    f.close()
    for phrase in corpus_de_base:
        ok = True
        for ligne in lexique:
            mot = re.compile(r"\b"+ligne+r"\b")
            if (mot.search(phrase)):
                if (ok):
                    f = open('corpus_triee.txt','a')
                    f.write(phrase+"\n")
                    f.close()
                    ok = False

#tri(corpus_phrases)

#On crée les entités nommés de chaque phrase du corpus trié grâce à stanford NER
def entitenomme():
    java_path = r'C:\Program Files\Java\jdk1.8.0_111\bin\java.exe'
    os.environ['JAVAHOME'] = java_path
    st = StanfordNERTagger('C:/Users/Thomaas/Downloads/stanford-ner-2014-06-16/classifiers/english.all.3class.distsim.crf.ser.gz',path_to_jar='C:/Users/Thomaas/Downloads/stanford-ner-2014-06-16/stanford-ner.jar',encoding='utf-8')
    f = open('corpus_triee.txt','r')
    corpus = f.readlines()
    f.close()
    f = open('corpus_entitenomme.txt','a')
    for lignes in corpus:
        tokenized_text = word_tokenize(lignes)
        classified_text = st.tag(tokenized_text)
        f.write(str(classified_text)+"\n")
    f.close()
        
#entitenomme()


#L'idée est de regarder si dans une phrase il y a plusieurs entité nommé "PERSON"
#Si c'est le cas on regarde grâce à notre lexique si entre ces deux "PERSON" un verbe correspondant à notre lexical de tueur s'y trouve.
def tueur():
    f = open('corpus_entitenomme.txt','r')
    corpus = f.readlines()
    i = 0
    for lignes in corpus:
        if ("PERSON" in lignes):
            i += 1
        if (i >= 2):
            print("Y'a un tueur dans cette phrase : "+lignes)

tueur()











