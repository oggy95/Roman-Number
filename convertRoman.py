roman = {1000: 'M',
         900: 'CM',
         500: 'D',
         400: 'CD',
         100: 'C',
         90: 'XC',
         50: 'L',
         40: 'XL',
         10: 'X',
         9: 'IX',
         5: 'V',
         4: 'IV',
         1: 'I'}

number = int(input())

listOfDigits = []

for i in range(4):
    listOfDigits.append(number % 10 * 10**i)
    number = number // 10

listOfDigits = reversed(listOfDigits)

for digit in listOfDigits:
    if digit in roman:
        print(roman[digit], end="")
    else:
        if digit != 0:
            for number in roman:
                first_digit = int(str(digit)[0])
                if 5 < first_digit < 10:
                    print(roman[5 * 10**(len(str(digit))-1)], end="")
                    for i in range(first_digit - 5):
                        print(roman[1 * 10**(len(str(digit))-1)], end="")
                    break
                elif digit % number == 0:
                    for i in range(number, digit+1, number):
                        print(roman[number], end="")
                    break
