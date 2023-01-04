# TODO

def main():
    while (True):
        try:
            n = int(input("Number: "))
        except:
            print("Must be a credit card number")
            continue
        break

    CheckSum(n)


def CheckSum(number):
    n = number
    n2 = n
    n3 = n
    digits1 = 0
    digits2 = 0
    doubled = 0
    first_digit = 0
    second_digit = 0
    sum1 = 0
    sum2 = 0
    sum = 0
    counter = 0
    while n2 != 0:
        digits1 = int((n2/10) % 10)
        digits2 = int(n2 % 10)
        doubled = digits1 * 2
        if doubled >= 10:
            first_digit = int(doubled / 10)
            second_digit = int(doubled % 10)
            doubled = first_digit + second_digit

        sum1 = sum1 + doubled
        sum2 = sum2 + digits2
        n2 = int(n2 / 100)
    sum = sum1 + sum2
    if sum%10 != 0:
        print ("INVALID")
    while (n3 != 0):
        n3 = int(n3 / 10)
        counter += 1

    if counter == 15 and (int(n/(10**(counter-2))) == 37 or int(n/(10**(counter-2))) == 34):
        print("AMEX")
    elif counter == 16 and (int(n/(10**(counter-2))) == 51 or int(n/(10**(counter-2))) == 52 or int(n/(10**(counter-2))) == 53 or int(n/(10**(counter-2))) == 54 or int(n/(10**(counter-2))) == 55):
        print("MASTERCARD")
    elif (counter == 13 or counter == 16) and int(n/(10**(counter-1))) == 4:
        print("VISA")
main()
