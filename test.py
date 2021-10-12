option = input("Enter Your Name:")
vowels = set("aeiou")
dic = {1: "a", 2: "e", 3: "i", 4: "o", 5: "u"}
text = []
for char in option:
    if char in dic.values():
        if char == "a":
            res = char.replace('a', '2')
            text.append(res)

        elif char == "e":
            res = char.replace('e', '3')
            text.append(res)

        elif char == "i":
            res = char.replace('i', '4')
            text.append(res)

        elif char == "a":
            res = char.replace('o', '5')
            text.append(res)

        elif char == "a":
            res = char.replace('u', '7')
            text.append(res)

    if not char or char.isspace():
        res = char.replace(char, "-1")
        text.append(res)

    else:
        res = char.replace(char, '1')
        text.append(res)
        # res+=res
        # print(res)
    for i in range(0, len(text)):
        text[i] = int(text[i])
# print(text)
num = sum(text)
print(f'the total length of input:{num}')
