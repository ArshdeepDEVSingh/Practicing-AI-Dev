# Goal:
# - Choose an action based on probabilities, not strict max.
# Rules:
# - Same actions, bases, memory, penalties, bonuses (keep all that)
# - After all adjustments, you’ll have final scores: st, re, sc
# New rule (core):
# - Convert scores into probabilities proportional to their value
# - Pick one action randomly using those 

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

  total = st + re + sc
  r = rd.randint(0, total-1)

  if r<st:
    mem.append(act[0])
  elif r<st+re:
    mem.append(act[1])
  else:
    mem.append(act[2])

  print("Study:", st, ", Rest:", re, ", Scroll:", sc)
  print("Last action:", mem[-1])
  print("Memory:", mem, "\n")