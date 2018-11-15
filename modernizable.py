### Exercise 1

# 1.1

print "Hello",
print "world!"

# 1.2

print 1, 2, 3

import sys
for i in range(5):
    sys.stdout.write(str(i))

print "".join(str(i) for i in range(5))

# 1.3

import sys
print >>sys.stderr, "This is an error message"


# 1.4

filename = "test.txt"
with open(filename, "w") as f:
    print >>f, "This is the first line of the file :-)"
    print >>f, "This is line number", 2


### Exercise 2

def print_type_and_value(x):
    print type(x), x

print_type_and_value(range(10))

l = [0, 1, 2, 3, 4, 5]
print_type_and_value(filter(lambda x: x%2 == 0, l))
print_type_and_value(map(lambda x: 2*x, l))
print_type_and_value(zip(l, l))

d = {"a": 1, "b": 2}
print_type_and_value(d.keys())
print_type_and_value(d.values())
print_type_and_value(d.items())

print_type_and_value(xrange(10))

d = {"a": 1, "b": 2}
print_type_and_value(d.iterkeys())
print_type_and_value(d.itervalues())
print_type_and_value(d.iteritems())


# 2.1

def min_max(items):
    return min(items), max(items)

def is_even(n):
    return n % 2 == 0

print(min_max(filter(is_even, [1, 2, 3, 4, 5])))



# 2.2

def delete_false_items(d):
    for k in d.keys():
        if not d[k]:
            del d[k]

d = {1: True, 2: False, 3: True, 4: False, 5: True, 6: False}
delete_false_items(d)
print(d)



### Exercise 3

print type(3 / 2), 3 / 2

# 3.1

def binary_search(x, items, start=None, end=None):
    """Returns True if and only if x is found in items[start:end]. If start"""
    if start is None:
        start = 0
    if end is None:
        end = len(items)
    if start >= end:
        return False
    middle = (start + end) / 2
    if items[middle] == x:
        return True
    elif items[middle] < x:
        return binary_search(x, items, middle + 1, end)
    else:
        return binary_search(x, items, start, middle)

items = (2, 3, 4, 6, 7, 9, 12)

# Find numbers between 1 and 13 which are not in 'items'
print(tuple(x for x in range(1, 14) if not binary_search(x, items)))
 

### Exercise 4

def print_and_round(x):
    print("round({}) == {}".format(x, round(x)))

for x in (-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5):
    print_and_round(x)


