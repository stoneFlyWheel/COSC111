# for letter in "Hello, World!":
    # print(letter, end = " ")

select = "SPOCK"
select = select.lower()
if select == "spock":
    select = select[0].upper() + select[1:]

print(select)