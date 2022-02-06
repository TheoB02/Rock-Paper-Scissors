from random import choice 
objects = ["rock", "paper", "scissors"]
computer = choice(objects)
rps = input ("What will you choose?").lower().strip()
if rps == computer:
  print ("It is a tie, we chose the same")
if rps == ("rock"):
  if computer == ("scissors"):
    print ("Goob job! You won!")
if rps == ("paper"):
  if computer == ("rock"):
    print ("Goob job! You won!")    
if rps == ("scissors"):
  if computer == ("paper"):
    print ("Goob job! You won!")    
if computer == ("scissors"):
  if rps == ("paper"):
    print ("I chose scissors. You lost! Try again") 
if computer == ("paper"):
  if rps == ("rock"):
    print ("I chose paper. You lost! Try again")  
if computer == ("rock"):
  if rps == ("scissors"):
    print ("I chose rock. You lost! Try again")   

if rps == ("amogus"):
  print ("Use rps not your mom")     

if rps == ("penis"):
   if computer == ("scissors"):
    print ("* cuts *")
if rps == ("penis"):
  if computer == ("rock"):
    print ("Ouch, hurts a lot")
if rps == ("penis"):
  if computer == ("paper"):
    print ("8====D")        

print ("Thanks for playing. I hope you enjoy it!")      
