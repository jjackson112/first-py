skillz ="Howdy, I'm busy crushing skillz!"
print(skillz + "And I'm killing it!")

user_input = input("Which birthday are you looking for? ")

if user_input == "Sasha":
  print("Birthday is 01/01/2009")
elif user_input == "Chippy":
  print("Birthday is 02/31/2000")
else:
  print("Can't find a birthday for this person.")

# Try and Except

print("Which two numbers do you want to add together?")

user_input1 = float(input("Input your first number: "))
user_input2 = float(input("Input your second number: "))

try:
  print(user_input1 + user_input2)
except:
  print("At least one of your inputs was not a number")