# part A --------

def compress(data):
    compress_list = []
    index = 0
    while index < len(data):
        target = data[index]
        count = 1

        while index + 1 < len(data) and data[index + 1] == target:
            count += 1
            index += 1
        compress_list.append(target)
        compress_list.append(count)
        index += 1
    print(compress_list)

compress(['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a'])

# part B --------

def decompress(data):
    decompress_list = []
    index = 0

    while index < len(data):
        letter_index = index
        num_index = index + 1
        letter = data[letter_index]
        num = data[num_index]

        for letters in range(num):
            decompress_list.append(letter)

        index += 2
    
    print(decompress_list)

decompress(['a', 3, 'b', 2, 'c', 1, 'a', 2])