import random
import os
import csv
import codecs
from data import vowel_to_index, lang_data
from data import Consonants_addr
from csvhandler import confirm_language, phoneme_reader, vector_between_languages


cur_path = os.path.dirname(__file__)
csv_path = os.path.relpath('..\\resources\\IPAConnectivity.csv', cur_path)


def rw_main():
    while 1:
        steps = input("how many rounds of drift? \n\n  ")
        if int(steps) == 0 or int(steps) > 100:
            print("\n number must be higher than zero and less than one hundred")
            break

        starting_lang = input("starting language: \n\n  ")
        if not confirm_language(starting_lang):
            break

        rw_temp = input("what random walk model? \n\n  1 = Gaussian\n  2 = Correlated\n  "
                        "3 = Biased\n  4 = return\n  5 = quit \n\n  ")
        if rw_temp != '1' and rw_temp != '2' and rw_temp != '3' and rw_temp != '4' and rw_temp != '5':
            print("invalid entry")
            break

        if rw_temp == '1':
            print("running", steps, "steps of a Gaussian Random Walk on", starting_lang, "\n")
            rw_manager(steps, starting_lang, 1)
            break

        if rw_temp == '2':
            print("running", steps, "steps of a Correlated Random Walk on", starting_lang, "\n")
            rw_manager(steps, starting_lang, 2)
            break

        if rw_temp == '3':
            print("running", steps, "steps of a Gaussian Random Walk on", starting_lang, "\n")
            rw_manager(steps, starting_lang, 3)
            break

        if rw_temp == '4':
            break

        if rw_temp == 'q':
            quit()


def rw_manager(steps, lang, form):

    # first step is to turn all the phonemes into addresses
    alphabet = phoneme_reader(lang, lang_data[lang])
    addressed_pho_c = []
    addressed_pho_v = []
    for item in alphabet:
        if item in Consonants_addr:
            temp = address_cons(item, True)
            addressed_pho_c.append(temp)
        if item in vowel_to_index:
            temp = address_vowel(item, True)
            addressed_pho_v.append(temp)

    # repeat the loop for every step
    for i in range(0, int(steps)):
        j = 0
        for item in addressed_pho_c:
            t1 = item[1]
            t2 = item[2]
            temp = ipa_consonant(item, form)
            addressed_pho_c[j] = [temp, t1, t2]
            j += 1

        j = 0
        for item in addressed_pho_v:
            temp = ipa_vowel(item, form)
            addressed_pho_v[j] = int(temp)
            j += 1

    # get everything back to phoneme form
    new_c = []
    new_v = []
    for item in addressed_pho_c:
        new_c.append(address_cons(item, False))
    for item in addressed_pho_v:
        new_v.append(address_vowel(item, False))

    new_alphabet = new_v + new_c

    print("New phonemic aplhabet: \n",new_alphabet, "\n\n")
    print("vector between drift and", lang, "\n")

    vector_between_languages(lang, 'blank', True, new_alphabet)


def gaussian_rw():
    return


def correlated_rw():
    return


def biased_rw():
    return


def ipa_consonant(character_addr, rw):

    rand = random.randrange(-1,1)

    # Size of the section it can move within is stored at addr[2], making sure we don't walk off the end of our 'array'
    if 0 < int(character_addr[0]) < int(character_addr[2]):
        return character_addr[0] + rand
    if int(character_addr[0]) == int(character_addr[2]):
        return character_addr[0] - abs(rand)
    if int(character_addr[0]) == 0:
        return character_addr[0] + abs(rand)


def address_cons(var, direction):

    # send direction True and get consonant -> address. Send False and get address -> consonant
    # send a vowel for address, send a tuple for consonant
    if direction:
        if var in Consonants_addr:
            return Consonants_addr[var]

    if not direction:
        for key in Consonants_addr:
            if Consonants_addr[key] == var:
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
                temp = len(row)
                # below is where the function call to various RWs will happen
                migration = row[random.randrange(1, temp-1)]
                return migration
            i += 1

