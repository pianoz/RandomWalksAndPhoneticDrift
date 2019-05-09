from data import Consonants_addr, vowel_to_index
import codecs
import os
import csv
from statistics import stdev, variance
# from ipadirectional import address_cons

cur_path = os.path.dirname(__file__)
csv_path = os.path.relpath('vowelconnectivity.csv', cur_path)


def return_largest(list1, list2):
    if len(list1) >= len(list2):
        return list1
    else:
        return list2


def return_smaller(list1, list2):
    if len(list1) < len(list2):
        return list1
    else:
        return list2


def vowel_sim_handler(vowel_1, vowel_2):
    # breadth first search from vowel_1 to vowel_2. return the degrees of separation. Vowels are stored in a graph-
    # -style

    add_vowel_1 = address_vowel(vowel_1, True)
    add_vowel_2 = address_vowel(vowel_2, True)
    explored_nodes = [add_vowel_1]

    if add_vowel_1 == add_vowel_2:
        return 0
    else:
        i = 0
        recursive_distance = vowel_recur(add_vowel_1, add_vowel_2, i, explored_nodes)
        return recursive_distance


def vowel_recur(vowel_add, target_add, count, explored_nodes):
    explored_nodes.append(vowel_add)
    count += 1
    checklist = []
    with codecs.open(csv_path, 'rb', encoding="utf-8") as IPA_connectivity_graph:
        csv_reader = csv.reader(IPA_connectivity_graph)
        i = 0
        for row in csv_reader:
            if i == int(vowel_add) - 1:
                checklist = row
                break
            i += 1
    checklist.pop(0)
    for i in checklist:
        if int(i) == target_add:
            return count
    if count < 10:
        for i in checklist:
            if i not in explored_nodes:
                return vowel_recur(i, target_add, count, explored_nodes)
    else:
        return count


def cons_sim_handler(cons_1, cons_2):
    temp1 = Consonants_addr[cons_1]
    temp2 = Consonants_addr[cons_2]
    if temp1[1] != temp2[1]:
        return 20
    else:
        return abs(temp1[0]-temp2[0])


def check_phoneme_classification(phoneme):
    if phoneme in Consonants_addr:
        return 0
    elif phoneme in vowel_to_index:
        return 1
    else:
        return 2


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


def erase_101(vector_list):
    i = 0
    for item in vector_list:
        if int(item) == 101 or int(item) == 20:
            vector_list[i] = 1
        i += 1
    return vector_list


def printer(lang1, lang2, avg, stddev, vari, _sum, trigger2, step=0):
    if trigger2:
        with open("walkdata.csv", "a", encoding='utf-8') as bigfile:
            string = lang1 + "," + str(step) + "," + str(avg) + "," + str(stddev) + ',' + str(vari) + ',' + str(_sum) + "\n"
            bigfile.write(string)
    else:
        with open("bigdata.csv", "a", encoding='utf-8') as bigfile:
            string = lang1 + "," + lang2 + "," + str(avg) + "," + str(stddev) + ',' + str(vari) + ',' + str(_sum) + "\n"
            bigfile.write(string)


def find_similarity(lost, gained, trigger, lang1, lang2, trigger2=False, step=0):
    # to check similarity, find if it is a vowel or consonant first, then do a for loop
    # for all of the items on the lost phonemes list and return the most similar. The degrees of separation is the
    # sum, the average separation is the average of these distances.

    # 101 is just a placeholder that I know will be higher than any actual possible value. It is erased if it still
    # remains in the list at the end, which is possible.
    numerical_similarity_vector = [101]*max(len(lost), len(gained))

    i = 0

    larger = return_largest(lost, gained)
    smaller = return_smaller(lost, gained)
    diff = len(larger)-len(smaller)

    for item_gained in smaller:
        gained_class = check_phoneme_classification(item_gained)
        for item_lost in larger:
            lost_class = check_phoneme_classification(item_lost)

            # if both are consonants
            if lost_class == 0 and lost_class == gained_class:
                # save similarity score, test to see if it is shorter than the last.
                tempc = cons_sim_handler(item_gained, item_lost)
                if numerical_similarity_vector[i] > tempc:
                    numerical_similarity_vector[i] = tempc

            # if both are vowels
            if lost_class == 1 and lost_class == gained_class:
                # Do the same but for vowels.
                tempv = vowel_sim_handler(item_gained, item_lost)
                if numerical_similarity_vector[i] > tempv:
                    numerical_similarity_vector[i] = tempv
        i += 1
    numerical_similarity_vector = erase_101(numerical_similarity_vector)

    average = round((sum(numerical_similarity_vector) + diff)/len(larger), 4)
    try:
        standard_dev = round(stdev(numerical_similarity_vector, average), 4)
    except AssertionError:
        print("values are uniform, no standard dev")
        standard_dev = 'NaN'

    try:
        vari = round(variance(numerical_similarity_vector), 4)
    except AssertionError:
        print("values are uniform, no variance")
        vari = 'NaN'

    _sum = sum(numerical_similarity_vector) + diff

    print(average, "Average separation of phonemes")
    print(standard_dev, "Standard Deviation")
    print(vari, "Variance")
    print(_sum, "Total separation\n")

    if trigger or trigger2:
        printer(lang1, lang2, average, standard_dev, vari, _sum, trigger2, step)

    return
