x = -1
if x < 0:
    raise Exception("No numbers below zero!")

def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Invalid age")
    else:
        print("Valid age:", age)

validate_age(25)
