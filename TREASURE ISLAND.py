print("Welcome to Treasure Island.")
print("Your mission is to go find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "Left" or "Right"\n').lower()
print(choice1)
if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat or Type "Swim" to swim across?\n').lower()
else:
    print("You fell into a hole.Game Over")
if choice2 == "wait":
    choice3 = input(
        'You\'ve arrived at the island unharmed.There is a house with three doors one blue, one yellow and one red. Which color do you choose?\n').lower()
    if choice3 == "red":
        print("It's a room full of fire. Game Over!")
    elif choice3 == "yellow":
        print("You found the treasure.You win!")
    elif choice3 == "blue":
        print("It's a room full of spiders.Game Over!")
else:
    print("You got attacked by a trout.Game over!")
