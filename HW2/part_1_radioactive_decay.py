# make function
def atoms_remaining(initial_atoms, half_life, elapsed_time):
    num_half_lives = elapsed_time // half_life
    remaining_atoms = initial_atoms // (2 ** num_half_lives)
    return remaining_atoms

print("the number of atoms that remain are:", atoms_remaining(8000000, 12, 50))

def print_decay_table(initial_atoms, half_life):
    for time in range(0, 60, 12):
        print("atoms remaining at", time, "seconds:", atoms_remaining(initial_atoms, half_life, time))

print_decay_table(8000000, 12)