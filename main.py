import random

word_list = ['aniket', 'rugved', 'ankur', 'mrunmayi']

end_of_game = False
number_of_lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

word = ["_"] * len(chosen_word)
print(word)

while not end_of_game:
    print(f"lives={number_of_lives}")
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            word[i] = guess
    print(word)
    if guess not in chosen_word:
        number_of_lives -= 1
        if number_of_lives == 0:
            end_of_game = True
            print("Looser")

    if "_" not in word:
        print("You won")
        end_of_game = True

