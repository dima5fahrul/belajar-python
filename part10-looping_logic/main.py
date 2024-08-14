# looping logic
sisi = 10

# for
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

# while
count = 1
while count <= sisi:
    print("*" * count)
    count += 1

# while with break
count = 1
while True:
    print("*" * count)
    count += 1
    if count > 5:
        break

# while tanpa ganjil
count = 1
while count <= sisi:
    if count % 2 == 0:
        print("*" * count)
    count += 1
