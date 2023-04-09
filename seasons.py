from datetime import date
import sys
import re

def main():
    birthdate = input("What is your date of birth? ")
    number = get_birthdate(birthdate)
    minutes = getWords(number)
    print(minutes, "minutes")


def get_birthdate(birthdate):
    if re.search(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", birthdate):
        birthdate = birthdate.split("-")
        birthdate = date(int(birthdate[0]), int(birthdate[1]),int(birthdate[2]))
        timedelta = date.today() - birthdate
        return timedelta.days * 24 * 60
    else:
        return sys.exit("Invalid date")


# Number to Words

# Main Logic
ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')

twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')

suffixes = ('', 'Thousand', 'Million', 'Billion')

def process(number, index):

    if number=='0':
        return 'Zero'

    length = len(number)

    if(length > 3):
        return False

    number = number.zfill(3)
    words = ''

    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])

    words += '' if number[0] == '0' else ones[hdigit]
    words += ' Hundred ' if not words == '' else ''

    if(tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]

    elif(tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]

    elif(tdigit == 0):
        words += ones[odigit]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '

    if(not len(words) == 0):
        words += suffixes[index]

    return words

def getWords(number):
    length = len(str(number))

    if length>12:
        return 'This program supports upto 12 digit numbers.'

    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    for i in range(length - 1, -1, -3):
        words.append(process(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp

    return final_words.strip()

if __name__ == "__main__":
    main()