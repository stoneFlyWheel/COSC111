import sys

running = True
while running:
    target = input("Please enter an integer: ")

    try:
        target = int(target)  
        count = 1

        while count <= target:
            if count % 2 == 0:
                print(count)
            else:
                pass
            count += 1

        print("Done!")

        running = False

    except:
        print("Invalid input. Please enter a valid number.")