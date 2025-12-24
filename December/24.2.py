# New constraint (important):
# - If an action has not appeared in the last 5 turns, give it a temporary bonus of +2 for that iteration only.
# Why this matters:
# - This is exploration vs exploitation
# - Prevents starvation of low-base actions
# - Used in real agents, schedulers, recommenders
# What to observe (don’t code blindly):
# - Does Scroll now appear sometimes?
# - Does the system oscillate without collapsing?
# - Does Study still dominate overall? (It should.)

import random as rd
act = ["Study", "Rest", "Scroll"]
mem = []

for loop in range(20):
  st, re, sc = 5, 3, 1
  
  if len(mem)>=5:
    print(mem[0], " removed.")
    mem.pop(0)

  if mem.count("Study")>=3:
    st-=2
    print("Penalty applied to Study.")
  elif mem.count("Study") == 0:
    st+=2
    print("Bonus applied to Study.")
  if mem.count("Rest")>=3:
    re-=2
    print("Penalty applied to Rest.")
  elif mem.count("Rest") == 0:
    re+=2
    print("Bonus applied to Rest.")
  if mem.count("Scroll")>=3:
    sc-=2
    print("Penalty applied to Scroll.")
  elif mem.count("Scroll") == 0:
    sc+=2
    print("Bonus applied to Scroll.")

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