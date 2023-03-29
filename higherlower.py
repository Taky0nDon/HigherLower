#H I G H E R L O W E R

from game_data import data
from art import logo, vs
from random import choice
from os import system
# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#}
#entry.get(key)
def clear():
    return system('cls')
def compare(entry1,entry2):
  """pass in 2 entries and return the one with the higher follower count"""
  if entry1['follower_count'] > entry2['follower_count']:
    return entry1
  else:
    return entry2
def get_entry(data):
  """pass this function the data (list) and return an entry"""
  entry = choice(data)
  return entry
#A/B: <name>, a <description>, from <country>
def print_a(entry):
  """pass an entry and print a formatted string for A"""
  a_name = A.get('name')
  a_description = A.get('description')
  a_country = A.get('country')
  print(f"Compare A: {a_name}, a {a_description}, from {a_country}")
def print_b(entry):
  """pass an entry and print a formatted string for B"""
  b_name = B.get('name')
  b_description = B.get('description')
  b_country = B.get('country')
  print(f"Against B: {b_name}, a {b_description}, from {b_country}")
#Choose two entries from data
# match user_choice with each option from data
#invalid input = incorrect
def match_choice(choice,entry1,entry2):
  """pass in user_choice, entries and return corresponding entry."""
  if choice == 'a':
    return entry1
  elif choice == 'b':
    return entry2
  else:
    return 'invalid'
#define A and B then remove from data so they can't be recycled
A = get_entry(data)
B = get_entry(data)
while A == B:
    B = get_entry(data)
#take input from the user to determine their choice
print(logo)
is_playing = True
score = 0
while is_playing == True:
  print_a(A)
  print(vs)
  print_b(B)
  
#test
  # print(f"A follows = {A['follower_count']}, B follows = {B['follower_count']}")
  user_choice = input("Who has more followers? Enter 'A' or 'B': ").lower()
  
#find the higher of the two
  higher = compare(A,B)
#compare match_choice() output with higher
#if they get it wrong, print "Sorry, that's wrong. Final score: {score}"
  if match_choice(user_choice,A,B) != higher:
    is_playing = False
    clear()
    print(f"Sorry, that's wrong. Final score: {score}")
#if they get it right, choose move B up to A
#make sure the new A is the previous winner
  else:
    score += 1
    A = B
    B = get_entry(data)
    data.remove(B)
    clear()
    print(f"You're right! Current score: {score}")
    
