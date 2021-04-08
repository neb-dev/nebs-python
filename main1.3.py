def input_shrooms(total):
    if  total >= 10:
        print("you collected extra shrooms! excellent work!")
    elif total >= 5:
        print("you collected enough shrooms. not too bad.")
    elif total < 5:
        print("you don't have enough shrooms. better luck next time...")
    else:
        print("invalid input type. what were you thinking?")

# Command Line Input
user_shrooms = int(input("enter the amount of shrooms in your inventory (integer values only): "))
input_shrooms(user_shrooms)

# String Formatting
brand_input = input("enter the name of your brand: ")
print("your brand name is: %s" % brand_input)

# String Formatting (Python 3.6)
slogan_input = input("enter your brand's slogan: ")
slogan = f"your slogan is: {slogan_input}"
print(slogan)

# String Formatting with multiple variables
currency = input("what is your currency: ")
amount = input("how much do you need: ")
print("thanks for your purchase of %s candies. your %s payment was received!" % (amount, currency))

spell = input("name of spell: ")
spell_type = input("spell type: ")
new_spell = f"you learned {spell}. it is a {spell_type} spell"
print(new_spell)

band = "Nostalgia"
drummer = "Josh"
print("{} is the drummer for the band {}".format(drummer, band))
    