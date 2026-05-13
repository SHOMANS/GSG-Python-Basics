# validation

avg = float(input("enter the avg "))

# readability
# best practice
# code quality

# if (avg > 100 or avg < 0):
#     print("enter valid number between 0 and 100")
# elif avg >= 90:
#     print("first")
# elif avg >= 80:
#     print("second")
# elif avg >= 70:
#     print("third")
# elif avg >= 60:
#     print("fourth")
# else:
#     print("fail")


if (0 <= avg <= 100):
    if avg >= 90:
        print("first")
    elif avg >= 80:
        print("second")
    elif avg >= 70:
        print("third")
    elif avg >= 60:
        print("fourth")
    else:
        print("fail")
else:
    print("enter valid number between 0 and 100")




