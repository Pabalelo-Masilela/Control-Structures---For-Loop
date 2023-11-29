'''This program is designed to display a desired,pre set patternn based on a numerical order relationship.'''
# Initial pattern
complete_pattern = "*"
for pattern in range(1,10):
# Adding a * charecter to each iteration between 1-5
    if pattern < 5:
        print(complete_pattern)
        complete_pattern = complete_pattern + "*"
# Removing a * charecter for each iteration between 5-10
    else:
        print(complete_pattern)
        complete_pattern = complete_pattern[1:]