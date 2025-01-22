#Print introduction
print("Welcome to Maya's Roulette Table!")
print("")
print("Game Rules:")
print("")
print("Every bet costs $5.")

#Initialize bet amount for future winnings calculations
bet = 5

#Import random
import random

#Add count variable to write round names
count = 1

#Add round titles using count variable
#Print game option in loop so they can repeat every round
#Create a place for player to input their game choice
while True:
  
#Rules function given to me by Professor Washington as part of my first deliverable corrections
  rules = f"""
  
-------
Round {count}
-------
Betting Options:
1. Straight Up: Single number selection. Potential payout is 35 to 1.
2. Split: Single number selection. Covers the chosen number and one adjacent number (either above or below). Potential payout is 17 to 1.
3. Street: Single number selection. Covers the chosen number and the next two numbers in sequence. Potential payout is 11 to 1.
4. Top: Any number from 1-18. Potential payout is even money ($10).
5. Bottom: Any number from 19-36. Potential payout is even money ($10).
6. Even/Odd: Covers all even or all odd numbers from 1-36. Potential payout is even money ($10).
7. Quit Game.
  """
  print(rules)

  count += 1

#----------------------------
#While loop given to me by Professor Washington as part of my first deliverable corrections
  print("")
  while True:
    choice = int(input("Game choice (Enter a number from 1-7): "))
    if not (1 <= choice <= 7):
      print("")
      print("Invalid number input. Please enter a number between 1 and 7.")
      print("--------------------------")
      print("")
      print("")
    else:
      break
  print("")
#----------------------------

  
#1. STRAIGHT UP:
#Ask player for game choice (part of original while loop)
#Ask player for bet number
#Validate that the bet number is between 1 and 36
#Spin wheel (random & between 1 and 36) using random.randit
#If number wins, bet x 35 + bet.
#Calculate amount won and print for player.
#If number loses, print loss message
  if choice == 1:
    print("Welcome to Straight Up!")
    print("")

#----------------------------
#While loop given to me by Professor Washington as part of my first deliverable corrections
    while True:
      bet1 = int(input("Which number would you like to select for the Straight Up bet (1-36): "))
      if not (1 <= bet1 <= 36):
        print("")
        print("Invalid number input. Please select a number between 1 and 36.")
        print("--------------------------")
        print("")
        print("")
      else:
        break
#----------------------------
    
    print("........... Spinning the Wheel ...........")
    randomnumber1 = random.randint(1, 36)
    print("Result: The rolled number is", randomnumber1)

    if randomnumber1 == bet1:
      winstraight = 35
      payout1 = (bet * winstraight) + bet
      print("Outcome: Congratulations! You win $"+str(payout1), "("+str(winstraight), "to 1 payout on your $5 bet).")

    else:
      print("Outcome: Sorry, you lose this round. Better luck next time!")

  
#2. SPLIT:
#Ask player for game choice (part of original while loop)
#Ask player for bet number
#Validate that the bet number is between 1 and 36
#Spin wheel (random & between 1 and 36) using random.randit
#If number is = bet number/one up/one down, win (bet x 17 + bet).
#Calculate amount won and print for player
#If number loses, print loss message
  if choice == 2:
    print("Welome to Split!")
    print("")
    
#----------------------------    
#While loop given to me by Professor Washington as part of my first deliverable corrections
    while True:
      bet2 = int(input("Which number would you like to select for the Split bet (1-36): "))
      if not (1 <= bet2 <= 36):
        print("")
        print("Invalid number input. Please select a number between 1 and 36.")
        print("--------------------------")
        print("")
        print("")
      else:
        break
#----------------------------
    
    print("........... Spinning the Wheel ...........")
    randomnumber2 = random.randint(1, 36)
    print("Result: The rolled number is", randomnumber2)

    if randomnumber2 == bet2 or randomnumber2 == bet2 - 1 or randomnumber2 == bet2 + 1:
      winsplit = 17
      payout2 = (bet * winsplit) + bet
      print("Outcome: Congratulations! You win $"+str(payout2), "(" +str(winsplit), "to 1 payout on your $5 bet).")

    else:
      print("Outcome: Sorry, you lose this round. Better luck next time!")

  
#3. STREET:
#Ask player for game choice (part of original while loop)
#Ask player for bet number
#Validate that the bet number is between 1 and 36
#Spin wheel (random & between 1 and 36) using random.randit
#If number is = their number or one of the two consecutive numbers, win (bet x 11 + bet).
#Calculate amount won and print for player
#If number loses, print loss message
  
  if choice == 3:
    print("Welcome to Street!")
    print("")

#----------------------------
#While loop given to me by Professor Washington as part of my first deliverable corrections
    while True:
      bet3 = int(input("Which number would you like to select for the Street bet (1-36): "))
      if not (1 <= bet3 <= 36):
        print("")
        print("Invalid number input. Please select a number between 1 and 36.")
        print("--------------------------")
        print("")
        print("")
      else:
        break
#----------------------------     
    
    print("........... Spinning the Wheel ...........")
    randomnumber3 = random.randint(1, 36)
    print("Result: The rolled number is", randomnumber3)

    if randomnumber3 == bet3 or randomnumber3 == bet3 + 1 or randomnumber3 == bet3 + 2:
      winstreet = 11
      payout3 = (bet * winstreet) + bet
      print("Outcome: Congratulations! You win $"+str(payout3), "("+str(winstreet), "to 1 payout on your $5 bet).")

    else:
      print("Outcome: Sorry, you lose this round. Better luck next time!")

      
#4. TOP:
#Ask player for game choice
#Spin wheel (random & between 1 and 36)
#If number is = between 1-18 (use range function), win $10.
#Print win message for player with amount won ($10)
#If number loses (over 18), print loss message

  if choice == 4:
    print("Welcome to Top!")
    print("")
    print("........... Spinning the Wheel ...........")
    randomnumber4 = random.randint(1, 36)
    print("Result: The rolled number is", randomnumber4)
  
    if randomnumber4 in range (1,18):
      print("Outcome: Congratulations! You win $10 (even money on your Top bet).")
      
    else:
      print("Outcome: Sorry, you lose this round. Better luck next time!")


#5. BOTTOM:
#Ask player for game choice
#Spin wheel (random & between 1 and 36)
#If number is = between 19-36 (use range function), win $10.
#Print win message for player with amount won ($10)
#If number loses (under 19), print loss message

  if choice == 5:
    print("Welcome to Bottom!")
    print("")
    print("........... Spinning the Wheel ...........")
    randomnumber5 = random.randint(1, 36)
    print("Result: The rolled number is", randomnumber5)
  
    if randomnumber5 in range (19,36):
      print("Outcome: Congratulations! You win $10 (even money on your Bottom bet).")
      
    else:
      print("Outcome: Sorry, you lose this round. Better luck next time!")


#6. EVEN/ODD:
#Ask player for game choice (part of original while loop)
#Ask player for even/odd bet
#Validate that input entered is either "Even" or "Odd"
#Spin wheel (random & between 1 and 36) using random.randit
#If number is = even or odd (depending on whats picked), win $10
#Calculate amount won and print for player
#If number loses, print loss message
  if choice == 6:
    print("Welcome to Even/Odd!")
    print("")

#----------------------------
#While loop given to me by Professor Washington as part of my first deliverable corrections
    while True:
      bet6 = (input("Your preference for Even/Odd (Enter 'Even' or 'Odd'): "))
      if bet6 != "Even" and bet6 != "Odd":
        print("")
        print("Invalid input. Please enter 'Even' or 'Odd'.")
        print("--------------------------")
        print("")
        print("")
      else:
        break
#----------------------------
    
    print("........... Spinning the Wheel ...........")
    randomnumber6 = random.randint(2, 2)
    print("Result: The rolled number is", randomnumber6)

    if bet6 == ("Even"):
      if randomnumber6 % 2 == 0:
        print("Outcome: Congratulations! You win $10 (even money on your Even/Odd bet).")
      else:
        print("Outcome: Sorry, you lose this round. Better luck next time!")

    elif bet6 == ("Odd"):
      if randomnumber6 % 2 == 0:
        print("Outcome: Sorry, you lose this round. Better luck next time!")

      else:
        print("Outcome: Congratulations! You win $10 (even money on your Even/Odd bet).")
    
      

#7. QUIT CHOICE:
#print thank you message
#break loop
  if choice == 7:
    print("Thank you for playing at Maya's Roulette Table! We hope to see you again soon!")
    break
