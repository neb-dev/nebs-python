def create_sentence(user_input):
    question_list = ("who", "when", "where", "how", "what", "why")
    if user_input.startswith(question_list): # startswith accepts a string or tuple of strings
        return "{}?".format(user_input.capitalize())
    else:
        return "{}.".format(user_input.capitalize())

inputs = []

while True:
    user_input = input("say something: ")
    if user_input == "\end":
        break
    else:
        inputs.append(create_sentence(user_input))

print(" ".join(inputs))


# first_input = ""
# second_input = ""
# third_input = ""

# while len(first_input) == 0:
#     first_input = input("say something: ")
#     while len(second_input) == 0:
#         second_input = input("say something: ")
#         while len(third_input) == 0:
#             third_input = input("say something: ")

# print("{} {} {}".format(first_input.capitalize().__add__("."), second_input.capitalize().__add__("?"), third_input.capitalize().__add__(".")))