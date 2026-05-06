# is_student = True
# age = 15

# print(is_student == True)
# print(age == 17)

# I'm looking for a student and his age is 17
# is_student is_age_17 Result
# True       True      True
# True       False     False
# False      True      False
# False      False     False


# is_student = False
# age = 16
# print(is_student == True and age == 17) # False



# I need a parent, or old man with 50 years old at least
# is_parent == True
# gender == "MALE"
# age >= 50

# 3 inputs
# is_parent => boolean => True, False
# gender => string => MALE, FEMALE
# age => integer 

# output 
# True or False

# is_parent gender age => result
# True      False  False  True
# False     True   False  False
# False     True   True   True

# and => all conditions should be True
# or => at least one condition should be True

# is_parent or (gender and age)

# user profile
name = "Yaseen"
is_parent = True
gender = "Male"
age = 30
# True
print(is_parent == True or (gender == "MALE" and age >= 50) ) 



# ========================================================
# ========================================================
print("==================")
# I need person has travel document or overseas and he should be an expert
is_expert = False
has_travel_document = True
is_overseas = True

# () priority
# and
# or

# 10 > 11 => False
# True === True?

print(has_travel_document == True or is_overseas==True and is_expert==True)
print(has_travel_document or is_overseas and is_expert)
# true or true and false 
# true or (true and false)
# true or false
# true

print((has_travel_document == True or is_overseas==True) and is_expert==True)
print((has_travel_document or is_overseas) and is_expert)
# (true or true) and false
# true and false
# false


# # I need person should be an expert and has travel document, or overseas
# is_expert=False
# has_trav=True
# is_overses=True
# print(is_expert==True and has_trav==True or is_overses==True)