#acp
t1 = (4,3,2,2,-1,18)
t2 = (2,4,8,8,3,2,9)

result = tuple(a * b for a, b in zip(t1, t2))
print(result)