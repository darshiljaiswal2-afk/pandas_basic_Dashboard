#collection
import collections
from collections import Counter, deque, namedtuple, OrderedDict, defaultdict

#containers
#list
#set
#dict
#tuple - inmutable

#types
#1 counter<- this video
#2 deque
#3 namedTuple()
#4 orderedDict
#5 defaultdict

c = Counter("gallad")
print(c)
c = Counter(['a', 'b', 'c', 'c'])
print(c)
c = Counter({'a': 1, 'b': 2, 'c': 3})
print(c)
c = Counter(cats=4, dogs=5)
print(c)
c = Counter(cats=4, dogs=5)
print(c['cats'])
print(c['dogs'])

d = "python is easy and python is powerful"
words = d.split()
count = Counter(words)
print(count)
print(dict(count))
print(c.elements())
print(c.most_common(2))

print("\n")
print(c.subtract(words))
print(c.update(words))
print(c.subtract(words))
print(c.clear())

print("\n")

d = deque([1, 2, 3])

d.append(4)  # add right
d.appendleft(0)  # add left

print(d)

print("\n")

Student = namedtuple("Student", ["name", "age", "branch"])

s = Student("Darshil", 19, "CSE")

print(s.name)
print(s.age)
print(s.branch)
print("\n")

d = defaultdict(int)

print(d["a"])

from collections import defaultdict

d = defaultdict(list)

d["CSE"].append("Darshil")
d["CSE"].append("Rahul")
d["AI"].append("Aman")

print(d)
# | Type          | Main purpose                         | Easy meaning       |
# | ------------- | ------------------------------------ | ------------------ |
# | `Counter`     | Count frequencies                    | **COUNT**          |
# | `deque`       | Add/remove both ends                 | **DOUBLE QUEUE**   |
# | `namedtuple`  | Named tuple fields                   | **TUPLE + NAMES**  |
# | `OrderedDict` | Order-specific dictionary operations | **ORDERED DICT**   |
# | `defaultdict` | Automatic default values             | **DICT + DEFAULT** |
