"""solvaer"""
def converter(num):
    """
    solva
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

    num = str(num)[::-1]

    word = []
    for i,j in enumerate(num):
        if i == 0:
            if int(num[:2][::-1]) in wordlist:
                word.append(wordlist[int(num[:2][::-1])])
            else:
                word.append(wordlist[int(j)])
                word.append(wordlist[int(num[i + 1]) * 10])

        elif i == 2:
            if num[i] == "0":
                word.append("")
            else:
                if num[:2][::-1] != "00":
                    word.append("AND")
                word.append(wordlist[int(j)] + "HUNDRED")

        elif i == 3:
            if num[3:5] == "00":
                word.append("")
            elif int(num[3:5][::-1]) in wordlist:
                word.append(wordlist[int(num[3:5][::-1])] + "THOUSAND")
            else:
                word.append(wordlist[int(j)] + "THOUSAND")
                word.append(wordlist[int(num[i + 1]) * 10])

        elif i == 5:
            if num[5:7] == "00":
                word.append("")
            elif int(num[5:7][::-1]) in wordlist:
                word.append(wordlist[int(num[5:7][::-1])] + "LAKH")
            else:
                word.append(wordlist[int(j)] + "LAKH")
                word.append(wordlist[int(num[i + 1]) * 10])

        elif i == 7:
            if int(num[7:9][::-1]) in wordlist:
                word.append(wordlist[int(num[7:9][::-1])] + "CRORE")
            else:
                word.append(wordlist[int(j)] + "CRORE")
                word.append(wordlist[int(num[i + 1]) * 10])

    return len("".join(reversed(word)))


def solver():
    """
    solver f
    """
    a = 1
    b = 1000
    return sum(converter(i) for i in range(a, b + 1))
