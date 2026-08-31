# make first function
def atoms_remaining(initial_atoms, half_life, elapsed_time):
    num_half_lives = elapsed_time // half_life
    remaining_atoms = initial_atoms // (2 ** num_half_lives)
    return remaining_atoms

# print the thing
print("the number of atoms that remain are:", atoms_remaining(8000000, 12, 50))

# elaborate on the thing (fancy time!)
# time is my local counter variable. it can't be accessed outside of the for loop because
# it's declared inside of it. it doesn't exist beyond that bound
def print_decay_table(initial_atoms, half_life):
    for time in range(0, 60, 12):
        print("atoms remaining at", time, "seconds:", atoms_remaining(initial_atoms, half_life, time))

# call the second function
print_decay_table(8000000, 12)

# it's useful to separate atoms_remaining from print_decay_table because it makes both
# functions much simpler. plus, it's easier to modify, since there are less elements
# to worry about in each