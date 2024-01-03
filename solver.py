"""Math 017"""


# Converter can only convert numbers upto 999999999
def converter(num):
    """
    returns the number of letters in a number written in words
    """
    wordlist = {
        0: "",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE",
        10: "TEN",
        11: "ELEVEN",
        12: "TWELVE",
        13: "THIRTEEN",
        14: "FOURTEEN",
        15: "FIFTEEN",
        16: "SIXTEEN",
        17: "SEVENTEEN",
        18: "EIGHTEEN",
        19: "NINETEEN",
        20: "TWENTY",
        30: "THIRTY",
        40: "FOURTY",
        50: "FIFTY",
        60: "SIXTY",
        70: "SEVENTY",
        80: "EIGHTY",
        90: "NINETY",
    }

    num = str(num)
    word = []

    word.append(wordlist[int(num[-1])])

    if len(num) >= 2 and int(num[-2:]) in wordlist:
        word.remove(wordlist[int(num[-1])])
        word.append(wordlist[int(num[-2:])])
    elif len(num) >= 2:
        word.append(wordlist[int(num[-2]) * 10])

    if len(num) >= 3 and num[-3] != "0":
        if num[-2:] != "00":
            word.append("AND")
        word.append(wordlist[int(num[-3])] + "HUNDRED")

    if len(num) >= 4 and int(num[-5:-3]) in wordlist and num[-5:-3] != "00":
        print("yes")
        word.append(wordlist[int(num[-5:-3])] + "THOUSAND")
    elif len(num) >= 5 and num[-5:-3] != "00":
        word.append(wordlist[int(num[-4])] + "THOUSAND")
        word.append(wordlist[int(num[-5]) * 10])

    if len(num) >= 6 and int(num[-7:-5]) in wordlist and num[-7:-5] != "00":
        word.append(wordlist[int(num[-7:-5])] + "LAKH")
    elif len(num) >= 6 and num[-7:-5] != "00":
        word.append(wordlist[int(num[-6])] + "LAKH")
        word.append(wordlist[int(num[-7]) * 10])

    if len(num) >= 8 and int(num[-9:-7]) in wordlist:
        word.append(wordlist[int(num[-9:-7])] + "CRORE")
    elif len(num) >= 8:
        word.append(wordlist[int(num[-8])] + "CRORE")
        word.append(wordlist[int(num[-9]) * 10])

    return "".join(reversed(word))


def solver(a, b):
    """
    returns number of letters between
    the numbers a and b if they are written in words
    """
    return sum(converter(i) for i in range(a, b + 1))
