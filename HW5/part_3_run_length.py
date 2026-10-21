def compress(data):
    compress_list = []
    index = 0
    print(len(data))
    while index < len(data):
        target = data[index]
        count = 1

        while index + 1 < len(data) and data[index + 1] == target:
            count += 1
            index += 1
        compress_list.append([target, count])
        index += 1
    print(compress_list)

compress(['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a'])