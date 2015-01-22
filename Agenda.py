__author__ = 'Kyle Lam'
import csv

agencies = []

# read the file
# file is 2 columns with a tab separation
with open('input3.txt', 'r') as f:  
    reader = csv.reader(f, delimiter='\t')
    for a, b in reader:
        entry = (int(a), int(b))
        agencies.append(entry)

days, agencyNum = agencies.pop(0);
solution = [None] * days  # to enable insertion between {0...days}
# sort the agency list based on 2nd entry i.e. value
agencies = sorted(agencies, key=lambda tup: tup[1])

print(agencies)
# largest elements are at the back

index = len(agencies) - 1   # start from the back of sort agenda to avoid shifting
added = 0   # counts the number of insertions into the solution list

# Attempt insertion until we've filled the list or until we have tried each agenda entry
while (added <= days)and( index>=0):
    day, val = agencies[index]
    # insert in an off by 1 manner, index 0 will be treated as day 1
    if day > days:
        day = days

    # the slot in the solution list is empty
    if solution[day-1]is None :
        solution.insert(day-1, agencies[index]) # day 2 entry would be slotted into index 1
        solution.pop(day)   # after above insertion, previous entry is pushed 1 spot back
        added += 1          # increase count
        index -= 1          # move onto preceding entry in agenda list

    # the slot we attempted to insert into already has a value
    else:
        while day > 0:      # decrementally try each slot until we either succeed or run out of days
            if solution[day-1]is None:
                solution.insert(day-1, agencies[index])
                solution.pop(day)
                added += 1
                index -= 1
                day = -1
                print(solution)
            else:           # doesn't fit in current slot, try the previous one
                day -= 1
                if day == 0:    # it isn't possible to insert this agenda entry
                    index -= 1  # decrease index and move to preceding entry

solutionIterator = iter(solution)

print(solution)









