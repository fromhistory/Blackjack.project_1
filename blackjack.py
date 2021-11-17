from replit import clear
from art import logo
import random 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def first_cards():
  your_cards = []
  for i in range(2):
    card = random.choice(cards)
    your_cards.append(card)
  return your_cards

def add_cards(your_cards):
  card = random.choice(cards)
  your_cards.append(card)
  return your_cards

def count_scores(result):
  score = sum(result)
  return score 

def comp_card():
  comp_cards = []
  card = random.choice(cards)
  comp_cards.append(card)
  return comp_cards

computer_card = comp_card()

def add_compcards(computer_card):
  while sum(computer_card) < 17:
    card = random.choice(cards)
    computer_card.append(card)
  return computer_card

added_cards = add_compcards(computer_card)
#print(f"new: {added_cards}")


def blackjack():

  play = True 

  while play:

    play = input("Do you want to play? Say 'yes' or 'no'. ")
    clear()

    if play == 'no':
      play = False 
    else:
      print(logo)
      result = first_cards()
      print(f"Your cards: {result}")
      score = count_scores(result)
      print(f"Your current score: {score}")
      computer_card = comp_card()
      unmuted_first = comp_card()
      print(f"Computer's first card: {computer_card[0]}")
      dealers_cards = add_compcards(computer_card)
      
      while True:
      
        new_card = input("Type 'yes' to get another card, type 'no' to pass: ")

        if new_card == 'yes':
          result = add_cards(result)
          print(f"Your cards {result}")
          score = count_scores(result)
          print(f"Your current score: {score}")
          if score > 21:
            print("You went over. You lose 😭")
            break
          elif score == 21:
            print("You won the game! Your score is 21!")
            break
          print(f"Computer's first card: {unmuted_first}")
          continue 
        else:
          score = count_scores(result)
          score_comp = count_scores(dealers_cards)
          print(f"Your cards: {result}")
          print(f"Your final score: {score}")
          print(f"Computer's final hand: {dealers_cards}")
          print(f"Computer's final score: {score_comp}")

          if score_comp > 21:
            print("You won the game! Congrats")
          elif score_comp > score:
            print("You lost the game. Computer won.")
          elif score_comp == score:
            print("That's a draw")
          else:
            print("You won the game! Congratulations!")
         
          break
        

blackjack() 
