#imports

from art import logo, vs
from game_data import data
import random
from replit import clear


#choose random A and B from the dictionary 
def choose_account():
  return random.choice(data)

# the game function
def play_game():
    score = 0
    game_over = False
    #display the logo of the game
    print(logo)
    #repeating if the user guess right
    A= choose_account()
    while (game_over == False):
      B= choose_account()
      #if accounts are similar choose another account B
      while(A==B):
        B= choose_account()
      A_name, A_description, A_country = A["name"], A["description"], A["country"]
      B_name, B_description, B_country = B["name"], B["description"], B["country"]
      print(f"Compare A : {A_name}, a {A_description}, from {A_country}")
      print(vs)
      print(f"Compare B : {B_name}, a {B_description}, from {B_country}")
      higher_guess = input("Who has more followers? Type 'A' or 'B' : ")
      if A['follower_count'] > B['follower_count']:
          higher_fact = 'A'
      else:
          A=B
          higher_fact = 'B'
      
      clear()
      print(logo)
#giving the user feedback of thier guess  
      if higher_fact == higher_guess:
          score += 1
          
          print(f"You're right. Your current score is {score}")
      else:
          game_over = True
         
          print(f"Sorry.. You're wrong. Final score is {score}")



play_game()
