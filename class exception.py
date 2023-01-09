
class InvalidAge(Exception):
    pass
try:
    age=int(input("Enter your age:"))
    if age<0:
        raise InvalidAge
except InvalidAge:
    print("Enter a positive value")
finally:
    print("Finished")


