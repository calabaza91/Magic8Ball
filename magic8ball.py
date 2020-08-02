#This simulates a Magic 8 Ball
#Update 2: Have user ask a question and play the game
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again' 
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so great'
    elif answerNumber == 9:
        return 'Very doubtful'

def printAnswer():
    r = random.randint(1,9)
    fortune = getAnswer(r)
    print(fortune + '\n')

while True:
    #Input is converted to a string and is lowercased
    getFortuneTold = str(input('Would you like to get your fortune told? (Y/N)\n')).lower()
    
    #check if first character matches 'y' or 'n', else shake again
    if getFortuneTold[0] == 'y':
        question = str(input('Ask a question into the mists..\n'))
        print('The mists respond..')
        dramaticPause = input('...*~press enter~*...')
        printAnswer()
    elif getFortuneTold[0] == 'n':
        print('Goodbye and good luck..')
        break;
    else:
        print('That is not a vaild answer, my dear.')
