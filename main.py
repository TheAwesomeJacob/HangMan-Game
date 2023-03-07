import random
import hangman_art
import words_list
from replit import clear

print(hangman_art.name_of_game)
random_word = random.choice(words_list.word_list)
end_game = False
blank_list = []
display_blanks = ""

for number in range(0, len(random_word)):
    blank_list.append("_")
  
while not end_game:
  
  display_blanks = " ".join(blank_list) 
  print(display_blanks + "\n")
  
  guessed_letter = input("Gues a letter: ").lower()
  print("\n")

  clear()
  
  if guessed_letter in random_word:
    for number in range(0, len(random_word)):
      if guessed_letter == random_word[number]:
        blank_list[number] = guessed_letter
  else:
    print(f"Your guessed letter: {guessed_letter}, is not int th word")
    print(hangman_art.stages.pop())
    if len(hangman_art.stages) == 0:
      print("You lose")
      end_game = True
    
  if '_' not in blank_list:
    end_game = True
    print("You win!")
