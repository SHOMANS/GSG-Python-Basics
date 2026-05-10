# inputs
user_age = 12
with_parent = False

# constant
allowed_age = 18

# requirement
is_age_ok = user_age >= allowed_age # more than 18 or not
is_age_not_ok = not is_age_ok # if is_age_ok = True then this variable will be False

# allow the user to go if his age is +18, or his age is less than 18 and with parents.

condition = is_age_ok or (is_age_ok == False and with_parent) 
# condition = is_age_ok || (!is_age_ok && with_parent)

print(condition)

# not => !
total = 143
print(total != 120)


# the user can join the call if he is participant, 
# or he is not participant but invited by the team.
# 10 minutes

# inputs
is_participant = False
invited_by_team = False

# is_not_participant = not is_participant

can_join = is_participant or not is_participant and invited_by_team
# can_join = is_participant or is_not_participant and invited_by_team
# can_join = is_participant or invited_by_team # is ok

print(can_join) # False

# ()
# not
# and
# or