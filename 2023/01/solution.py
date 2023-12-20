with open("input.txt") as file:
    input = file.read().splitlines()

_sum = 0
for line in input:
    num = ""
    for char in line:
        if char.isdigit():
            num += char        
            break
    for char in reversed(line):
        if char.isdigit():
            num += char
            break
    num = int(num)
    _sum += num

print(_sum)
    