# while looping

# while loop
print("while loop")
i = 0
while i < 5:
    print(i)
    i += 1

# while loop with start
print("while loop with start")
i = 2
while i < 5:
    print(i)
    i += 1

# while loop with start and step
print("while loop with start and step")
i = 2
while i < 10:
    print(i)
    i += 2

# while loop with start, end and step
print("while loop with start, end and step")
i = 10
while i > 2:
    print(i)
    i -= 2


# while loop continue
print("while loop continue")
i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1

# while loop break
print("while loop break")
i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i += 1

# while loop pass
print("while loop pass")
i = 0
while i < 5:
    if i == 2:
        pass
        print("passing")
    print(i)
    i += 1

# while loop else
print("while loop else")
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("done")

# while loop else with break
print("while loop else with break")
i = 0
while i < 5:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("done")

# while loop else with continue
print("while loop else with continue")
i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print(i)
    i += 1
else:
    print("done")
