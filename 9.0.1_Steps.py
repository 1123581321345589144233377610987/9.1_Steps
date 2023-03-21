print("You will be entering the number of steps taken for each day in a week.")
data = {"Sunday": 0, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0}
total = 0
for i in data:
    data[i] = int(input(f"Please enter the number of steps taken on {i}: "))
    total += data[i]
print(f"You walked a total of {total:,} steps during the week.")
print(f"That was an average of {total/len(data):,.2f}")
min = data['Sunday']
max = data['Sunday']
maybemin = []
for i in data:
    if data[i] < min:
        min = data[i]
    if data[i] == min:
        maybemin += [i]
print(f"The minimum steps you took were {min} on:")
for i in maybemin:
    if data[i] == min:
        print(f"--- {i}")
maybemax = []
for i in data:
    if data[i] > max:
        max = data[i]
    if data[i] == max:
        maybemax += [i]
print(f"The maximum steps you took were {max} on:")
for i in maybemax:
    if data[i] == max:
        print(f"--- {i}")
