x = 4 #setting up the x coordanite
y = 4 #setting up the y coordanite
ex = 5 #1st enemy's x coordanite
wave = 1 #wave
ammo = 5 #ammo ammount
ey = 5 #1st enemy's y coordanite
d = True
turn = 0 #turn #
eys = 9 #2nd enemy's y coordanite
exs = 9 #2nd enemy's y coordanite
health = "3" #health
import os
valmov = ["w", "a", "s", "d", "t", "g", "h"] #what you are allowed to type
import time
def printscreen(x, y, z, u, f): #prints the screen
  os.system('clear') #clears the screen
  for k in range(10):
    j = ""
    for i in range(10):
      j = j + x[k][i] + "   " #takes the screen list and converts it to a string
    #prints the string
    if k == 0:
     print(j + "              Wave: " + str(u) + "\n")
    elif k == 1:
     print(j + "              Turn: " + str(f) + "\n")
    else:
      print(j + "\n")
      #adds extra stats
  print("HEALTH: " + y + "  Ammo: " + str(z))
  print("\n\n\n\n\nPress h and then enter for controls\n\n\n\n\n\n")
total = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", ".", "."], ] #The Screen List
total[y][x] = "I"
printscreen(total, health, ammo, wave, turn)
ttime = time.time() #Takes the time that you start
#game starts
while True:
  pastx = x
  pasty = y  #finds last coordanites
  pl = False
  if total[ey][ex] == "x": #tests to see if enemy is alive
    pl = True
  no = False
  #controls are here(Movement)
  k = input("move")
  if k in valmov:
    if k == "w":
      if y > 0:
        y = y - 1
      else:
        no = True
    elif k == "s":
      if y < 9:
        y = y + 1
      else:
        no = True
    elif k == "a":
      if x > 0:
        x = x - 1
      else:
        no = True
    elif k == "d":
      if x < 9:
        x = x + 1
      else:
        no = True
    elif ammo > 0:
     #shooting controls!
     if k == "t":
       ammo = ammo -1
       printscreen(total, health, ammo, wave, turn)
       for o in range(y+1):
         time.sleep(0.2)
         total[y - o - 1][x] = "o"
         if o > 0:
           total[y - o][x] = "."
         printscreen(total, health, ammo, wave, turn)
       if y > 0:
         total[0][x] = "."
       if y < 9:
         total[9][x] = "."
       no = True
       turn = turn + 1
     if k == "g":
       ammo = ammo - 1
       printscreen(total, health, ammo, wave, turn)
       for o in range(9-y):
         time.sleep(0.2)
         total[y + o + 1][x] = "o"
         if o > 0:
           total[y + o][x] = "."
         printscreen(total, health, ammo, wave, turn)
       if y > 0:
         total[0][x] = "."
       if y < 9:
         total[9][x] = "."
       no = True
       turn = turn + 1
     #Help menu
     if k == "h":
       print("\n\n\n")
       print("W = Forward        S = Backwards\nA = left        D = right \n T = upshoot        G = downshoot\n\nAfter every action press Enter\n\n\n\n\nPress H and then enter to exit\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
       while True:
        oo = input(".")
        no = True
        if oo == "h":
          break
    else:
      no = True
  else:
    no = True
  total[y][x] = "I"
  #clears last coordanite and updates new one
  if no == False:
    total[pasty][pastx] = "."
    turn = turn + 1
  #checks to see if you hit an enemy and if you did it teleports you to the last coordanite
  if turn == 5 and wave == 1:
    total[ey][ex] = "x"
  jj = True
  if total[eys][exs] == "x":
    jj = False
  if turn > 4 and wave == 1:
    if x == ex and y == ey and pl == True:
      total[y][x] = "x"
      x = pastx
      y = pasty
      total[y][x] = "I"
      health = str(int(health) - 1)
  printscreen(total, health, ammo, wave, turn)
  #Ai for the wave 2 enemy
  if wave == 2:
    total[eys][exs] = "."
    if abs(y - eys) > abs(x - exs):
      if eys < y:
        eys = eys + 1
      else:
        eys = eys - 1
    elif abs(x - exs) > abs(x - eys):
      if exs < x:
        exs = exs + 1
      else:
        exs = exs - 1
    elif abs(y - eys) == abs(x - exs):
      if exs < x:
        exs = exs + 1
      else:
        exs = exs - 1
    #weird code for what to do when 2nd wave enemy is hit
    if exs == x and eys == y:
      health = str(int(health) - 1)
      if x < 9:
       exs = exs + 1
      else:
        exs = exs - 1
      for ll in range(2):
        total[y][x] = "x"
        printscreen(total, health, ammo, wave, turn)
        time.sleep(0.2)
        total[y][x] = "I"
        printscreen(total, health, ammo, wave, turn)
        time.sleep(0.2)
    total[eys][exs] = "x"
  #updates wave if conditions are met
  if pl == False and turn >5 and wave == 1:
    time.sleep(1)
    wave = 2
    turn = 0
    printscreen(total, health, ammo, wave, turn)
  if jj == True and wave == 2 and turn > 2: #Has he won?
    d = False
    etime = time.time() # takes the time when you finish
    break
  if health == "0":
    break
#game end
#If lost then print this
if d == True:
 print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
 time.sleep(0.75)
 print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGame Over\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
 time.sleep(1)
#If won print this
else:
 print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Win\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
 time.sleep(1)
 print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTime: " + str(etime - ttime) + "Seconds\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #subtracts times to get the total time
 time.sleep(10)
#again text
while True:
  os.system('clear')
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAgain?\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  time.sleep(0.5)
  os.system('clear')
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAgain\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  time.sleep(0.5)