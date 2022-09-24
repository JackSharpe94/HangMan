import random
import re

f = open("words", "r")
options = f.read().splitlines()
# Generate a random answer from file
answer_to_guess = options[random.randint(0, len(options))]
answerArr = []
number_of_guesses = 0
lives = {"easy": 5, "medium": 3, "hard": 2}
for x in answer_to_guess:
    answerArr.append(x)

f.close()

print("This is a game of hangman")
print("What is your name?")
name = input()

while True:
    print("Please enter a difficulty, easy, medium or hard")
    difficulty = input()
    if difficulty not in lives.keys():
        print("please enter a valid difficulty")
        continue
    else:
        break

print(f"Hi {name}, please enter a letter between a - z")
while number_of_guesses < lives[difficulty]:
    guess = input()
    if len(re.findall("[a-z]", guess)) == 0 and len(guess) == 1:
        print("please enter a valid letter")
        continue
    else:
        while True:
            if guess in answerArr:
                print("Success")
                for letter in answerArr:
                    if letter == guess:
                        answerArr.remove(letter)
                break
            else:
                print("try again")
                number_of_guesses = number_of_guesses+1
                print(f"you have guessed {number_of_guesses} times, you have {lives[difficulty] - number_of_guesses} "
                      f"guesses remaining")
                break
    if len(answerArr) == 0:
        print("you win!")
        break

print("GAME OVER")


