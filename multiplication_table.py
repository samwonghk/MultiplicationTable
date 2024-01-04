"""
九因歌 Multiplication Table for number 1 to 9
"""

from os import system, name

# Clear the terminal screen
if name == 'posix':
    system('clear')
else:
    system('cls')

# Print the header line
print("")
print("懷舊練習簿 Exercise Book Old-day\n\n")

# Set the mapping of Chinese characters
chinese_char = {
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    6: "六",
    7: "七",
    8: "八",
    9: "九",
    10: "十"
}

# Print the table header
print("=" * 100)
print("|" + " " * 46 + "九因歌"[-1::-1] + " " * 46 + "|")
print("=" * 100)
print("|", end="")
for i in range(9,0,-1):
    print(f"    {chinese_char[i]}    |", end="")
print("")
print("|" + "-" * 98 + "|")

# Print the multiplication table
for i in range(1, 10):
    print("|", end="")
    for j in range(9, 0, -1):
        result = i * j
        if result < 10:
            if i == 3 and j == 3:
                result_char = '該'  + "  " + chinese_char[result]
            else:
                result_char = '如' + "  " + chinese_char[result]
        else:
            ten = result // 10
            digit = result % 10
            result_char = chinese_char[ten] + chinese_char[10]
            if digit > 0:
                result_char = result_char + chinese_char[digit]
            else:
                if ten == 1:
                    result_char = '得' + result_char
                else:
                    result_char = '中' + result_char

        print(f"{chinese_char[i]}{chinese_char[j]}{result_char}"[-1::-1], end="|")
    print("")
print("=" * 100)

# Print Capital Letters
for i in range(0, 26):
    print(chr(65+i), end="\t")
    if i == 12:
        print("")
print("")
print("")

# Print Lower-case Letters
for i in range(0, 26):
    print(chr(97+i), end="\t")
    if i == 12:
        print("")
print("")
print("")

# Print 1 to 0
for i in range(1, 11):
    print(f"\t    {i % 10}", end=" ")
print("")
print("")

for i, c in enumerate("𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"):
    print(c, end="\t")
    if i == 12:
        print("")
print("")
print("")

for i, c in enumerate("𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"):
    print(c, end="\t")
    if i == 12:
        print("")
print("")
print("")
print("")
print("")
