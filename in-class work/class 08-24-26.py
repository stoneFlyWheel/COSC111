list1 = ["apple", "cherry", "banana", "date", "elderberry"]

for fruit in list1:
    if fruit == "banana":
        print("i hate bananas! :(")
    else:
        print(fruit)

list1.remove("banana")

print(list1)

# 123 in base 4
print(int("123", 4))