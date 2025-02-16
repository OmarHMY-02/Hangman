import random
stages = ["0", "1", "2", "3", "4", "5", "6"]
word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += " _ "
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"********* {lives} *********")
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed that letter {guess}")
    
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
            
        elif letter in correct_letters:
            display += letter
            
        else:
            display += " _ "
            
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"you guess {guess}, that't not in the word, you lose a life")
        if lives == 0:
            game_over = True
            print("******************* Game Over, you Lose. *******************")
    
    if "_" not in display:
        game_over = True
        print("You Win")
    
    print(stages[lives])
