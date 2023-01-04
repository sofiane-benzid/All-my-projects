x = 10
    y = 1
    n = number
    n2 = n
    n3 = n
    n4 = n
    n5 = n
    n6 = n
    n7 = n
    sum1 = 0
    sum2 = 0
    sum = 0
    first_digit = 0
    second_digit = 0
    doubled = 0
    counter = 0

    while n3 !=0:
        digits1 = (n/x)%10
        digits2 = (n2/y)%10
        doubled = digits1 * 2
        if doubled > 10:
            first_digit = int(doubled / 10)
            second_digit = int(doubled%10)
            doubled = int(first_digit + second_digit)
        x = x * 100
        y = y * 100
        sum1 += int(doubled)
        sum2 += int(digits2)
        n3 = n3 / 100

    while n4 != 0:
        n4 = n4 / 10
        counter += 1

    while n5 >=10:
        n5 = n5 / 10

    while n6 >= 100:
        n6 = n6 / 10

    n6 = n6 % 10

    if sum%10 != 0:
        print ("INVALID")
    elif (counter == 15 and n5 == 3) and (n6 == 4 or n5 == 7):
        print ("AMEX")
    elif (counter == 16 and n5 == 5) and (n5 == 1 or n5 == 2 or n5 == 3 or n5 == 4 or n5 == 5):
        print ("MASTERCARD")
    elif (counter == 13 or counter == 16) and n4 == 4:
        print ("VISA")
    else:
        print ("INVALID")