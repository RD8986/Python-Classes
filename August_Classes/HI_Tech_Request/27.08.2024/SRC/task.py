one = [1, 2, 3, 4, 5]
second = [10, 2, 4, 5]
findata = []
for x in one:
    if x not in findata:
        findata.append(x)
        for y in second:
            if y not in findata:
                findata.append(y)

print("Final Data = ", sorted(findata))
