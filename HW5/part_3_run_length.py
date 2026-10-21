# part A --------

def compress(data):
    # set initial values
    compress_list = []
    index = 0

    # while index is less than how long the list is
    while index < len(data):
        # initial values
        target = data[index]
        count = 1

        # while the next index is still in range and the next element in data is still target
        while index + 1 < len(data) and data[index + 1] == target:
            # increment counter
            count += 1
            # check next index
            index += 1

        # loop ends, target is something else
        
        # append what was counted
        compress_list.append(target)
        # append how many there are
        compress_list.append(count)

        # move on to next target
        index += 1
    print(compress_list)

compress(['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a'])

# part B --------

def decompress(data):
    # set initial values
    decompress_list = []
    index = 0

    # while index is in range
    while index < len(data):
        # set initial values
        letter_index = index
        num_index = index + 1
        letter = data[letter_index]
        num = data[num_index]

        # append as many copies of the target letter is specified in num
        for letters in range(num):
            decompress_list.append(letter)

        # increment index by two (so letter_index stays even)
        index += 2
    
    print(decompress_list)

decompress(['a', 3, 'b', 2, 'c', 1, 'a', 2])