#Part 1: open the text file for reading

reader = open("COSC111/in-class assignments/dracula.txt", "r")

#Part 2: initialize the following variables (will be used for counting names):

jonathan_count = 0
dracula_count = 0
mina_count = 0
lucy_count = 0
renfield_count = 0

for line in reader:
    line = line.lower()
    
    jonathan_count += line.count("jonathan")
    dracula_count += line.count("dracula")
    mina_count += line.count("mina")
    lucy_count += line.count("lucy")
    renfield_count += line.count("renfield")

#no changes to the following lines need to be made

#(they will print out correct counts after you complete Parts 1-3 above)

reader.close()

print("jonathan:", jonathan_count)

print("dracula:", dracula_count)

print("mina:", mina_count)

print("lucy:", lucy_count) 

print("renfield:", renfield_count)