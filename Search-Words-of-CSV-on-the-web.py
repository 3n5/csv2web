import webbrowser
import csv

with open('C:/Users/USER/Desktop/test.csv', 'r', encoding='shift_jis') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for file in csv_reader:
        webbrowser.open(
            "https://www.google.com/search?q={}".format(','.join(file)))
print('ok')


