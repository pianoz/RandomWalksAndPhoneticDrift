import random
import os
import csv
import codecs
from data import vowel_to_index
from data import Consonants_addr
cur_path = os.path.dirname(__file__)
csv_path = os.path.relpath('..\\resources\\IPAConnectivity.csv', cur_path)


def rw_handler():
    while 1:
        menu = input("RANDOM WALK MODELER, press 1 to continue, press 2 to return")
        if menu == 1:
            steps = input("how many rounds of drift? ")
            starting_lang = input("starting language: ")
            rw_temp = input("what random walk model? \n 1 = Gaussian, 2 = Correlated, 3 = Biased, 4 = return, q = quit")

            if rw_temp == 1:
                print("running", steps, "of a Gaussian Random Walk on ", starting_lang, "\n")

            if rw_temp == 2:
                print("running", steps, "of a Correlated Random Walk on ", starting_lang, "\n")

            if rw_temp == 3:
                print("running", steps, "of a Gaussian Random Walk on ", starting_lang, "\n")

            if rw_temp == 4:
                break

            if rw_temp == 'q':
                quit()


def gaussian_rw():
    return


def correlated_rw():
    return


def biased_rw():
    return


def ipa_consonant(character_addr, rw):

    rand = random.randrange(-1,1)

    # Size of the section it can move within is stored at addr[2], making sure we don't walk off the end of our 'array'
    if character_addr[1] != character_addr[2] and character_addr[1] != 0:
        return character_addr + rand
    if character_addr[1] == character_addr[2]:
        return character_addr - abs(rand)
    if character_addr[1] == 0:
        return character_addr[1] + abs(rand)


def address_cons(var, direction):

    # send direction True and get consonant -> address. Send False and get address -> consonant
    # send a vowel for address, send a tuple for consonant
    if direction:
        if var in Consonants_addr:
            return Consonants_addr[var]

    if not direction:
        for key in Consonants_addr:
            if key == var:
                return key


def address_vowel(var, direction):

    # send direction True to get vowel -> address. Send False to get address -> vowel
    # make sure you are sending the right data type.
    if direction:
        return vowel_to_index[var]

    # yeah, going back takes some time.
    if not direction:
        with codecs.open(csv_path, 'rb', encoding="utf-8") as IPA_connectivity_graph:
            csv_reader = csv.reader(IPA_connectivity_graph)
            i = 0
            for row in csv_reader:
                if i == var - 1:
                    return row[0]
                i += 1


def ipa_vowel(character_address, rw):
    # To use this, simply input a vowel address.
    with codecs.open(csv_path, 'rb', encoding="utf-8") as IPA_connectivity_graph:
        csv_reader = csv.reader(IPA_connectivity_graph)

        # We look through the dictionary in 'data' for the location of that node on the IPA vowel connectivity chart
        # after we find it, we pick a random edge to pick from that node and travel on it, returning the new address
        # to be edited after RW styles are made.

        i = 0
        for row in csv_reader:
            if i == character_address - 1:
                temp = row.len()
                # below is where the function call to various RWs will happen
                migration = row[random.randrange(1, temp-1)]
                return migration
            i += 1

