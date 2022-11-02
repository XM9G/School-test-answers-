from csinsc import *


# The game start scene.
label .game_start
# The introductory text to our game. Put your instructions here.
print(Style.bold + Colour.white + Highlight.red + "Escape from Castle Darkhallow.\n")
print(Colour.reset + Colour.red + "You have awoken in a cold dungeon.") 
print("The light is dim. You can barely see.")
print("You feel along the stony wall and find a door,")
print("and with a push it creaks open.") 
print("Stale air rushes in. You walk through, slowly...\n" + Colour.reset)

# The two doors scene.
label .corridor
print("Flickering torches light your way.") 
print("You see two doors at the end of the damp and silent corridor.")
print("One has an 'x' carved into it. The other an 'o'.")
print("You need to keep moving. You must choose.")
label .doors
whereto = input("Do you go through door x or door o?: ")

if whereto == "x":
  goto .optionx
if whereto == "o":
  goto .one
print("\nThat is not an option, young one. Try again.\n")
goto .doors

label .optionx
print("")
print('In this room there is an enemy that you have to defeat.')
print('There are 2 ways to defeat him: Option 1 is to use the sword that is in the room and option 2 is to go through the secret door')
whereto = input('Which option do you choose, 1 or 2? ')

if whereto == "2":
    goto .one
if whereto == "1":
    goto .two
print("That is not an option.")
goto .optionx


label .one
print("")
print('In this room there is a door but its high and you cant get to it')
print("There are 2 spells: One is a jump potion and the 2nd one is a invisibility potion")
label .invis
potion = input('Which potion do you want to use? 1 or 2? ')

if potion == "1":
    print("you used the jump potion to get to the door")
    goto .high

if potion == "2":
    print("You used the invisibilty potion but it diddnt help you. you are still in the room.")
    goto .invis
print("thats not an option.")
goto .invis

label .two
print("you tried to use the sword to kill the enemey but It diddnt work however they told you some important information. ")
print("They said that when your at the last room you should go through the door with the higher number.")
goto .doors

label .high
print("")
print("there is a door but to get through you have to answer a question.")
question = input('The question is: What comes next in the pattern 2, 4, 6, 8? ')

if question == "10":
    print("correct")
    goto .final
if question != "10":
    print("wrong")
    goto .high
print("that is not an option.")
goto .high
label .final
print("")
print("Now you are in the final room.")
print("There are 10 doors.")
print("If you choose the wrong one you will go back to the start.")
door = input('What number door do you choose?')
if door == "10":
    print("Good Job, you completed the game.")
if door != "10":
    print("Sorry you got the wrong door.")
    print("")
    goto .game_start