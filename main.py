print("Let's play rock, paper, scissors!")
print()
name = input("What is your name: ")
print("Hi \033[36m", name, "\033[0m ready to play")
import random
p1wins = 0
p2wins = 0

while True:

  p1 = input("Enter your choice (R/P/S): ").lower()
  options = ['r', 'p', 's']
  p2 = random.choice(options)
  print()
  print(name, "chose", p1)
  print("computer chose", p2)
    

  if p1 == p2:
    print("\033[30m It's a draw! \033[0m")
  elif (p1 == 'r' and p2 == 's') or (p1 == 'p'
                                       and p2 == 'r') or (p1 == 's'
                                                          and p2 == 'p'):
    print("\033[35m", name, "wins! \033[0m")
    p1wins += 1
  elif (p2 == 'r' and p1 == 's') or (p2 == 'p'
                                       and p1 == 'r') or (p2 == 's'
                                                          and p1 == 'p'):
    print("\033[31m The Computer wins! \033[0m")
    p2wins += 1
  elif p1 != options:
    print("Invalid Move \033[36m", name, "\033[0m the computer wins!")
    p2wins += 1
    print()
  if p1wins < 3 and p2wins < 3:
    playagain = input("Do you wanna play again(Y/N)?: ").upper()
    if playagain == "Y":
      continue
  else:
    print("Thanks for playing!")
    print(name,'has',p1wins,'wins and computer has',p2wins,'wins')
    if p1wins > p2wins:
      print(name,'wins')
    else:
      print('The computer wins')
    break
  
