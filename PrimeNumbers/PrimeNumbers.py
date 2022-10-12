# Prime number:
# The program that prints the numbers entered from the keyboard if they are prime numbers.
# Klavyeden girilen sayıların  asal sayılar ise yazdıran program.

while True:
    num = int(input("Enter a number: "))
    counter = 0

    if num == 1:
        counter += 1
    for k in range(2, num):
        sonuc = int(num % k)
        if sonuc == 0:
            counter = counter + 1

    if counter == 0 and num != 2:
        print(num, "is a Prime number")

    if num == 2:
        print(num, "is a Prime  number")
