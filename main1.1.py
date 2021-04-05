seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
print(seconds)

seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)

# Index
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

# Range
temperatures = [90.9, 88.5, 88, 92.7, 99]
print(temperatures[0:2])
print(temperatures[:2])
print(temperatures[3:5])
print(temperatures[3:])

# Negative Indexes
print(temperatures[-1])
print(temperatures[-5])
print(temperatures[-2:])
print(temperatures[-4:-2])
print(temperatures[:-1])