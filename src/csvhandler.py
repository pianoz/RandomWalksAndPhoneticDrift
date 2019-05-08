import os
import csv
import codecs
from data import lang_data
from similarity import find_similarity

# from termcolor import colored

# os.system('color')


cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in '%s': %s" % (cwd, files))
cur_path = os.path.dirname(__file__)
csv_path = os.path.relpath('phoible.csv', cur_path)


def alphabet(lang):

    alphabet = []
    value = lang_data.get(lang)
    print(value)

    with codecs.open(csv_path, 'rb', encoding="utf-8") as phoible_csv:
        csv_reader = csv.reader(phoible_csv)

        i = 0
        # yes, I know this is a non-optimal search pattern. It's not my fault Python's file read system is fucked.
        for row in csv_reader:
            # index row[3] is the language name. Read continues until it encounters a new language name.
            if row[3].lower() != lang and i > int(value):
                return
            if i >= int(value) and row[3].lower() == lang:
                print(row)
            i += 1
    return


def reader(language):
    # this will read out all the information for a single language, language name must be exact as it-
    # is the key. think about it like shitty SQL
    # Also, I tried but there really aren't any better keys than direct language name for our dataset.
    if confirm_language(language):

        # determines the phonemic set of languages
        with codecs.open(csv_path, 'rb', encoding="utf-8") as phoible_csv:
            csv_reader = csv.reader(phoible_csv)
            address = lang_data.get(language)
            i = 0
            lname = ''
            phn_list = []
            # alo_list = []

            for row in csv_reader:
                if i >= int(address):
                    # location of phonemes is 6, allophones are 7
                    phn_list.append(row[6])
                    # alo_list.append(row[6])
                    lname = row[3].lower()
                i += 1
                if lname != language and i > int(address):
                    break

            print(phn_list)


def confirm_language(language):
    # make sure the language exists in the database.
    if language.lower() in lang_data:
        return True
    else:
        print(language, " does not exist as an entry. check spelling or specificity.")
        return False


def phoneme_reader(lang, address):

    # determines the phonemic set of languages
    with codecs.open(csv_path, 'rb', encoding="utf-8") as phoible_csv:
        csv_reader = csv.reader(phoible_csv)

        i = 0
        lname = ''
        phn_list = []
        # alo_list = []
        for row in csv_reader:
            if i >= int(address):
                # location of phonemes is 6, allophones are 7
                phn_list.append(row[6])
                # alo_list.append(row[6])
                lname = row[3].lower()
            i += 1
            if lname != lang and i > int(address):
                break

        return phn_list


def vector_between_languages(lang1, lang2, trigger, blank):
    # os.system('color')

    # just a handler for the vector reader to make things more easy to read
    if confirm_language(lang1):
        lang1_index = lang_data.get(lang1)

        phn1 = phoneme_reader(lang1, lang1_index)

        if trigger:
            phn2 = blank

        if not trigger:
            if not confirm_language(lang2):
                return
            if confirm_language(lang2):
                lang2_index = lang_data.get(lang2)
                phn2 = phoneme_reader(lang2, lang2_index)


        # using some python set stuff here
        print("loss from language 1: ", set(phn1) - set(phn2))
        print("gain in language 2: ", set(phn2)-set(phn1), "\n")

        find_similarity(set(phn1) - set(phn2), set(phn2)-set(phn1))

        # print(colored(("loss from language 1: ", set(phn1)-set(phn2)), 'red'))
        # print(colored(("gain in language 2: ", set(phn2)-set(phn1)), 'blue'))


def csvmain():
    blank = []
    while(1):
        find = input("1 = print language data, 2 = compare language vector, 3 = return, q = quit")
        if find == '1':
            lang = input("what language would you like to find?")
            reader(lang.lower())
        if find == '2':
            lang1 = input("language from: ")
            lang2 = input("language to: ")
            vector_between_languages(lang1.lower(), lang2.lower(), False, blank)
        if find == '3':
            break

        if find == 'q':
            quit()
