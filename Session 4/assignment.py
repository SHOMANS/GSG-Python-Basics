print("\nAnswers of Question 2:")
points = 40
points += 20
points -=10
points *= 2

is_vip = points >= 100
print("Final points:", points)
print("Is the customer is VIP?", is_vip)
print("Can the customer get a free delivrey?", points > 150 or is_vip)

# DRY => Don't Repeat Yourself



total_bill = 120
points = 20
premium_member = True

print(total_bill > 150 and points > 50 or premium_member)
# False and False or True
# (False and False) or True
# False or True
# True

print(total_bill > 150 and (points > 50 or premium_member))
# False and (False or True)
# False and True
# False