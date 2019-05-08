from csvhandler import vector_between_languages, reader
from ipadirectional import rw_main
import os
import sys

sys.path.append(os.getcwd().index('src'))

cur_path = os.path.dirname(__file__)
csv_path = os.path.relpath('vowelconnectivity.csv', cur_path)


def main():
    print(("--------------------------------------------------------------------\n"
           "                  RANDOM WALKS AND PHONETIC DRIFT                   \n"
           "              A project by Robert Perez and Jacob Bloom             \n"
           "--------------------------------------------------------------------\n"))
    while 1:
        crsr = input("\n  1 = language difference vector \n"
                     "  2 = check language data, \n"
                     "  3 = random walk test \n"
                     "  4/q = quit \n \n ")
        if crsr == '1':
            lang1 = input("language from: ")
            lang2 = input("language to: ")
            blank = []
            vector_between_languages(lang1.lower(), lang2.lower(), False, blank)
        if crsr == '2':
            lang = input("what language would you like to find?")
            reader(lang.lower())
        if crsr == '3':
            rw_main()
        if crsr == '4' or crsr == 'q':
            quit()


main()
