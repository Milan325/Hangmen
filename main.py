import random
from lifes import logo, stages
from word_list import words


def choose():
    a_word = random.choice(words)
    listed_word = list(a_word)
    return listed_word


def game_loop():
    global chosen_word
    lives = 6
    hidden_word = []
    for letter in chosen_word:
        hidden_word.append("_")
    print(hidden_word)
    end = False
    while not end:
        guess = input("Guess a letter: ")
        guess = guess.lower()
        for place in range(len(chosen_word)):
            letter = chosen_word[place]
            if letter == guess:
                hidden_word[place] = letter
        if guess not in chosen_word:
            lives -= 1
        if guess in hidden_word:
            print(f"You have already guessed letter \"{guess}\"")
        print(hidden_word)
        print(stages[lives])
        if "_" not in hidden_word:
            print("You won!!!\nCongrats 👍")
            ask = input("Do you want to play again? (y/n) ").lower()
            if ask == "y":
                chosen_word = choose()
                hidden_word = []
                for letter in chosen_word:
                    hidden_word.append("_")
                print(hidden_word)
            elif ask == "n":
                end = True
        elif lives == 0:
            print("You've lost.")
            ask = input("Do you want to play again? (y/n) ").lower()
            if ask == "y":
                chosen_word = choose()
                hidden_word = []
                for letter in chosen_word:
                    hidden_word.append("_")
                print(hidden_word)
            elif ask == "n":
                end = True


chosen_word = choose()
print(logo)
game_loop()
