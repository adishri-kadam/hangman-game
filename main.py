import random
from word_list import word_list
from stages import stages

chosen_wrd = random.choice(word_list)
chosen_word = list(chosen_wrd)
# test- print(chosen_word)
lives = 6

display = []
for word in chosen_word:
    display.append('_')
print(f"{' '.join(display)}")

ch = True
while ch == True :
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            ch = False
            print(f"Game Over!.You lost the word was {chosen_wrd}")

    print(f"{' '.join(display)}")
    if '_' not in display:
        ch = False
        print('you win')
        break
    print(stages[lives])

