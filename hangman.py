import random
listOfWords = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".split()
inputList = []
gameOn = True
wordChosen = random.choice(listOfWords)
startingLife = 7
life = startingLife

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def userInput():
  userInput = input("Guess a letter: ")
  return userInput

def checkGuess(userInput, wordChosen, inputList):
  if userInput in wordChosen:
    print("Correct!")
    inputList.append(userInput)
    return "correct"
  else:
    print("Incorrect!")
    return "incorrect"

def revealedWord(wordChosen, userInput, inputList):
  for letter in wordChosen:
    if letter in inputList:
      #print(userInput, end ="")
      print (letter, end="")
    else:
      print("_", end="")
  print()

def winningTracker(inputList,wordChosen, gameOn):
  if set(inputList) == set(wordChosen):
    print("You won!!")
    gameOn = False
    return gameOn
  else:
    return gameOn

def lifeTracker(decision, life):
  if decision != "correct":
    life -= 1
  print(HANGMANPICS[(startingLife-life)])    
    
  return life


while gameOn == True:
  ObtainedInput = userInput()
  decision = checkGuess(ObtainedInput, wordChosen, inputList)
  revealedWord(wordChosen, userInput, inputList) 
  life = lifeTracker(decision, life)
  if life == 0:
    gameOn = False
  gameOn = winningTracker(inputList, wordChosen, gameOn)
  