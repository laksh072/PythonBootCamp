# Write a Python program that manages a list of student scores. Perform the following operations step-by-step:
# Create an empty list to store scores.
# Append the scores: 85, 90, 78, 92, 88
# Insert the score 80 at index
# Remove the score 92 from the list
# Sort the scores in ascending order
# Reverse the list
# Find and print the maximum and minimum score
# Check if 90 is in the list
# Print the total number of scores
# Slice and print the first three scores
# find the last element from the list
# replace the score with new score on the index 2
# create a new copied list also

list_scores = []
list_scores.extend([67, 87, 55, 89, 24])
list_scores[2] = 80
print(list_scores)
list_scores.remove(89)

list_scores.sort()
print(f"sorted- {list_scores}")

list_scores.reverse()
print(f"revered- {list_scores}")

hasItem = 86 in list_scores
print(f"hasitem 86- {hasItem}")

sliceList = list_scores[0:3]
print(f"sliced- {sliceList}")

for item in list_scores:
    print(item)

list_scores.append(45)
print(f"last- {list_scores[-1]}")

list_scores[2] = 100
print(f"added 100 at index2 - {list_scores}")
print(f"max- {max(list_scores)}")
print(f"min- {min(list_scores)}")

dup_score = list(list_scores)
print(f"duplicate list - {dup_score}")
