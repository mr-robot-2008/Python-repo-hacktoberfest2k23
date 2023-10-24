i = int(input())
c = int(input())

hcf = 1

if i == 0 or c == 0:
    # If either number is 0, the HCF is 0
    hcf = 0
elif i == 1 or c == 1:
    # If either number is 1, the HCF is the other number
    hcf = min(i, c)
else:
    # Use the existing code for other cases
    b = 2
    while (i > 1 and c > 1):
        if i % b == 0 and c % b == 0:
            hcf = hcf * b
            i = i // b
            c = c // b
        else:
            b = b + 1
        if b>c or b>i:
          break
print("HCF:", hcf)
