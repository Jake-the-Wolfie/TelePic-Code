# Footnote [1]: If something goes awry here (such as the ends of the names are missing), your names are probably too long. Make them shorter.

import csv
import random

print('How many players are there in your game?')
players = int(input())
print('How long will each chain be?')
chainlength = int(input())

header = ['Chain / Round']
chainlist = [] 
PermaPlayers = []
ChainNames = []
TempPlayers = []

random.seed(version=2)

# Header setup
for x in range(0, chainlength):
    headstring = str(x+1)
    header.append(headstring)

# Loading the text files into the program
names = open('playerlist.txt', 'r')
for x in range(0, players):
    user = names.readline(100) # Footnote [1]
    PermaPlayers.append(user.rstrip())
names.close()
names = open('chainnames.txt', 'r')
for x in range(0, players):
    user = names.readline(100) # Footnote [1]
    ChainNames.append(user.rstrip())
names.close()

TempPlayers = PermaPlayers

print('Step 0 complete!')
# The above is setup, the bottom is the program.
# This should proccess the players.

for x in range(0, players):
    templist = [PermaPlayers[x]]
    chainlist.append(templist)
# This code adds the players in order of what you put in players.txt, no randomness is nessecary.

bad_numbers = {0}
GoodNumber = 0
for x in range(1, chainlength):
    while GoodNumber == 0:
        RandNum = random.randint(1, players - 1)
        if RandNum not in bad_numbers:
            GoodNumber = 1
    bad_numbers.add(RandNum)
    GoodNumber = 0
    for y in range(0, players):
        n = (RandNum + y) % players
        templist = PermaPlayers[n]
        chainlist[y].append(templist)
# This essentially does a Caesar shift on the playerlist, then adds them to the existing nested lists inside chainlist.
# I made sure that it couldn't get the same number twice.
# This should proccess the chains.

for x in range(0, players):
    chainlist[x].insert(0, ChainNames[x])
# This inserts the name of the chain at the beginning.

blanklist = []
for x in range (0, players):
    blanklist.append('')
# This makes me feel slimey, but it's the easiest way I thought of to get the alternating rows and colummns.
# This exports the data to the files

with open('chainsheet.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for x in range(0, players):
        writer.writerow(chainlist[x])
        writer.writerow(blanklist)
f.close()

print('All Done!')
# Done!