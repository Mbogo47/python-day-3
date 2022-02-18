print("Welcome to the Love Calculator!")
name_1 = input("What is your name?\n").lower()
name_2 = input("What is their name?\n").lower()

combined_name = name_1 + name_2
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

true = (t + r + u + e)
print(f"Total= {true}")

love = (l + o + v + e)
print(f"Total= {love}")
love_score = str(true) + str(love)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {int(love_score)}, you go together like coke and mentos.")
elif 40 < int(love_score) < 50:
    print(f"Your score is {int(love_score)}, you are alright together.")
else:
    print(f"Your score is {int(love_score)}.")
