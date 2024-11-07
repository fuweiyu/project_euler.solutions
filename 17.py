# Dictionary with written numbers
numbers_in_words = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
    1000: "one thousand"
}

def number_to_words(n):
    if n in numbers_in_words:
        return numbers_in_words[n]
    elif n < 100:
        return numbers_in_words[n // 10 * 10] + "-" + numbers_in_words[n % 10] if n % 10 != 0 else numbers_in_words[n // 10 * 10]
    elif n < 1000:
        result = numbers_in_words[n // 100] + " hundred"
        if n % 100 != 0:
            result += " and " + number_to_words(n % 100)
        return result
    return ""

# Loop to count letters in numbers from 1 to 1000
letters=''
total_letters=0
for i in range(1, 1001):
    letters=number_to_words(i).replace(" ", "")
    letters=letters.replace("-", "")
    total_letters=total_letters+int(len(letters))
print(total_letters)