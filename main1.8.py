# Keyword Arguments
# def concat_strings(a = "Hello", b) will throw an error due to invalid order of default/non-default arugment. a being default arugment b being non-default
def concat_strings(a = "Hello", b = "World"): 
    return a + " " + b

print(concat_strings())
print(concat_strings("Goodbye"))

# Arbitary number of arugments
def mean(*args): # args can be named whatever you'd like
    return sum(args) / len(args)

print(1,8,14,21)

def sort_strings(*args):
    strings = [arg.upper() for arg in args]
    # strings.sort()
    return sorted(strings)

print(sort_strings("Hello", "Goodbye", "Tempalte", "Unique", "Zebra"))

def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3))

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=9))