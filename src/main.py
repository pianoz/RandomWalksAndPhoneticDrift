from csvhandler import vector_between_languages, reader, confirm_language
from ipadirectional import rw_main
from data import testing_languages
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
                     "  4/q = quit \n "
                     "  5 = CHECKALL \n \n ")
        if crsr == '1':
            lang1 = input("language from: ")
            lang2 = input("language to: ")
            blank = []
            vector_between_languages(lang1.lower(), lang2.lower(), False, blank, False)
        if crsr == '2':
            lang = input("what language would you like to find?")
            reader(lang.lower())
        if crsr == '3':
            rw_main()
        if crsr == '4' or crsr == 'q':
            quit()
        if crsr == '5':
            last_chance = input("Are you sure? This will take a long time to run. Y/N")
            if last_chance == 'Y':
                big_boy_handler()


def big_boy_handler():
    count = 0
    for items in testing_languages:
        if confirm_language(items):
            for jtems in testing_languages:
                if confirm_language(jtems):
                    print("Testing", count, "/11449 non-Indian Indo-European languages")
                    if items != jtems:

                        blank =[]
                        vector_between_languages(items, jtems, False, blank, True)
                count += 1
        count += 1
    return

main()
