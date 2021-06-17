import csv
import os

# Numerical values for your pleasure
print('How many players are there in your game?')
players = int(input())
print('How long will each chain be?')
chainlength = int(input())


# The following extracts and converts all the information into a useable format.

playerlist = []
contentlist = []
chainletters = []

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
    chainletters.append(Letter)


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
            playerlist.append(row)
        linecount = linecount + 1


chainnames = []
for x in range(0, players):
    chainnames.append(playerlist[x].pop(0))
    del contentlist[x][0]

absolute_path = os.path.abspath(__file__)
absolute_path = os.path.dirname(absolute_path)
WikiPage = os.path.join(absolute_path, 'WikiPage') # This should be the path to a folder which will have our text files.
SubPage = os.path.join(WikiPage, 'SubPages')

if not os.path.isdir(SubPage):
    os.makedirs(SubPage)
# The following creates the Main Page.
WikiPage = os.path.join(WikiPage, 'WikiPage.txt')
print("What is your game's url?")
url = input()
print("What is your game's name?")
name = input()
print("What is your username?")
host = input()
print("What month did your game start?")
datestart = input()
print("What month did your game end?")
datestop = input()
print("What year did it take place?")
year = input()
print("What description would you like to add?")
description = input()
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
        mainpage.write("'''" + str(x + 1) + ".''' " + '{{U|' + str(playerlist[x][0]) + '}}<br/>')
        mainpage.write('\n')
        if (x + 1) % 10 == 0:
            if x != players:
                mainpage.write('{{multicol-break}}')
                mainpage.write('\n')
    mainpage.writelines(Part2)
    # Writing down all the chains
    numblist = 0
    for x in range(0, players):
        mainpage.write("| '''<span style=" + "font-size:120%;" + ">[[/Chain " + chainletters[x] + "|" + chainnames[x] + "]]</span>'''")
        mainpage.write('\n')
        mainpage.write('----')
        mainpage.write('\n')
        for y in range(0, chainlength):
            if y % 2 == 0:
                mainpage.write("*{{U|" + playerlist[x][y] + "}} (phrase)")
            else:
                mainpage.write("*{{U|" + playerlist[x][y] + "}} (picture)")
            mainpage.write('\n')
        if (x + 1) % 5 == 0:
            if x != 0:
                mainpage.write('|-')
                mainpage.write('\n')
    mainpage.writelines(Part3)
mainpage.close()

# The following creates the Sub Pages
print('What will the image prefix be?')
print('"Stellar" would be the prefix in this example: Stellar_b2')
print("This is used to prevent multiple different game's images from overlapping on eachother")
imgprefix = input()
WikiPage = os.path.join(absolute_path, 'WikiPage')
SubPage = os.path.join(WikiPage, 'SubPages')
for x in range(0, players):
    imgnumb = 0
    CreatePage = os.path.join(SubPage, 'SubPage' + str(x + 1) + '.txt')
    with open(CreatePage, 'w') as subpage:
        # Preparing the text file
        if x != 0:
            subpage.write('<br /><div style="float:left;font-size:150%;font-weight:bold;">[[Telephone Pictionary: ' + name + '/Chain ' + chainletters[x-1] + '|« Previous]]</div>')
            subpage.write('\n')
            subpage.write('\n')
        if x != (players - 1):
            subpage.write('<br /><div style="float:left;font-size:150%;font-weight:bold;">[[Telephone Pictionary: ' + name + '/Chain ' + chainletters[x+1] + '|Next »]]</div><br /><br />')
            subpage.write('\n')
            subpage.write('\n')
        subpage.write('==Chain ' + chainletters[x] + ': ' + playerlist[x][0] + "'s Chain==")
        subpage.write('\n')
        subpage.write('\n')
        for y in range(0, chainlength):
            if y % 2 == 0:
                subpage.write("<span style=" + '"font-size:130%;color:#00bf80;">' + "'''{{U|" + playerlist[x][y] + "}} - Phrase '''</span>")
                subpage.write('\n')
                subpage.write(':<span style="font-size:170%;color:#434343;">' + contentlist[x][y] + '</span>')
                subpage.write('\n')
            else:
                imgnumb = imgnumb + 1
                subpage.write("<span style=" + '"font-size:130%;color:#00bf80;">' + "'''{{U|" + playerlist[x][y] + "}} - Picture '''</span>")
                subpage.write('\n')
                subpage.write(':[[Image:' + imgprefix + '_' + chainletters[x] + str(imgnumb) + '.png]]')
                subpage.write('\n')
            if y != (chainlength - 1):
                subpage.write('\n')
                subpage.write('\n')
        if x!= 0:
            subpage.write('<br /><div style="float:left;font-size:150%;font-weight:bold;">[[Telephone Pictionary: ' + name + '/Chain ' + chainletters[x-1] + '|« Previous]]</div>')
            subpage.write('\n')
        if x != (players - 1):
            subpage.write('<br /><div style="float:left;font-size:150%;font-weight:bold;">[[Telephone Pictionary: ' + name + '/Chain ' + chainletters[x+1] + '|Next »]]</div><br /><br />')
            subpage.write('\n')
        subpage.write('<br />[[Category:Telephone Pictionary]]')
    subpage.close()

print('All done!')

