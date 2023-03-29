# HigherLower
Higher/Lower Game, 100 Days of Code Day 14. Simulates a database of instagram accounts and uses them for a game where the user attempts to guess which of the two accounts
has the most followers.

data.py contains the data as a list of dictionaries, each dictionary having 4 keys:
'name': the name of the person or organization the instagram is for
'follower_count': How many followers the account has
'description': What the person/organization is known for
'country': What country the person/organization is from.

art.py contains ASCII art for the title and versus logos

higherlower.py holds all the game logic.

The program begins by using a function called get_entry() that takes in the data list from data.py as an argument and returns a random entry.
Two variables, "A" and "B" each store one random entry.

If A and B happen to draw the same entry, get_entry() is rerun for B until they are different.

The logo is then printed, and two more global variables are declared. Score is set to an initial value and zero, and is_playing is set to True.
The gameplay loop will continue until is_playing is set to False.

Two functions were created to print formatted strings based on the values of A and B.
1) print_a() take an entry as an argument and returns a formatted string: "Compare A: {a_name}, a {a_description}, from {a_country}"
2) print_b() takes an entry as an argument and returns a formatted string: "Against B: {b_name}, a {b_description}, from {b_country}"

A potential improvement would be combining these two into one function.

The functions work using the dictionary.get() method to define variables for the name, description, and country.
It would have been possible to use entry['name'], entry['description'] and entry['country'] instead.

After the formatted strings and versus logo have been printed, a variable called user_choice is declared and stores the users guess as to which account has more followers.
the user's input is turned to lowercase with lower() to avoid case sensitive errors.

Then, a variable called "higher" is declared and set to the output of compare(). 
compare() is a function that accepts two entries (A and B) as arguments and returns the entry with the most followers using a simple if/else block.

a function called match_choice() is then called. The purpose of this function is to determine whether the user's choice was correct. match_choice() takes three
arguments: user_choice, and both entries (A and B).
if user_choice is equal to "a", entry1 (A) is returned. If user_choice is equal to "b", entry2 (B) is returned. For all other cases, the function returns
a string: "invalid"

if the output of match_choice() does not equal higher, then is_playing is set to False, the screen is cleared, and the user is told they guessed wrong and their final score.
Since match_choice() returns 'invalid' for all inputs other than 'a' or 'b' invalid inputs will always be treated as incorrect answers and therefore end the game.

if the output of match_choice() does match higher, the score is increased by one, A is set to the old value of B, and a new entry is chosen for B.
The user is then told they guessed right and their score.
The loop starts over, printing the new formatted strings based on the new values of A and B as well as the versus logo.

