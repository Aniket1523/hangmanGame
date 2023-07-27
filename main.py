import random
from hangman_word import word_list
from hangman_art import stages, logo
end_of_game = False
number_of_lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
word = ["_"] * len(chosen_word)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print(f"You already guessed {guess}")
        continue;
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            word[i] = guess
            print(f"You guessed {guess} and that's correct")


    if guess not in chosen_word:
        print(f"You guessed {guess} and that's incorrect. You lost one life. ")
        number_of_lives -= 1
        if number_of_lives == 0:
            end_of_game = True
            print("Looser")

    if "_" not in word:
        print("********** YOU WON **********")
        end_of_game = True
    print(word)
    print(stages[number_of_lives])

