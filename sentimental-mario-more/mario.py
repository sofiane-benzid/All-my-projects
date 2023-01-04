# TODO

while True:
    try:
        height = int(input("Height: "))
    except:
        print("number pls")
        continue
    if height > 0 and height <= 8:
        break

n = height
j = 0
k = j
for row in range(height):
    while (j < n):
        n = n - 1
        k = k + 1
        print(" " * n + "#" * k + " " * 2 + "#"*k)

