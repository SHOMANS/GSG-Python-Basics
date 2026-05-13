final_average = float(input("enter AVG "))

print(final_average)

if 100 >= final_average >= 85:
    print("Excellent")
if 75 <= final_average < 85:
    print("Very Good")
if 65 <= final_average < 75:
    print("Good")
if 50 <= final_average < 65:
    print("Pass")
else:
    print("Fail")
# if (final_average > 100 or final_average < 0): # validation
#     print("wrong AVG: you should enter value between 0 and 100")
