import webbrowser
import csv

with open('C:/Users/USER/Desktop/test.csv', 'r', encoding='shift_jis') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    #browser = webbrowser.get('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" %s')
    for file in csv_reader:
        webbrowser.open(
            "{}".format(','.join(file)))
print('fin')


