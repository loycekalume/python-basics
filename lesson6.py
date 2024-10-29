#lists
scores=[90,40,45,80,47,55,66,33,20,90]
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])

scores.append(61)#adds an element at the end
print(scores)

scores.pop(0)# removes n element from list
print(scores)

scores.sort()
print(scores)

scores.sort(reverse=True)#sorts in descending order
print(scores)