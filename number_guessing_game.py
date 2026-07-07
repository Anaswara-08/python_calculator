while True :
 print('-------Welcome to Number Guessing Game------')
 print ("Choose difficulty , 1.Easy", \
 "2.medium" ,\
 "3.hard")
 difficulty = int(input("Choose difficulty (1,2 or 3 ): "))
 if difficulty == 1:
   import random 
   secret_num = random.randint(1,50 )
   attempts = 0
   print("I am thinking of a number between 1 and 50")
   max_number = 50 
   max_attempts = 10
 elif difficulty == 2:
   import random 
   secret_num = random.randint(1,100 )
   attempts = 0
   print("I am thinking of a number between 1 and 100")
   max_number = 100 
   max_attempts = 7 
 elif difficulty == 3:
   import random 
   secret_num = random.randint(1,200 )
   attempts = 0
   print("I am thinking of a number between 1 and 200")
   max_number = 200 
   max_attempts = 5
 else :
   print ("invalid input choose between 1 , 2 and 3")
   continue
 while True:
  try:
   guess = int(input("Enter Your Guess: "))
  except ValueError:
   print("please enter a valid number")
   continue
  attempts += 1
  if guess == secret_num :
    print ("You won !!")
    print("you guessed right .congratulation")
    print(f"You have gussed the number in {attempts} attempts")
    break
  attempts_left = max_attempts-attempts 
  print("Attempts left",attempts_left)
  if attempts_left == 0:
   print("Game Over !!.Sorry you lost")
   print("The secret Number is ",secret_num)
   break
  elif guess < secret_num :
    print('Oops! Too low .Try a higher number')
  else:
    print("Oops!Too high.Try a lower number")
 play_again = input('Do you want to play again?(y/n)')
 if play_again != "y":
   print("Thank you for playing")
   break



