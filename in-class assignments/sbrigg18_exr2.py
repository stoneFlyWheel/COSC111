# givens
initial_atoms = 8000000 # number of atoms at time zero
half_life = 12 # half-life, in seconds
elapsed_time = 50 # time elapsed, in seconds 

# operations

# how many half-lives have elapsed?
half_lives_count = elapsed_time // half_life

# how many atoms remain?
atoms_count = initial_atoms // (2 ** half_lives_count)

# what fraction of a half-life is left?
fraction_half_life = (elapsed_time - (half_lives_count * half_life)) / half_life

# does pemdas work still?
order_of_operations = (half_life + 1) ** 2 - elapsed_time // 10

# results

print("complete half-lives elapsed: " + str(half_lives_count))
print("approx. atoms remaining: " + str(atoms_count))
print("fraction of half-life left: " + str(fraction_half_life))
print("checking if pemdas still works: " + str(order_of_operations))

# integer division makes more sense because if you had fractions of an atom,
# we wouldn't be here to discuss semantics! so let's be safe and leave the atoms
# whole