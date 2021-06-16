'''
Todo:
Load and process the spreadsheet: Done!
Create the Main Page: Done!
Create the Sub Pages: Not Started

Remember: In the Main page code, you commented out user input to run the code more easily. Put it back. Please.
'''

import csv
import os

# Numerical values for your pleasure
players = 20
chainlength = 13

# Be sure to put commas and a space after every number of the chain you wish to exclude. If you want to exclude the Main page, put a 0.
chainexclude = [3]
# If you only want specific pages, the use this instead. Like the above, 0 is the Main page.
chaininclude = []

# The following extracts and converts all the information into a useable format.

chainlist = []
contentlist = []

'''
in_ex should be used to indicate whether we are including, excluding, or doing nothing to the chains.
0 = Nothing
1 = Include
2 = Exclude
'''


if chaininclude != []:
    setchain = set(chaininclude)
    in_ex = 1
elif chainexclude != []:
    setchain = set(chainexclude)
    in_ex = 2
else:
    setchain = set()
    in_ex = 0


with open('chainsheet.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    linecount = 0
    for row in reader:
        if linecount == 0:
            linecount = linecount + 1
            continue
        if linecount % 2 == 0:
            contentlist.append(row)
        else:
            chainlist.append(row)
        linecount = linecount + 1

chainnames = []
for x in range(0, players):
    chainnames.append(chainlist[x].pop(0))
    del contentlist[x][0]
for x in range(0, players):
    for y in range(0, players):
        if chainlist[x].count('') > 0:
            chainlist[x].remove('')
        if contentlist[x].count('') > 0:
            contentlist[x].remove('')
            



absolute_path = os.path.abspath(__file__)
absolute_path = os.path.dirname(absolute_path)
WikiPage = os.path.join(absolute_path, 'WikiPage') # This should be the path to a folder which will have our text files.
SubPage = os.path.join(WikiPage, 'SubPages')

if not os.path.isdir(SubPage):
    os.makedirs(SubPage)
  

print('Step 1 complete!')
# The following creates the Main Page.
createmain = 0
WikiPage = os.path.join(WikiPage, 'WikiPage.txt')
if in_ex == 0:
    createmain = 1
elif in_ex == 1:
    if 0 in setchain:
        createmain = 1
else:
    if 0 not in setchain:
        createmain = 1
if createmain == 1:
    '''
    url = input("What is your game's url? ")
    name = input("What is your game's name? ")
    host = input("What is your username? ")
    datestart = input("What month did your game start? ")
    datestop = input("What month did your game end? ")
    year = input("What year did it take place? ")
    description = input("What description would you like to add? ")
    '''
    url = 'https://forum.mafiascum.net/viewtopic.php?f=61&t=86676'
    name = 'Gramophone Pictureka'
    host = 'Jake The Wolfie'
    datestart = 'June'
    datestop = 'July'
    year = '1994'
    description = 'Nothing Happened.'
    Part1 = ['\n', '\n', '==The Player List==', '\n', '{{multicol}}', '\n']
    Part2 = ['{{multicol-end}}', '\n', '\n', '==The Chains==', '\n', '\n', '\n', '{| style="border:0px !important;border-spacing:15px;"', '\n']
    Part3 = ['|}', '\n', '[[Category:Mish Mash]]']
    with open(WikiPage, 'w') as mainpage:
        # Preparing the text file
        if  datestart != datestop:
            mainpage.write("[" + url + " Telephone Pictionary:" + name + "] is a game of [[Telephone Pictionary]] run by {{U|" + host + "}} started in " + datestart + " and ended in " + datestop + ", " + year + ". " + description)
        else:
            mainpage.write("[" + url + " Telephone Pictionary:" + name + "] is a game of [[Telephone Pictionary]] run by {{U|" + host + "}} in " + datestart + " " + year + ". " + description)
        mainpage.writelines(Part1)
        # Writing down the player list
        for x in range(0, players):

            mainpage.write("'''" + str(x + 1) + ".''' " + '{{U|' + str(chainlist[x][0]) + '}}<br/>')

            mainpage.write('\n')
            if (x + 1) % 10 == 0:
                if x != players:
                    mainpage.write('{{multicol-break}}')
                    mainpage.write('\n')
        mainpage.writelines(Part2)
        # Writing down all the chains
        numblist = 0
        for x in range(0, players):
            if numblist == 0:
                Letter = 'A'
                b = bytes(Letter, 'utf-8')
                b = b[0] + x
                Letter = chr(b)
                if Letter == 'Z':
                    numblist = 1
            else:
                Letter = '1'
                Letter = int(Letter)
                Letter = Letter + (x - 26)
                Letter = str(Letter)

            mainpage.write("| '''<span style=" + "font-size:120%;" + ">[[/Chain " + Letter + "|" + chainnames[x] + "]]</span>'''")

            mainpage.write('\n')
            mainpage.write('----')
            mainpage.write('\n')
            for y in range(0, chainlength):
                if y % 2 == 0:
                    mainpage.write("*{{U|" + chainlist[x][y] + "}} (phrase)")
                else:
                    mainpage.write("*{{U|" + chainlist[x][y] + "}} (picture)")
                mainpage.write('\n')
            if (x + 1) % 5 == 0:
                if x != 0:
                    mainpage.write('|-')
                    mainpage.write('\n')
        mainpage.writelines(Part3)
    mainpage.close()


print('Step 2 complete!')
# The following creates the Sub Pages

imgprefix = input('What will the image prefix be? ("Stellar" would be the prefix in this example: Stellar_b2) ')

for x in range(1, players + 1):
    createsub = 0
    if in_ex == 0:
        createsub = 1
    elif in_ex == 1:
        if x in setchain:
            createsub = 1
    else:
        if x not in setchain:
            createsub = 1
            # Process Normally
    if createsub == 1:
        
        six = 6


print('All done!')

