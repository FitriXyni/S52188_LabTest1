import collections
s = (input("Enter Your Letter : "))
print(collections.Counter(s).most_common(1)[0])
