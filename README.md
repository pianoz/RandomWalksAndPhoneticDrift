## Random Walks And Phonetic Drift
A program designed to check the statistical difference between languages, and use random walks to model shifts in their phonetics.

# Overall Design:
Program does a statistical analysis on different spoken languages to tell the difference between them. This is based on a model where vowels shift along a graph data-set, and consonants can move between vocalization placement but not their manner of articulation (i.e. plosive, nasal, etc.) this information can be more easily visualized with the graphs available at www.internationalphoneticassosciation.org 

In order to run the code, simply install and then navigate to the src folder. Once there, type 
#$ python3 main.py 
into the terminal. That should bring it right up. it doesn't use any esoteric libraries, so the native install of python should be be able to run it witout any module installation. 
