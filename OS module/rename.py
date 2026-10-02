import os

# let's say we have to change the 50 files name out of 100 files names :-
for i in range(0,50):
    os.rename(f"data/Concept_{i+1}", f"data/Tutorial_{i+1}")