from random import randint # i need random numbers :D

# have lots of greetings so it doesn't get stale!
greeting = ["hello world!", "hi dr. puretskiy!", "good morning!", "good... whatever time it is!"]

first_name = "sage"
last_name = "briggs"
full_name = first_name + " " + last_name

# i like to think i'm a fun person, with lots of fun facts!
fun_fact = ["i love to read!", "i love to play video games!", "i've never had a pet!", "i'm a black belt in taekwondo!"]

lucky_number = randint(1, 50)

# putting it all together
print(greeting[randint(0, len(greeting) - 1)]) # be polite
print("my name is " + full_name + ".") # introduce yourself
print(fun_fact[randint(0, len(fun_fact) - 1)]) # be memorable
print("my lucky number today is: " + str(lucky_number)) # be lucky!