
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

corridor = input("You got to the end of the corridor, do you turn left or right? ").lower()

if corridor == "left":
  print("Great choice!. You are continuing the game!\n")
  step2 = input("It was terrible rain, there is too much water. Do you want to wait untill the level decrease or you want to swim across? Type: wait or swim...").lower()
  
  if step2 == "wait":
    print("Good decision again, go slowly to the door.\n")
    step3 = input("You are about to end this horrible labyrinth. The last choice you must to make is door\'s colour. Do you prefer red, blue or yellow? ").lower()
    
    if step3 == "yellow":
      print("Great! You saved your life and you found your treasure!")
    elif step3 == "red":
      print("Burned by fire. Game over.")
    else:
      print("Eaten by beasts. Game over.")

  else:
    print("Sorry, water density doesn\'t let you swim too far. Game over.")
else:
  print("You fell into the hole. Game over.")
