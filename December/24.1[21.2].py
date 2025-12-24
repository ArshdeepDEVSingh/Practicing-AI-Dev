# Revision for 21.2.py

import random as rd
act = ["Study", "Rest", "Scroll"]
mem = []

for loop in range(20):
  st, re, sc = 5, 3, 1

  if mem.count("Study")>=3:
    st-=2
    print("Penalty applied to Study.")
  if mem.count("Rest")>=3:
    re-=2
    print("Penalty applied to Rest.")
  if mem.count("Scroll")>=3:
    sc-=2
    print("Penalty applied to Scroll.")
  
  if len(mem)>=5:
    print(mem[0], " removed.")
    mem.pop(0)

  st += rd.randint(-1, 1)
  re += rd.randint(-1, 1)
  sc += rd.randint(-1, 1)

  if st >= re and st >= sc:
    mem.append(act[0])
  elif re >= st and re >= sc:
    mem.append(act[1])
  elif sc >= st and sc >= re:
    mem.append(act[2])

  print("Study:", st, ", Rest:", re, ", Scroll:", sc)
  print("Last action:", mem[-1])
  print("Memory:", mem, "\n")