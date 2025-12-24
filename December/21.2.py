# Rules:
# - Same actions: Study (5), Rest (3), Scroll (1)
# - The agent runs for 20 decisions (iterations).
# - It must remember the last 5 chosen actions.
# - If an action appears 3 or more times in memory:
# - Apply a penalty of −2 to that action’s base score.
# - Add random noise (−1 to +1) once per action per decision.
# - Choose the action with highest final score.
# - Update memory (FIFO: drop oldest).
# Output each step:
# - Current memory
# - Final scores
# - Chosen action
# Why this is actually useful:
# - This is anti-addiction logic
# - This is behavior regulation
# - This is how real agents avoid loops
# - This maps directly to:
# - habit modeling
# - reward shaping
# - moral / control cortex ideas you like

import random as rd
memorya = ["Study", "Rest", "Scroll"]
memorys = ["Study", "Rest", "Scroll"]

study = 5
rest = 3
scroll = 1

study+=rd.randint(-1, 1)
rest+=rd.randint(-1, 1)
scroll+=rd.randint(-1, 1)
memoryn=[study, rest, scroll]

if len(memorys)>5:
  memorys.pop(0)
if memorys.count("Study")>3:
  study-=2
if memorys.count("Rest")>3:
  rest-=2
if memorys.count("Scroll")>3:
  scroll-=2

a=max(memoryn)
b=memorya[memoryn.index(a)]
memorya, memoryn = list(), list()
if b=="Study":
  memorys.append("Study")
  memoryn.append(study)
elif b=="Rest":
  memorys.append("Rest")
  memoryn.append(rest)
elif b=="Scroll":
  memorys.append("Scroll")
  memoryn.append(scroll)
else:
  print("Err")

for i in range(20):
  study = 5
  rest = 3
  scroll = 1

  study+=rd.randint(-1, 1)
  rest+=rd.randint(-1, 1)
  scroll+=rd.randint(-1, 1)
  memoryn=[study, rest, scroll]

  if len(memorys)>5:
    memorys.pop(0)
  if memorys.count("Study")>3:
    study-=2
  if memorys.count("Rest")>3:
    rest-=2
  if memorys.count("Scroll")>3:
    scroll-=2

  a=max(memoryn)
  b=memorya[memoryn.index(a)]
  if b=="Study":
    memorys.append("Study")
    memoryn.append(study)
  elif b=="Rest":
    memorys.append("Rest")
    memoryn.append(rest)
  elif b=="Scroll":
    memorys.append("Scroll")
    memoryn.append(scroll)
  else:
    print("Err")
  
  print(memorya)
  print("Study:", study, "Rest:", rest, "Scroll:", scroll)
  print("Current action:", memorya[-1])