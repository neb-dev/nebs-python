# List Comprehension
populations = [1872, 1324, 3420]
calculated_pops = [population / 10 for population in populations]

print(calculated_pops)

# List Comprehension w/ Conditional
player_inventory = [201, 47, 360, -999]
stacks = [(item / 20).__round__() for item in player_inventory if item > 0]

print(stacks)

# If Else
results = [11, 212, -40, 199]
calculated_results = [result / 10 if result > 0 else 0 for result in results]
print(calculated_results)

# Convert
def sum_strings(data):
    converted_strings = [float(value) for value in data]
    return sum(converted_strings)

print(sum_strings(["1.1", "3.4", "2.0"]))