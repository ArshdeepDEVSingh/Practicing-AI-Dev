# Problem 1 — Controlled Random Decision Maker
# Goal:
# - Simulate a simple “AI” that chooses an action, but not purely randomly.
# Task:
# Write a Python program that:
# - Has 3 actions: "Study", "Rest", "Scroll".
# Each action has a base score:
# - Study → 5
# - Rest → 3
# - Scroll → 1
# Add controlled randomness:
# - Add a random number between -1 and +1 to each score.
# - Select the action with the highest final score.
# Print:
# - Base scores
# - Random noise added
# - Final scores
# - Chosen action
# Rules:
# - Use only core Python + random.
# - No shortcuts.
# - Make it readable.
# Why this matters (don’t skip):
# This is the foundation of:
# - Decision-making
# - Reward systems
# - Non-chaotic randomness
# - Agent behavior

import random as rd

for x in range(10):
  Study=5
  Rest=3
  Scroll=1
  
  for i in range(rd.randint(1,100)):
    a=rd.randint(1,3)
    b=rd.randint(-1,1)
    if a==1:
      Study+=b
    elif a==2:
      Rest+=b
    elif a==3:
      Scroll+=b
    else:
      print(str("Err"))
  
  c=max(Study, Rest, Scroll)
  if c==Study:
    print("Study", Study)
  elif c==Rest:
    print("Rest", Rest)
  elif c==Scroll:
    print("Scroll", Scroll)
  else:
    print("None")
