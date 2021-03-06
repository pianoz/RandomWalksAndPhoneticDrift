import os
import csv
import codecs


# this file is only to create the datasets in data.py I keep it around in case I need to redo something, but there is no other reason for it.
def locate_languages():
    cur_path = os.path.dirname(__file__)
    csv_path = os.path.relpath('..\\resources\\phoible.csv', cur_path)

    dictonario = {}
    with codecs.open(csv_path, 'rb', encoding="utf-8") as phoible_csv:
        csv_reader = csv.reader(phoible_csv)

        # We are interested in glyphID and language name mostly
        i = 0
        lname = ''
        for row in csv_reader:
            if lname != row[3].lower():
                lname = row[3].lower()
                if not lname in dictonario:
                    dictonario[lname] = i
                # pstring = '"' + lname + '": "' + str(i) + '",'
            i += 1

    for items in dictonario:
        print('"' + str(items) + '": "' + str(dictonario[items]) + '",')


def test(data1, data2):
    with open("bigdata.csv", "a") as bigfile:
        string = data1 + "," + data2 + "," + '12' + "," + '12.2' + "\n"
        bigfile.write(string)


def testhandler():

    i =0
    while i < 10:
        data1 = "englsh" + str(i)
        data2 = "spanish" + str(i)
        test(data1, data2)
        i += 1

