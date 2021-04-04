work_hours = 8
work_days = 5
pay_periods = 2
total = work_hours * work_days * pay_periods
rate = 17
pay = total * rate

print(pay)

# variables
name = "josh"
age = 30
# float
weight = 160.5
# list
kill_streak = [3, 5, 1, 9] # [90.9] list can contain sub lists
# range
players = list(range(1,10))
odds = list(range(1, 10, 2))
print(odds)

print(type(name), type(age), type(weight), type(kill_streak))

# dir(str)
# attributes
# help(str.upper)

# dir(__builtins__)

kill_streak_sum = sum(kill_streak)
length = len(kill_streak)
mean = kill_streak_sum / length

print(mean)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
tens = student_grades.count(10)

print(tens)

# dictionary (key:value)
family = {"josh": 30, "jess": 31, "bailey": 1.5}
age_sum = sum(family.values())
family_size = len(family)
average_age = age_sum / family_size

print(average_age)

# Tuple like a dictionary but non-mutable
palette_one = ("#f1f1f1", "#333333", "#4287f5")
palette_two = ("#f5f5f5", "#454545", "#6dd46a")
palette_three = ("#f0fff0", "#c7c7c7", "#725fb0")
palettes = (palette_one, palette_two, palette_three)

color_codes = palettes

temperature_data = {"morning": (3.1, 2.0, 4.9), "noon": (1.2, 0.9, 3.4), "evening": (0.2, 0.1, 1.0)}
day_temperatures = temperature_data
