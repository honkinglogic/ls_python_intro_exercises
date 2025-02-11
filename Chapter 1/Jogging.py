x = float(input())
y = float(input())
days = 1
distance = x

while distance < y:
    distance += (distance * 0.1)
    days += 1
print(days)