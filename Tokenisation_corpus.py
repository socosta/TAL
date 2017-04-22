from __future__ import unicode_literals

import nltk
import os
import numpy
import nltk.corpus
from nltk.text import Text
import re
import sys
from nltk.tokenize import RegexpTokenizer

folder = nltk.data.find("C:\Users\Utilisateur\Documents\L3 MIASHS\SEMESTRE 6\INGENERIE LANGAGE\TAL-Lettre-D-master\TAL-Lettre-D")
read_corpus = nltk.corpus.PlaintextCorpusReader(folder, 'corpus_zombie.txt')

#On tokénise le corpus en phrase
nb_phrases = len(read_corpus.sents())
print("Notre corpus contient"+str(nb_phrases)+ "phrases")

#On tokénise le corpus en mots
nb_mots=len([word for sentence in read_corpus.sents() for word in sentence])
print("Notre corpus contient"+str(nb_mots)+"mots")

#On tokénise en caractère(lettres)
nb_car= ([char for sentence in read_corpus.sents() for word in sentence for char in word])
print("Notre corpus contient"+str(nb_car)+"caractères")
