import random
import os
import csv
import codecs
from data import vowel_to_index
from data import Consonants_addr
cur_path = os.path.dirname(__file__)
csv_path = os.path.relpath('..\\resources\\IPAConnectivity.csv', cur_path)


def rw_handler():
    return


def gaussian_rw():
    return


def correlated_rw():
    return


def biased_rw():
    return


def ipa_consonant(character, direction):
    if character in NPClicks:
        return
    if character in NPVoImp:
        return
    if character in PCons:
        return


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


def ipa_vowel(character_address):
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

